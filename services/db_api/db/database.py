from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from config.config import settings

# sync_engine = create_engine(
#     url=settings.DATABASE_URL_psycopg,
#     # echo=True,
#     # pool_size=5,
#     # max_overflow=10,
#
# )

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    # echo=True,
    # pool_size=5,
    # max_overflow=10,

)

# session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

async def get_async_session() -> AsyncSession:
    async with async_session_factory() as session:
        yield session

class Base(DeclarativeBase):
    pass




