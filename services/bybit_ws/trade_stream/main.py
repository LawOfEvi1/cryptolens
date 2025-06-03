import asyncio

from common.common_module_db import fill_pairs
from common.kafka_producer import get_kafka_producer
from trade_stream.trade_stream import trade_stream


async def main():
    pairs = await fill_pairs()
    producer = get_kafka_producer()
    await trade_stream(pairs, producer)


if __name__ == "__main__":
    asyncio.run(main())
    # test
