import datetime
from sqlalchemy.future import select
from sqlalchemy import Boolean, Integer, VARCHAR, DateTime
from sqlalchemy.orm import Mapped, MappedColumn

from db.models.BaseORMModel import BaseORMModel
from db.database import async_session_factory


class User(BaseORMModel):
    __tablename__ = 'users'

    user_id: Mapped[int] = MappedColumn(Integer, unique=True, nullable=False)
    username: Mapped[str | None] = MappedColumn(VARCHAR(32), nullable=True)
    phone_number: Mapped[str | None] = MappedColumn(VARCHAR(15), nullable=True)
    reg_date: Mapped[datetime.datetime] = MappedColumn(DateTime, default=datetime.datetime.utcnow)
    upd_date: Mapped[datetime.datetime | None] = MappedColumn(DateTime, onupdate=datetime.datetime.utcnow)
    send_notification: Mapped[bool] = MappedColumn(Boolean, default=True, nullable=False)

    def __str__(self) -> str:
        return f"User: {self.username}, id: {self.user_id}"

    @classmethod
    async def get_all_users(cls):
        """Получает всех пользователей, у которых send_notification=True"""
        try:
            async with async_session_factory() as session:
                result = await session.execute(
                    select(cls).filter(cls.send_notification == True)
                )
                return result.scalars().all()
        except Exception as e:
            print(f"Error in get_all_users: {e}")
            return []
