import requests

from common import url_start


async def fill_pairs():
    url = url_start + "api/v1/trading-pair/select-all"
    result = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # выбросит исключение, если статус не 200

        data = response.json()  # если ответ в JSON формате
        for tp in data:
            result.append(tp["symbol"])

    except requests.exceptions.RequestException as e:
        print("❌ Ошибка запроса:", e)

    return  result