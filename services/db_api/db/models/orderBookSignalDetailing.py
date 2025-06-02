from sqlalchemy.orm import MappedColumn, Mapped
from sqlalchemy import Integer, String, Float, ForeignKey
from db.models.BaseORMModel import BaseORMModel
from db.database import async_session_factory

class OrderBookSignalDetailing(BaseORMModel):
    __tablename__ = 'order_book_signal_detailing'

    id_signal: Mapped[int] = MappedColumn(ForeignKey("order_book_signal.id"), nullable=False)
    price: Mapped[float] = MappedColumn(Float, nullable=False)
    count: Mapped[float] = MappedColumn(Float, nullable=False)
    s: Mapped[str] = MappedColumn(String, nullable=False)

    def __str__(self) -> str:
        return f"{self.s}"

# Обертка для пакетной вставки сессии (bulk insert) — её оставляем вне класса
async def record_order_book_signal_detailing_list(data: list[dict]):
    async with async_session_factory() as session:
        await session.execute(
            OrderBookSignalDetailing.__table__.insert(),
            data
        )
        await session.commit()
