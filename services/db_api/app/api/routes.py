from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.shemas.kline import KlineIn
from db import Kline, MaximumOrderBookLimits, Liquidation, VolumeMotion
from db.database import get_async_session  # ты можешь реализовать Depends здесь


router = APIRouter()



@router.post("/create-kline")
async def create_kline(data: KlineIn
                       , session: AsyncSession = Depends(get_async_session)):
    result = await Kline.create(data.model_dump(), session)
    return {"id": result.id}





class MaximumOrderBookLimitsIn(BaseModel):
    symbol: str
    delta_count_coin: float
    max_buyers_price: float
    max_buyers_coin: float
    max_sellers_price: float
    max_sellers_coin: float
    average_price: float
    timestamp_ms: float

@router.post("/create-maximum-order-book-limits")
async def create_MaximumOrderBookLimits(data: MaximumOrderBookLimitsIn
                       , session: AsyncSession = Depends(get_async_session)):
    result = await MaximumOrderBookLimits.create(data.model_dump(), session)
    return {"id": result.id}

class LiquidationIn(BaseModel):
    symbol: str
    timestamp_ms: float
    type: str
    volume: float
    price: float

@router.post("/create-liquidation")
async def create_kline(data: LiquidationIn
                       , session: AsyncSession = Depends(get_async_session)):
    result = await Liquidation.create(data.model_dump(), session)
    return {"id": result.id}

class VolumeMotionIn(BaseModel):
    symbol: str
    timestamp_ms: float
    delta: float
    delta_min: float
    delta_max: float
    bids: float
    asks: float
    price: float
    start: bool
    end: bool
    trend: str

@router.post("/create-volume-motion")
async def create_volume_motion(data: VolumeMotionIn
                       , session: AsyncSession = Depends(get_async_session)):
    result = await VolumeMotion.create(data.model_dump(), session)
    return {"id": result.id}














