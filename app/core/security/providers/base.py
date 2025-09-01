from abc import ABC, abstractmethod
from typing import Any

class BaseProvider(ABC):
    name: str

    @abstractmethod
    def is_configured(self) -> bool:
        ...

    @abstractmethod
    def authorization_url(self, state: str) -> str:
        ...

    @abstractmethod
    async def fetch_user(self, code: str) -> dict[str, Any]:
        ...

    # Optional for non-OAuth providers (e.g., LDAP)
    async def authenticate(self, **kwargs) -> dict | None:
        return None
