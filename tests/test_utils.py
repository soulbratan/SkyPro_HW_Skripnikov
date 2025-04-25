import json
from typing import Any
from unittest.mock import mock_open, patch

import pytest

from src.external_api import exchange_api
from src.utils import load_transactions_list, transaction_amount

# 1) Тесты функции load_transactions_list с помощью заглушек
# 2) Тест функции exchange_api с помощью заглушки функции ("requests.get")
# 3) Тест функции transaction_amount с помощью фикстуры
# 4) Тест функции transaction_amount с помощью параметризации
# 5) Тест функции transaction_amount с помощью заглушки функции ("exchange_api")


# 1)
def test_load_transactions_list_success() -> None:
    """Тест успешной загрузки списка транзакций."""
    test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    test_json = json.dumps(test_data)

    with patch("builtins.open", mock_open(read_data=test_json)):
        result = load_transactions_list("test.json")
        assert result == test_data


def test_load_transactions_list_empty() -> None:
    """Тест успешной загрузки списка транзакций."""
    with patch("builtins.open", mock_open(read_data="")):
        result = load_transactions_list("empty.json")
        assert result == []


def test_load_transactions_list_invalid_file() -> None:
    """Тест невалидного файла (должен вернуть[])."""
    with patch("builtins.open", mock_open(read_data="invalid_json}")):
        result = load_transactions_list("invalid.json")
        assert result == []


def test_load_transactions_list_not_a_list() -> None:
    """Тест JSON, который не является списком (должен вернуть [])."""
    test_data = {"id": 1, "amount": 100}  # Словарь
    test_json = json.dumps(test_data)

    with patch("builtins.open", mock_open(read_data=test_json)):
        result = load_transactions_list("not_a_list.json")
        assert result == []


def test_load_transactions_list_file_not_found() -> None:
    """Тест отсутствующего файла (должен вернуть [])."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions_list("nonexistent.json")
        assert result == []


# 2)
@patch("requests.get")
def test_exchange_api_return(mock_get: Any) -> Any:
    mock_get.return_value.json.return_value = {"result": 80.0}
    assert float(exchange_api("USD", "RUB", 1.0)) == 80.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1.0",
        headers={"apikey": "ec2dgEIZNQPgWKhhMBuIjKEQKHmUP2py"},
        data={},
    )


# 3)
def test_transaction_amount_rub(transaction_1: dict) -> None:
    result = transaction_amount(transaction_1)
    assert result == 43318.34


# 4)
@pytest.mark.parametrize(
    "some_transactions, result",
    [
        ({"operationAmount": {"amount": "1018.34", "currency": {"name": "руб.", "code": "RUB"}}}, 1018.34),
        ({"operationAmount": {"amount": "0.0", "currency": {"name": "руб.", "code": "RUB"}}}, 0.0),
        ({"operationAmount": {"amount": "1234.12", "currency": {"name": "руб.", "code": "RUB"}}}, 1234.12),
        (
            {"operation": {"amount": "1234.12", "currency": {"name": "руб.", "code": "RUB"}}},
            "Некорректные данные транзакции",
        ),
        (
            {"operationAmount": {"am": "1234.12", "currency": {"name": "руб.", "code": "RUB"}}},
            "Некорректные данные транзакции",
        ),
        (
            {"operationAmount": {"amount": "1234.12", "curre": {"name": "руб.", "code": "RUB"}}},
            "Некорректные данные транзакции",
        ),
    ],
)
def test_transaction_amount_param(some_transactions: dict, result: Any) -> None:
    results = transaction_amount(some_transactions)
    assert results == result


# 5)
@patch("src.external_api.exchange_api")
def test_transaction_amount_api(mock_exchange_api: Any) -> None:
    mock_exchange_api.return_value = "100.0"
    test_data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "100.0", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    assert transaction_amount(test_data) == 100.0
