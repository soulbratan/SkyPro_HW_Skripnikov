import csv
from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd
from pandas.errors import EmptyDataError

from src.read_tables import csv_to_dict, excel_to_dicts


# 1, 2, 3, 4) Тесты функции csv_to_dict с помощью заглушек
# 5, 6, 7) Тесты функции excel_to_dicts с помощью заглушек



# 1)
def test_successful_csv() -> Any:
    """Тест нормальной работы."""
    # Подготовка тестовых данных в формате CSV
    csv_data = """id;name;amount
1;Alice;100
2;Bob;200
3;Charlie;300"""
    with patch("builtins.open", mock_open(read_data=csv_data)): # Мокаем open и csv.DictReader
        result = csv_to_dict("dummy_path.csv")
        assert len(result) == 3 # Проверяем корректность преобразования
        assert result[0] == {"id": "1", "name": "Alice", "amount": "100"}
        assert result[1] == {"id": "2", "name": "Bob", "amount": "200"}
        assert result[2] == {"id": "3", "name": "Charlie", "amount": "300"}


# 2)
def test_empty_csv_file() -> Any:
    """Тест пустого файла."""
    csv_data = "id;name;amount"
    with patch("builtins.open", mock_open(read_data=csv_data)):
        result = csv_to_dict("empty.csv")
        assert result == []


# 3)
def test_csv_file_not_found() -> None:
    """Тест отсутствующего файла (должен вернуть [])."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = csv_to_dict("nonexistent.csv")
        assert result == []


# 4)
def test_csv_file_error() -> None:
    """Тест битого файла (должен вернуть [])."""
    with patch("builtins.open", side_effect=csv.Error):
        result = csv_to_dict("corrupted.csv")
        assert result == []


# 5)
def test_successful_read_excel() -> Any:
    """Тест рабочего файла."""
    mock_data = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
    with patch("pandas.read_excel", return_value=mock_data):
        result = excel_to_dicts("dummy.xlsx")
        assert result == [{"A": 1, "B": "x"}, {"A": 2, "B": "y"}]


# 6)
def test_empty_excel_file() -> Any:
    """Тест пустого файла."""
    with patch("pandas.read_excel", side_effect=EmptyDataError("No data")):
        result = excel_to_dicts("empty.xlsx")
        assert result == []


# 7)
@patch("pandas.read_excel")
def test_file_not_found(mock_read_excel: Any) -> Any:
    """Тест несуществующего файла."""
    mock_read_excel.side_effect = FileNotFoundError # Мокируем FileNotFoundError
    result = excel_to_dicts("nonexistent.xlsx")
    assert result == []
    mock_read_excel.assert_called_once_with("nonexistent.xlsx")
