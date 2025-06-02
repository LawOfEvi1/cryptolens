from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, MappedColumn
from sqlalchemy import Integer, select, update as sql_update, delete as sql_delete, Identity
from typing import TypeVar, Type, Optional, Any, Dict

from db import BaseModel

Base = declarative_base()
T = TypeVar("T", bound="BaseORMModel")


class BaseORMModel(BaseModel):
    __abstract__ = True

    id: Mapped[int] = MappedColumn(Integer, Identity(start=1, cycle=False), primary_key=True, autoincrement=True)



    @classmethod
    def from_message(cls: Type[T], payload: dict) -> T:
        allowed_keys = {c.name for c in cls.__table__.columns}
        filtered = {k: v for k, v in payload.items() if k in allowed_keys}
        return cls(**filtered)

    @classmethod
    async def create(cls: Type[T], payload: dict, session: AsyncSession) -> T:
        obj = cls.from_message(payload)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    @classmethod
    async def get_by_id(cls: Type[T], id_: int, session: AsyncSession) -> Optional[T]:
        result = await session.execute(select(cls).where(cls.id == id_))
        return result.scalar_one_or_none()

    @classmethod
    async def all(cls: Type[T], session: AsyncSession) -> list[T]:
        result = await session.execute(select(cls))
        return result.scalars().all()

    @classmethod
    async def update(cls: Type[T], id_: int, values: dict, session: AsyncSession) -> Optional[T]:
        await session.execute(
            sql_update(cls)
            .where(cls.id == id_)
            .values(**values)
        )
        await session.commit()
        return await cls.get_by_id(id_, session)

    @classmethod
    async def delete(cls: Type[T], id_: int, session: AsyncSession) -> bool:
        result = await session.execute(sql_delete(cls).where(cls.id == id_))
        await session.commit()
        return result.rowcount > 0
