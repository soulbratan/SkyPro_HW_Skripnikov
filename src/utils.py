import json
import logging
from pathlib import Path
from typing import Any

from src import external_api

# Путь относительно текущего файла
current_dir = Path(__file__).parent  # Директория текущего скрипта
file_path = current_dir.parent / "logs" / "utils.log"  # Поднимаемся вверх и ищем файл

# Абсолютный путь
absolute_path = file_path.resolve()

logger = logging.getLogger("utils")  # Создание объекта логгера для модуля utils
file_handler = logging.FileHandler(filename=absolute_path, mode="w", encoding="UTF-8")  # Настраиваем хэндлер для файла
file_formatter = logging.Formatter(
    fmt="%(asctime)s %(filename)s, %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)  # Настраиваем форматер
file_handler.setFormatter(file_formatter)  # Устанавливаем форматер
logger.addHandler(file_handler)  # Добавляем хэндлер в логер
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования


def load_transactions_list(file_name: str) -> list:
    """
    Функция принимает на вход (file_name) путь до JSON-файла и
     возвращает список словарей с данными о финансовых транзакциях.
     Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    logger.info(f"Func <{load_transactions_list.__name__}> started. Checking the path - ({file_name})")
    try:
        with open(file_name, "r", encoding="utf-8") as f:  # Обращаемся к файлу по заданному пути
            data = json.load(f)  # Преобразуем JSON-файл в файл Python
            if isinstance(data, list):  # Проверка на соответствие типа данных
                logger.info(
                    f"Func <{load_transactions_list.__name__}> successfully completed. The list has been received."
                )
                return data  # Если соответствует, возвращаем список словарей
            logger.warning("Returned the empty list.")
            return []  # В обратном случае возвращаем пустой список
    except (FileNotFoundError, json.JSONDecodeError) as e:  # Если не найден, или не список возвращаем []
        logger.error(f"<line43> {e}")
        return []


# file_names = "../data/operations.json"

# result = load_transactions_list(file_names)
#
# print(result[0])


def transaction_amount(transaction: dict) -> Any:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях (float).
    Если транзакция была в другой валюте, то происходит конвертация через Exchange Rates Data API по текущему курсу.
    """
    logger.info(f"Func <{transaction_amount.__name__}> started.")
    if "operationAmount" in transaction:  # Проверяем наличие ключей
        if (
            "amount" in transaction["operationAmount"] and "currency" in transaction["operationAmount"]
        ):  # Проверяем наличие ключей
            if "RUB" in transaction["operationAmount"]["currency"]["code"]:  # Проверяем валюту операции
                logger.info(f"Func <{transaction_amount.__name__}> successfully completed.")
                return float(transaction["operationAmount"]["amount"])  # Если "RUB" выводим сумму транзакции (float)
            else:
                logger.info("Starting request to Exchange Rates Data API")
                amount = float(transaction["operationAmount"]["amount"])
                from_currency = transaction["operationAmount"]["currency"]["code"]
                to_currency = "RUB"
                result = float(
                    external_api.exchange_api(from_currency, to_currency, amount)
                )  # Иначе конвертируем через API и выводим
                logger.info(f"Func <{transaction_amount.__name__}> completed.")
                return result
        else:
            logger.error("No key found with the name <amount> or <currency>")
            return "Некорректные данные транзакции"
    else:
        logger.error("No key found with the name <operationAmount>")
        return "Некорректные данные транзакции"


# transactions = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {"amount": "1.0", "currency": {"name": "USD", "code": "USD"}},
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560",
# }
#
#
# x = transaction_amount(transactions)
# print(x)
