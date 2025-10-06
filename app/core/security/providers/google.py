import httpx
import urllib.parse
from app.core.config import settings
from .base import BaseProvider

GOOGLE_AUTH = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO = "https://www.googleapis.com/oauth2/v3/userinfo"
SCOPE = "openid email profile"

class GoogleProvider(BaseProvider):
    name = "google"

    def is_configured(self) -> bool:
        return all([settings.GOOGLE_CLIENT_ID, settings.GOOGLE_CLIENT_SECRET, settings.GOOGLE_REDIRECT_URI])

    def authorization_url(self, state: str) -> str:
        print(settings.GOOGLE_REDIRECT_URI)
        params = {
            "client_id": settings.GOOGLE_CLIENT_ID,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "response_type": "code",
            "scope": SCOPE,
            "state": state,
            "access_type": "offline",
            "prompt": "consent",
        }
        return f"{GOOGLE_AUTH}?{urllib.parse.urlencode(params)}"

    async def fetch_user(self, code: str) -> dict:
        async with httpx.AsyncClient(timeout=20) as client:
            data = {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            }
            token = (await client.post(GOOGLE_TOKEN, data=data)).json()
            headers = {"Authorization": f"Bearer {token.get('access_token')}"}
            profile = (await client.get(GOOGLE_USERINFO, headers=headers)).json()
            return {
                "provider": self.name,
                "provider_user_id": profile.get("sub"),
                "email": profile.get("email"),
                "raw_profile": profile,
            }
