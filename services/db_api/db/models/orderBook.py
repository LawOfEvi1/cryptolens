from sqlalchemy import Float, BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, MappedColumn

from db.models.BaseORMModel import BaseORMModel


class OrderBook(BaseORMModel):
    __tablename__ = 'order_book'

    symbol: Mapped[str] = MappedColumn(ForeignKey("trading_pair.symbol"))
    sum_ask: Mapped[float]
    sum_bid: Mapped[float]
    delta: Mapped[float] = MappedColumn(Float, default=0.0, nullable=False)
    timestamp_ms: Mapped[int] = MappedColumn(BigInteger)
    limit_req: Mapped[int]

    def __str__(self) -> str:
        return f"OrderBook(symbol={self.symbol}, delta={self.delta})"
