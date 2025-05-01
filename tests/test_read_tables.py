import csv
from typing import Any
from unittest.mock import mock_open, patch

import pytest
from src.read_tables import csv_to_dict


def test_successful_csv():
    # Подготовка тестовых данных в формате CSV
    csv_data = """id;name;amount
1;Alice;100
2;Bob;200
3;Charlie;300"""
    # Мокаем open и csv.DictReader
    with patch('builtins.open', mock_open(read_data=csv_data)):
        result = csv_to_dict("dummy_path.csv")
        # Проверяем корректность преобразования
        assert len(result) == 3
        assert result[0] == {"id": "1", "name": "Alice", "amount": "100"}
        assert result[1] == {"id": "2", "name": "Bob", "amount": "200"}
        assert result[2] == {"id": "3", "name": "Charlie", "amount": "300"}


def test_empty_csv_file():
    # Тест с пустым CSV (только заголовки)
    csv_data = "id;name;amount"

    with patch('builtins.open', mock_open(read_data=csv_data)):
        result = csv_to_dict("empty.csv")
        assert result == []

def test_csv_file_not_found() -> None:
    """Тест отсутствующего файла (должен вернуть [])."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = csv_to_dict("nonexistent.csv")
        assert result == []

def test_csv_file_error() -> None:
    """Тест битого файла (должен вернуть [])."""
    with patch("builtins.open", side_effect=csv.Error):
        result = csv_to_dict("corrupted.csv")
        assert result == []
