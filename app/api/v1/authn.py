import secrets
from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from fastapi.responses import RedirectResponse
from app.core.database import get_session
from app.core.security.providers import get_provider
from app.schemas.authn import (
    LDAPLoginRequest,
    LoginRequest,
    SignupRequest,
    TokenResponse,
)
from app.services.authn import (
    authenticate_user,
    create_user,
    issue_token_for_user,
    upsert_identity_user,
)
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/ldap/login", response_model=TokenResponse)
async def ldap_login(
    payload: LDAPLoginRequest, session: AsyncSession = Depends(get_session)
):
    provider = get_provider("ldap")
    profile = await provider.authenticate(
        username=payload.username, password=payload.password
    )
    if not profile:

        raise HTTPException(status_code=401, detail="LDAP authentication failed")
    user = await upsert_identity_user(
        session,
        provider="ldap",
        provider_user_id=profile["provider_user_id"],
        email=profile.get("email"),
        raw_profile=profile.get("raw_profile", {}),
    )
    await session.commit()
    token = issue_token_for_user(user)
    return TokenResponse(access_token=token)


@router.post("/auth/signup", response_model=TokenResponse)
async def signup(payload: SignupRequest, session: AsyncSession = Depends(get_session)):
    # In a real system, email confirmation is required.
    user = await create_user(
        session, email=payload.email, password=payload.password, confirmed=True
    )
    await session.commit()
    token = issue_token_for_user(user)
    return TokenResponse(access_token=token)


@router.post("/auth/token", response_model=TokenResponse)
async def token(payload: LoginRequest, session: AsyncSession = Depends(get_session)):
    user = await authenticate_user(session, payload.email, payload.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    token = issue_token_for_user(user)
    return TokenResponse(access_token=token)


@router.get("/auth/provider/{name}/authorize")
async def oauth_authorize(name: str):
    provider = get_provider(name)
    state = secrets.token_urlsafe(16)
    url = provider.authorization_url(state=state)
    return RedirectResponse(url)


@router.get("/auth/provider/{name}/callback", response_model=TokenResponse)
async def oauth_callback(
    name: str, code: str, session: AsyncSession = Depends(get_session)
):
    provider = get_provider(name)
    profile = await provider.fetch_user(code)
    user = await upsert_identity_user(
        session,
        provider=profile["provider"],
        provider_user_id=profile["provider_user_id"],
        email=profile.get("email"),
        raw_profile=profile.get("raw_profile", {}),
    )
    await session.commit()
    token = issue_token_for_user(user)
    return TokenResponse(access_token=token)
