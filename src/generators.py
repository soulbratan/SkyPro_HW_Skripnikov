from typing import Any


def filter_by_currency(transactions: list, currency_code: str) -> Any:
    """Функция фильтрации списка словарей по заданной валюте (возвращает итератор)"""
    for transaction in transactions:  # Перебираем словари
        operation_amount = transaction.get("operationAmount", {})  # Заходим в нужный нам ключ
        currency = operation_amount.get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: list) -> Any:
    """Функция обработки списка словарей и возврата описания каждой операции по очереди"""
    for transaction in transactions:
        if transaction.get("description") == "":  # Проверяем наличие данных по операции
            yield "---Нет описания операции!!!---"
        else:
            yield transaction.get("description")


def card_number_generator(start: Any, end: int) -> Any:
    """Функция генерации номеров банковских карт от заданных начального до конечного значений"""
    if type(start) is not int or type(end) is not int:  # Входные данные неправильного типа
        raise ValueError("Неправильный тип заданного значения")
    if not (0 <= start <= end <= 9999999999999999):  # Ограничиваем диапазон генерируемых номеров
        raise ValueError("Некорректные заданные значения")
    for number in range(start, end + 1):
        card_num = "0000000000000000"  # Базовый номер
        card_num = card_num[: -len(str(number))] + str(number)
        yield f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:16]}"
