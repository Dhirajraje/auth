import httpx
import urllib.parse
from app.core.config import settings
from .base import BaseProvider

AUTH = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
TOKEN = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
USERINFO = "https://graph.microsoft.com/v1.0/me"
SCOPE = "openid email profile User.Read"

class MicrosoftProvider(BaseProvider):
    name = "microsoft"

    def is_configured(self) -> bool:
        return all([settings.MS_CLIENT_ID, settings.MS_CLIENT_SECRET, settings.MS_REDIRECT_URI])

    def authorization_url(self, state: str) -> str:
        params = {
            "client_id": settings.MS_CLIENT_ID,
            "response_type": "code",
            "redirect_uri": settings.MS_REDIRECT_URI,
            "response_mode": "query",
            "scope": SCOPE,
            "state": state,
        }
        return f"{AUTH}?{urllib.parse.urlencode(params)}"

    async def fetch_user(self, code: str) -> dict:
        async with httpx.AsyncClient(timeout=20) as client:
            data = {
                "client_id": settings.MS_CLIENT_ID,
                "client_secret": settings.MS_CLIENT_SECRET,
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": settings.MS_REDIRECT_URI,
                "scope": SCOPE,
            }
            token = (await client.post(TOKEN, data=data)).json()
            headers = {"Authorization": f"Bearer {token.get('access_token')}"}
            profile = (await client.get(USERINFO, headers=headers)).json()
            # Microsoft Graph 'id' is the user id, 'mail' or 'userPrincipalName' for email
            email = profile.get("mail") or profile.get("userPrincipalName")
            return {
                "provider": self.name,
                "provider_user_id": profile.get("id"),
                "email": email,
                "raw_profile": profile,
            }
