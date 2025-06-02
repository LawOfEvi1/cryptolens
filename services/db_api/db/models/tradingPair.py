from __future__ import annotations

from sqlalchemy.future import select
from sqlalchemy import String, Boolean
from sqlalchemy.orm import MappedColumn, Mapped
from sqlalchemy.dialects.postgresql import insert

from db.database import async_session_factory
from db.models.BaseORMModel import BaseORMModel


class TradingPair(BaseORMModel):
    __tablename__ = 'trading_pair'

    symbol: Mapped[str] = MappedColumn(String, nullable=False, unique=True, primary_key = False)
    ref: Mapped[str] = MappedColumn(String)
    spot: Mapped[bool] = MappedColumn(Boolean, default=False, nullable=False)
    inverse: Mapped[bool] = MappedColumn(Boolean, default=False, nullable=False)
    linear: Mapped[bool] = MappedColumn(Boolean, default=False, nullable=False)
    option: Mapped[bool] = MappedColumn(Boolean, default=False, nullable=False)
    base_coin: Mapped[str] = MappedColumn(String)
    quote_coin: Mapped[str] = MappedColumn(String)
    contract_type: Mapped[str] = MappedColumn(String)
    use: Mapped[bool] = MappedColumn(Boolean, default=True, nullable=False)

    def __str__(self) -> str:
        return f"TradingPair: {self.name} ({self.symbol}), url: {self.ref}"

    @staticmethod
    async def save_trading_pair(user_data: dict):
        async with async_session_factory() as session:
            stmt = insert(TradingPair).values(
                symbol=user_data["symbol"],
                name=user_data["name"],
                spot=user_data["spot"],
                inverse=user_data["inverse"],
                linear=user_data["linear"],
                base_coin=user_data["baseCoin"],
                quote_coin=user_data["quoteCoin"],
                contract_type=user_data["contractType"],
                ref='https://www.bybit.com/trade/usdt/' + user_data["symbol"],
                option=user_data["option"]
            ).on_conflict_do_nothing(index_elements=["symbol"])

            await session.execute(stmt)
            await session.commit()

    @staticmethod
    async def select_trading_pair(symbol: str) -> TradingPair | None:
        async with async_session_factory() as session:
            result = await session.execute(
                select(TradingPair).filter(TradingPair.symbol == symbol)
            )
            return result.scalars().one_or_none()

    @staticmethod
    async def select_trading_pair_all() -> list[TradingPair]:
        async with async_session_factory() as session:
            result = await session.execute(
                select(TradingPair).filter(TradingPair.use == True)
            )
            return result.scalars().all()

    @staticmethod
    async def update_trading_pair_use(symbol: str, use: bool):
        async with async_session_factory() as session:
            result = await session.execute(
                select(TradingPair).filter(TradingPair.symbol == symbol)
            )
            trading_pair = result.scalar_one_or_none()
            if trading_pair:
                trading_pair.use = use
                await session.commit()
            else:
                print(f"Торговая пара с символом {symbol} не найдена.")
