from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Тестируем функцию "filter_by_currency":
# 1) С помощью фикстуры по разным валютам;
# 2) При условии пустого списка на входе обработки;
# 3) С помощью параметризации. Фильтр по разным валютам (t_example - входной список).


# 1)
def test_filter_by_currency_usd(transaction: list) -> None:
    result = list(filter_by_currency(transaction, "USD"))
    assert result == [
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
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


def test_filter_by_currency_rub(transaction: list) -> None:
    result = list(filter_by_currency(transaction, "RUB"))
    assert result == [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


# 2)
def test_filter_by_currency_empty() -> None:
    result = list(filter_by_currency([], "RUB"))
    assert result == []


# 3)
t_example = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "durham", "code": "AED"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "yen", "code": "JPY"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "euro", "code": "EU"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


@pytest.mark.parametrize(
    "currency_code, exp_result",
    [
        (
            "EU",
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "euro", "code": "EU"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
        ),
        (
            "USD",
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
        ),
        (
            "JPY",
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "yen", "code": "JPY"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                }
            ],
        ),
        (
            "AED",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "durham", "code": "AED"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        ),
        ("UK", []),
    ],
)
def test_filter_by_currencies(currency_code: str, exp_result: list) -> None:
    result = list(filter_by_currency(t_example, currency_code))
    assert result == exp_result


# Тестируем функцию "transaction_descriptions":
# 1) С помощью фикстуры;
# 2) При условии пустого списка на входе обработки;
# 3) С помощью параметризации.


# 1)
def test_transaction_descriptions(transaction: list) -> None:
    result = transaction_descriptions(transaction)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод с карты на карту"
    assert next(result) == "Перевод организации"


# 2)
empty_transactions: list = []


def test_transaction_description_empty() -> None:
    result = list(transaction_descriptions(empty_transactions))
    assert result == []


# 3)
@pytest.mark.parametrize(
    "next_transaction, result",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            "Перевод организации",
        ),
        (
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
            "---Нет описания операции!!!---",
        ),
        (
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                }
            ],
            "Перевод со счета на счет",
        ),
        (
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "descriptiona": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
            None,
        ),
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            "Перевод организации",
        ),
    ],
)
def test_transaction_descriptions_param(next_transaction: list, result: str) -> None:
    results = transaction_descriptions(next_transaction)
    assert next(results) == result


# Тестируем функцию "card_number_generator":
# 1) Начальных значений;
# 2) Конечных значений;
# 3) Некорректные входные данные(отрицательные, больше 9999999999999999, start > end, другой тип вместо цифры-int).


# 1)
def test_card_number_generator_1() -> Any:
    result = card_number_generator(1, 5)
    assert next(result) == "0000 0000 0000 0001"
    assert next(result) == "0000 0000 0000 0002"
    assert next(result) == "0000 0000 0000 0003"
    assert next(result) == "0000 0000 0000 0004"
    assert next(result) == "0000 0000 0000 0005"


# 2)
def test_card_number_generator_2() -> Any:
    result = card_number_generator(9999999999999995, 9999999999999999)
    assert next(result) == "9999 9999 9999 9995"
    assert next(result) == "9999 9999 9999 9996"
    assert next(result) == "9999 9999 9999 9997"
    assert next(result) == "9999 9999 9999 9998"
    assert next(result) == "9999 9999 9999 9999"


# 3)
def test_card_number_generator_wrong_1() -> None:
    with pytest.raises(ValueError) as exc_info:
        next(card_number_generator(-5, -1))
    assert str(exc_info.value) == "Некорректные заданные значения"


def test_card_number_generator_wrong_2() -> None:
    with pytest.raises(ValueError) as exc_info:
        next(card_number_generator(9999999999999999, 10000000000000000))
    assert str(exc_info.value) == "Некорректные заданные значения"


def test_card_number_generator_wrong_3() -> None:
    with pytest.raises(ValueError) as exc_info:
        next(card_number_generator(5, 1))
    assert str(exc_info.value) == "Некорректные заданные значения"


def test_card_number_generator_wrong_4() -> None:
    with pytest.raises(ValueError) as exc_info:
        next(card_number_generator("5", 1))
    assert str(exc_info.value) == "Неправильный тип заданного значения"
