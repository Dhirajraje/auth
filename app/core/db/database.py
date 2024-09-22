from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base,sessionmaker


_DB_URL = 'sqlite+aiosqlite:///./test.db'
_ECHO_SQL = True


Base = declarative_base()

engine = create_async_engine(_DB_URL, echo=_ECHO_SQL)


async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)



async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session