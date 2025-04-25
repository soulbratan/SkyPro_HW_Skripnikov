import json
from unittest.mock import mock_open, patch

from src.utils import load_transactions_list

# 1) Тесты функции load_transactions_list с помощью заглушек

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
