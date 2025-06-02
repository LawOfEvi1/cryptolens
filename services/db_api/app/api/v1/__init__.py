from fastapi import APIRouter
from . import kline, liquidation, orderbook, volume_motion, trading_pair

api_router = APIRouter()
api_router.include_router(kline.router)
# api_router.include_router(liquidation.router)
# api_router.include_router(orderbook.router)
# api_router.include_router(volume_motion.router)
api_router.include_router(trading_pair.router)
