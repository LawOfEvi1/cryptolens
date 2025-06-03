import asyncio

from common.common_module_db import fill_pairs
from common.kafka_producer import get_kafka_producer
from order_book.order_book_stream import subscribe_order_book


async def main():
    pairs = await fill_pairs()
    producer = get_kafka_producer()
    await subscribe_order_book(pairs, producer)


if __name__ == "__main__":
    asyncio.run(main())
