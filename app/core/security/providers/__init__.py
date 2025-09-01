from fastapi import HTTPException

from app.core.security.providers.google import GoogleProvider
from app.core.security.providers.microsoft import MicrosoftProvider
from .ldap_provider import LDAPProvider

PROVIDER_REGISTRY = {
    "ldap": LDAPProvider,
    "google": GoogleProvider,
    "microsoft": MicrosoftProvider,
}


def get_provider(name: str):
    Provider = PROVIDER_REGISTRY.get(name)
    if not Provider:
        raise HTTPException(status_code=404, detail="Provider not found")
    provider = Provider()
    if not provider.is_configured():
        raise HTTPException(status_code=400, detail=f"Provider '{name}' not configured")
    return provider