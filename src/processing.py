# Новый модуль для функций обработки данных
import re
from collections import Counter
from typing import Any


def filter_by_state(unfiltered_list: list, filtering_state: str = "EXECUTED") -> list:
    """Функция фильтрующая входящий список по ключу "state". По умолчанию ключ равен "EXECUTED"."""
    if filtering_state != "EXECUTED" and filtering_state != "CANCELED" and filtering_state != "PENDING":
        raise ValueError("Неправильное имя фильтра")
    return [
        i for i in unfiltered_list if i.get("state", " ") == filtering_state
    ]  # Возвращаем отфильтрованный по ключу 'state' список с помощью list comprehension


def sort_by_date(unsorted_list: Any, reverse: bool = True) -> Any:
    """Функция сортирует список словарей по дате. По умолчанию сортировка по убыванию."""
    for i in unsorted_list:
        if len(i["date"]) < 1 or int(i["date"][8:10]) > 31 or int(i["date"][5:7]) > 12 or not i["date"][0:4].isdigit():
            raise ValueError("Некорректная дата")
    return sorted(
        unsorted_list, key=lambda x: x["date"], reverse=reverse
    )  # Возвращаем отсортированный по дате список с помощью sorted


def search_transactions(transactions: list[dict], search_text: str) -> list[dict]:
    """Функция принимает список словарей с транзакциями и строку поиска. Возвращает отфильтрованный список словарей"""
    new_list = list()
    pattern = f"{search_text}"
    for i in transactions:
        text_description = i.get("description", " ")
        search_result = re.search(pattern, text_description, flags=re.IGNORECASE)
        if search_result:
            new_list.append(i)
    return new_list


def count_descriptions(transactions: list[dict], category_list: Any) -> Any:
    """
    Функция принимает список словарей и список категорий операций.
    Возвращает словарь с посчитанными операциями по каждой категории
    """
    try:
        if type(category_list) is list:
            new_list = list()
            descriptions_list = [i.get("description", []) for i in transactions]
            for i in category_list:
                for item in descriptions_list:
                    if i.lower() in item.lower():
                        new_list.append(item)
            counted = dict(Counter(new_list))
            return counted
        else:
            return "Второй аргумент не список"
    except Exception as e:
        return f"Error: {e}"


test_list = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]
