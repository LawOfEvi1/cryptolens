from sqlalchemy import String, BigInteger, Float, ForeignKey
from sqlalchemy.orm import Mapped, MappedColumn

from db.models.BaseORMModel import BaseORMModel


class MaximumOrderBookLimits(BaseORMModel):
    __tablename__ = 'maximum_order_book_limits'

    symbol: Mapped[str] = MappedColumn(ForeignKey("trading_pair.symbol"))
    delta_count_coin: Mapped[float] = MappedColumn(Float, default=0.0, nullable=False)
    max_buyers_price: Mapped[float] = MappedColumn(Float, default=0.0, nullable=False)
    max_buyers_coin: Mapped[float] = MappedColumn(Float, default=0.0, nullable=False)
    max_sellers_price: Mapped[float] = MappedColumn(Float, default=0.0, nullable=False)
    max_sellers_coin: Mapped[float] = MappedColumn(Float, default=0.0, nullable=False)
    average_price: Mapped[float] = MappedColumn(Float, default=0.0, nullable=False)
    timestamp_ms: Mapped[int] = MappedColumn(BigInteger)

    def __str__(self) -> str:
        return (
            f"MaxOBL: {self.symbol}, buyers_price: {self.max_buyers_price}, "
            f"sellers_price: {self.max_sellers_price}"
        )
