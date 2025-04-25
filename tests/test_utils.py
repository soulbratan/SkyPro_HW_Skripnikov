import json
from unittest.mock import mock_open, patch
from typing import Any
from src.utils import load_transactions_list
from src.external_api import exchange_api

# 1) Тесты функции load_transactions_list с помощью заглушек
# 2) Тест функции exchange_api с помощью заглушки функции ("requests.get")

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
