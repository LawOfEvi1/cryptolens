from typing import Union

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker




@DeprecationWarning
async def proceed_schemas(engine: AsyncEngine, metadata)->None:
    pass
    # try:
    #     async with engine.begin() as conn:
    #         await conn.run_sync(metadata.create_all)
    # except Exception as e:
    #     print(f"Error occurred while applying schemas: {e}")
    #     # await AsyncEngine.rollback()
    #     raise

def get_session_maker(engine: AsyncEngine)->sessionmaker:
    return sessionmaker(engine, class_=AsyncSession)