import os
from typing import Any

import requests
from dotenv import load_dotenv


def exchange_api(from_currency: str, to_currency: str, amount: float) -> Any:
    """Функция обращения к Exchange Rates Data API для конвертации валюты по текущему курсу и вывода значения"""
    load_dotenv()  # Загружаем переменные из .env-файла
    apilayer_token = os.getenv("API_KEY")  # Получаем значение API_KEY
    headers = {"apikey": f"{apilayer_token}"}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    payload: dict = {}
    # Формируем запрос согласно документации API
    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()  # Вызовет исключение при статусе 4XX/5XX
        result = response.json()
        return result["result"]
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None


# r = exchange_api('USD', 'RUB', 10.0)
#
# print(r)
