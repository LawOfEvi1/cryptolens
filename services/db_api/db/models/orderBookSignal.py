from sqlalchemy.orm import MappedColumn, Mapped
from sqlalchemy import Integer, String, Float, BigInteger, Boolean
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.BaseORMModel import BaseORMModel  # твой базовый класс с create и т.п.

class OrderBookSignal(BaseORMModel):
    __tablename__ = 'order_book_signal'

    symbol: Mapped[str] = MappedColumn(String, nullable=False)
    buy: Mapped[bool] = MappedColumn(Boolean, nullable=False)
    sell: Mapped[bool] = MappedColumn(Boolean, nullable=False)
    limit_req: Mapped[int] = MappedColumn(Integer, nullable=False)
    delta_count_coin: Mapped[float] = MappedColumn(Float, nullable=False)
    current_price: Mapped[float] = MappedColumn(Float, nullable=False)
    value_deal: Mapped[float] = MappedColumn(Float, nullable=False)
    timestamp_ms: Mapped[int] = MappedColumn(BigInteger, nullable=False)

    def __str__(self) -> str:
        return f"symbol: {self.symbol}, value_deal: {self.value_deal}, buy: {self.buy}"
