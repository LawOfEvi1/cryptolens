import asyncio

from all_liquidation import run_listener_all_liquidation
from trade_stream import run_listener_trade_stream
from kline_service.main import main as run_listener_get_kline_stream
from order_book.main import main as run_orderbook


# from orderbook_service.main import run as run_orderbook  # в будущем

async def main():

    task1 = asyncio.create_task(run_listener_get_kline_stream())
    # task2 = asyncio.create_task(run_orderbook())
    task3 = asyncio.create_task(run_listener_all_liquidation())
    task4 = asyncio.create_task(run_listener_trade_stream())

    # Ждём их завершения
    await asyncio.gather(
                        task1
                         # , task2
                         , task3
                         ,
                         task4
                         )


if __name__ == "__main__":
    asyncio.run(main())
