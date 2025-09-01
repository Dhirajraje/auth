from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.authn import User, Identity
from app.core.security.utils import verify_password, hash_password, create_access_token

async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    res = await session.execute(select(User).where(User.email == email))
    return res.scalar_one_or_none()

async def create_user(session: AsyncSession, email: str, password: str | None = None, confirmed: bool = False) -> User:
    u = User(email=email, password_hash=hash_password(password) if password else None, is_confirmed=confirmed)
    session.add(u)
    await session.flush()
    return u

async def upsert_identity_user(session: AsyncSession, provider: str, provider_user_id: str, email: str | None, raw_profile: dict) -> User:
    # Find identity
    res = await session.execute(select(Identity).where(Identity.provider == provider, Identity.provider_user_id == provider_user_id))
    ident = res.scalar_one_or_none()
    if ident:
        user = await session.get(User, ident.user_id)
        return user

    # Else attach to existing user by email or create new
    user = None
    if email:
        user = await get_user_by_email(session, email)
    if not user:
        user = await create_user(session, email=email or f"{provider_user_id}@{provider}.local", password=None, confirmed=True)

    ident = Identity(provider=provider, provider_user_id=provider_user_id, user_id=user.id, raw_profile=str(raw_profile))
    session.add(ident)
    await session.flush()
    return user

async def authenticate_user(session: AsyncSession, email: str, password: str) -> User | None:
    user = await get_user_by_email(session, email)
    if not user or not user.password_hash:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user

def issue_token_for_user(user: User) -> str:
    return create_access_token(sub=str(user.id))
