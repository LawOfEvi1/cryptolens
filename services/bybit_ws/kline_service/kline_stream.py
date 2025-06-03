from pybit.unified_trading import WebSocket
from functools import partial
from asyncio import sleep

ws = WebSocket(testnet=False, channel_type="linear")

def handle_kline_msg(source, producer, message):
    if message['data'][0]['confirm']:
        print(f"✅ KLINE {source} {message['topic']}")
        producer.send(source, message)
        producer.flush()

async def subscribe_kline(pairs, producer):
    print('start subscribe_kline')
    try:
        # Подписываемся на несколько пар с различными интервалами
        for pair in pairs:
            for interval in [1, 5, 15, 60]:
                ws.kline_stream(
                    interval=interval,
                    symbol=pair,
                    callback=partial(handle_kline_msg, "get_kline_stream", producer)
                )

        # Обрабатываем события в цикле
        while True:
            await sleep(1)  # Не даём программе завершиться, ожидаем сообщений
    except Exception as e:
        print(f"Error occurred: {e}")
        await sleep(5)  # Ждём 5 секунд перед переподключением
        await subscribe_kline(pairs, producer)  # Рекурсивно переподключаем
