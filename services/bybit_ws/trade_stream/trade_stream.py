from datetime import datetime

from pybit.unified_trading import WebSocket
from functools import partial
from asyncio import sleep

ws = WebSocket(testnet=False, channel_type="linear")

def handle_message(source, producer, message):
        print(f"✅ trade_stream {source} {message['topic']}")

        producer.send(source, message)
        producer.flush()

async def trade_stream(pairs, producer):
    # pairs = ['SOLUSDT']
    print('start trade_stream')
    try:
        # Подписываемся на несколько пар
        for pair in pairs:
            ws.trade_stream(symbol=pair,
                                callback=partial(handle_message, f"trade_stream_{pair}", producer)
                                )

        # Обрабатываем события в цикле
        while True:
            await sleep(1)  # Не даём программе завершиться, ожидаем сообщений
    except Exception as e:
        print(f"Error occurred: {e}")
        await sleep(5)  # Ждём 5 секунд перед переподключением
        await trade_stream(pairs, producer)  # Рекурсивно переподключаем
