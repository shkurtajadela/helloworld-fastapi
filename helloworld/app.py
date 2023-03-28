from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine

from helloworld.settings import settings
from helloworld.routers import router
from helloworld.dependencies import database
# from helloworld.logging import setup_logger
from helloworld.models.file import *

# setup_logger()

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(
    router,
    prefix=settings.API_PREFIX
)


async def init_models():
    async with database.engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


@app.on_event('startup')
async def startup_event():
    database.engine = create_async_engine(
        url=settings.DATABASE_URL, echo=settings.DATABASE_ECHO, future=True
    )
    # await init_models()


@app.on_event('shutdown')
async def shutdown_event():
    engine: AsyncEngine = database.engine
    await engine.dispose()
