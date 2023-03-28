from typing import AsyncGenerator, Optional, Type

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine

from helloworld.repositories.base import BaseRepository

engine: Optional[AsyncEngine] = None  # initialize in app.py at startup


async def get_engine() -> AsyncEngine:
    if engine is not None:
        return engine
    raise RuntimeError('Application not started.')


async def get_connection(
    engine: AsyncEngine = Depends(get_engine),
) -> AsyncGenerator[AsyncConnection, None]:
    async with engine.connect() as connection:
        yield connection


def get_repository(repository: Type[BaseRepository]):
    async def wrapper(
        connection: AsyncConnection = Depends(get_connection),
    ) -> BaseRepository:
        instance = repository(connection=connection)
        return instance

    return wrapper
