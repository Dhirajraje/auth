from ldap3 import Server, Connection, AUTO_BIND_NO_TLS, SIMPLE
from app.core.config import settings
from .base import BaseProvider

class LDAPProvider(BaseProvider):
    name = "ldap"

    def is_configured(self) -> bool:
        print("Checking LDAP configuration...")
        print(f"LDAP URI: {settings.LDAP_URI}")
        print(f"LDAP Bind DN Template: {settings.LDAP_BIND_DN_TEMPLATE}")
        return bool(settings.LDAP_URI and settings.LDAP_BIND_DN_TEMPLATE)

    def authorization_url(self, state: str) -> str:
        raise NotImplementedError("LDAP does not use browser OAuth. Use /auth/ldap/login.")

    async def fetch_user(self, code: str) -> dict:
        raise NotImplementedError("LDAP does not support authorization code flow.")

    async def authenticate(self, *, username: str, password: str) -> dict | None:
        bind_dn = settings.LDAP_BIND_DN_TEMPLATE.format(username=username)
        print(f"Attempting LDAP bind with DN: {bind_dn}")
        server = Server(settings.LDAP_URI)
        try:
            conn = Connection(server, user=bind_dn, password=password, authentication=SIMPLE, auto_bind=True)
            # In real use, query attributes. Here we just return a basic profile.
            return {"provider": self.name, "provider_user_id": bind_dn, "email": None, "raw_profile": {"dn": bind_dn}}
        except Exception:
            return None
