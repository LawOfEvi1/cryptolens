from sqlalchemy import String, BigInteger, Float, ForeignKey
from sqlalchemy.orm import Mapped, MappedColumn

from db.models.BaseORMModel import BaseORMModel


class Kline(BaseORMModel):
    __tablename__ = 'kline'

    symbol: Mapped[str] = MappedColumn(ForeignKey("trading_pair.symbol"))
    start: Mapped[int] = MappedColumn(BigInteger)
    end: Mapped[int] = MappedColumn(BigInteger)
    interval: Mapped[str] = MappedColumn(String)
    open: Mapped[float] = MappedColumn(Float)
    close: Mapped[float] = MappedColumn(Float)
    high: Mapped[float] = MappedColumn(Float)
    low: Mapped[float] = MappedColumn(Float)
    volume: Mapped[float] = MappedColumn(Float)
    turnover: Mapped[float] = MappedColumn(Float)

    def __str__(self) -> str:
        return f"Kline: {self.symbol}, high: {self.high}, low: {self.low}"
