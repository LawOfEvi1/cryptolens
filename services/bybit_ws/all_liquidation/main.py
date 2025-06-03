import asyncio

from all_liquidation.all_liquidation_stream import subscribe_all_liquidastion
from common.common_module_db import fill_pairs
from common.kafka_producer import get_kafka_producer


async def main():
    pairs = await fill_pairs()
    producer = get_kafka_producer()
    await subscribe_all_liquidastion(pairs, producer)


if __name__ == "__main__":
    asyncio.run(main())
    # test
