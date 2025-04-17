from typing import Any


def filter_by_currency(transactions: list, currency_code: str) -> Any:
    """Функция фильтрации списка словарей по заданной валюте (возвращает итератор)"""
    for transaction in transactions:  # Перебираем словари
        operation_amount = transaction.get("operationAmount", {})  # Заходим в нужный нам ключ
        currency = operation_amount.get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: list) -> Any:
    pass


def card_number_generator(start: Any, end: int) -> Any:
    pass