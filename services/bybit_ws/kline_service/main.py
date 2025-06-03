import asyncio

from common.common_module_db import fill_pairs
from common.kafka_producer import get_kafka_producer
from kline_service.kline_stream import subscribe_kline




async def main():
    pairs = await fill_pairs()
    producer = get_kafka_producer()
    await subscribe_kline(pairs, producer)

if __name__ == "__main__":
    asyncio.run(main())
    # test
