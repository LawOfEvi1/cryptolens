from sqlalchemy import String, BigInteger, Float
from sqlalchemy.orm import MappedColumn, Mapped

from db.models.BaseORMModel import BaseORMModel


class Liquidation(BaseORMModel):
    __tablename__ = 'liquidation'

    symbol: Mapped[str] = MappedColumn(String)
    timestamp_ms: Mapped[int] = MappedColumn(BigInteger)
    type: Mapped[str] = MappedColumn(String)
    volume: Mapped[float] = MappedColumn(Float)
    price: Mapped[float] = MappedColumn(Float)

    def __str__(self) -> str:
        return f"Liquidation: {self.symbol}, volume: {self.volume}, price: {self.price}"
