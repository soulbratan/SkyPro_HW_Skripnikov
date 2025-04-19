# Тесты для модуля decorators.
# Тестирование декоратора 'log':
import os
from typing import Any

import pytest

from src.decorators import log


# 1) Тестируем вывод в консоль логов (входные параметры декорируемой функции (1, 2)).
def test_log_decorator_1(capsys: Any) -> Any:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    my_function(1, 2)  # Вызываем функцию
    captured = capsys.readouterr()  # Перехватываем вывод в консоль
    assert "- my_function started. Inputs: (1, 2), {}" in captured.out
    assert "- my_function OK. Result: 0.5. Time execution:" in captured.out


# 2) Тестируем вывод в консоль логов (входные параметры декорируемой функции (20, 20)).
def test_log_decorator_2(capsys: Any) -> Any:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    my_function(20, 20)
    captured = capsys.readouterr()
    assert "- my_function started. Inputs: (20, 20), {}" in captured.out
    assert "- my_function OK. Result: 1.0. Time execution:" in captured.out


# 3) Тестируем вывод в консоль метаданных декорируемой функции.
def test_log_decorator_help(capsys: Any) -> Any:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        """Функция проверки декоратора"""
        return x / y

    help(my_function)
    captured = capsys.readouterr()
    assert "Функция проверки декоратора" in captured.out


# 4) Тестируем вывод в консоль логов об ошибке 'ZeroDivisionError'(входные параметры декорируемой функции (1, 0)).
def test_log_decorator_error_ZeroDiv(capsys: Any) -> Any:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    with pytest.raises(ZeroDivisionError, match="division by zero"):
        my_function(1, 0)
        captured = capsys.readouterr()
        assert "- my_function error: ZeroDivisionError: division by zero. Inputs: (1, 0), {}." in captured.out


# 5) Тестируем вывод в консоль логов об ошибке 'TypeError'(входные параметры декорируемой функции (1, )).
def test_log_decorator_error_type(capsys: Any) -> Any:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    with pytest.raises(TypeError):
        my_function(
            1,
        )
        captured = capsys.readouterr()
        assert "my_function() missing 1 required positional argument: 'y'" in captured.out


# 6) Тестируем вывод в файл (.txt) логов (входные параметры декорируемой функции (1, 2)).
def test_file_logging_1() -> Any:
    test_file = "tests/test_file.txt"  # Прописываем создаваемый файл и его путь
    if os.path.exists(test_file):  # Проверяем существование такого файла
        os.remove(test_file)  # Если есть, удаляем, чтобы создался заново (т.к. в декораторе режим добавления 'a')

    @log(filename=test_file)  # Определяем функцию с файлом внутри теста.
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    my_function(1, 2)
    with open(test_file, "r") as file:  # Открываем файл в режиме чтения
        content = file.read()  # Сохраняем данные из файла в переменную
    assert "- my_function started. Inputs: (1, 2), {}" in content  # Сравниваем содержимое с ожиданием
    assert "- my_function OK. Result: 0.5. Time execution:" in content
    os.remove(test_file)  # Удаляем тестовый файл после использования


# 7) Тестируем вывод в файл (.txt) логов (входные параметры декорируемой функции (20, 20)).
def test_file_logging_2() -> Any:
    test_file = "tests/test_file.txt"
    if os.path.exists(test_file):
        os.remove(test_file)

    @log(filename=test_file)
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    my_function(20, 20)
    with open(test_file, "r") as file:
        content = file.read()
    assert "- my_function started. Inputs: (20, 20), {}" in content
    assert "- my_function OK. Result: 1.0. Time execution:" in content
    os.remove(test_file)


# 8) Тестируем вывод в файл (.txt) логов об ошибке 'ZeroDivisionError'(входные параметры декорируемой функции (1, 0)).
def test_file_logging_error_ZeroDiv() -> Any:
    test_file = "tests/test_file_error.txt"
    if os.path.exists(test_file):
        os.remove(test_file)

    @log(filename=test_file)
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    with pytest.raises(ZeroDivisionError, match="division by zero"):
        my_function(1, 0)
        with open(test_file, "r") as file:
            content = file.read()
        assert "- my_function error: ZeroDivisionError: division by zero. Inputs: (1, 0), {}." in content
    os.remove(test_file)


# 9) Тестируем вывод в (.txt) логов об ошибке 'TypeError'(входные параметры декорируемой функции (1, )).
def test_file_logging_error_type() -> Any:
    test_file = "tests/test_file_error.txt"
    if os.path.exists(test_file):
        os.remove(test_file)

    @log(filename=test_file)
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    with pytest.raises(TypeError):
        my_function(
            1,
        )
        with open(test_file, "r") as file:
            content = file.read()
        assert 'my_function() missing 1 required positional argument: "y"' in content
    os.remove(test_file)
