from pydantic_settings import BaseSettings

# from pydantic import AnyUrl
# from typing import List


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./dev.db"
    JWT_SECRET: str = "devsecret-change-me"
    JWT_ALG: str = "HS256"
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 60

    ALLOWED_PROVIDERS: str = "google,microsoft,ldap"

    GOOGLE_CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None
    GOOGLE_REDIRECT_URI: str | None = None

    MS_CLIENT_ID: str | None = None
    MS_CLIENT_SECRET: str | None = None
    MS_REDIRECT_URI: str | None = None

    LDAP_URI: str | None = None
    LDAP_BIND_DN_TEMPLATE: str | None = None

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
