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