# Для модуля decorators.
# Напишите декоратор log, который будет автоматически логировать
# начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
# Декоратор должен принимать необязательный аргумент filename,
# который определяет, куда будут записываться логи (в файл или в консоль):
# - Если filename задан, логи записываются в указанный файл.
# - Если filename не задан, логи выводятся в консоль.

# Логирование должно включать:
# - Имя функции и результат выполнения при успешной операции.
# - Имя функции, тип возникшей ошибки и входные параметры,
# если выполнение функции привело к ошибке.

from datetime import datetime
from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор для логирования выполнения функции в консоль или в файл(опция)"""
    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Записываем информацию о вызове функции
            func_name = func.__name__
            inputs = f"Inputs: {args}, {kwargs}"
            # Формируем сообщение о начале выполнения функции
            start_time = datetime.now()
            start_msg = f"{start_time} - {func_name} started. {inputs}"
            print(start_msg)
            # Выполняем функцию
            result = func(*args, **kwargs)
            end_time = datetime.now()
            time_execution = end_time - start_time
            # Формируем сообщение об успешном выполнения функции
            success_msg = f"{end_time} - {func_name} OK. Result: {result}. Time execution: {time_execution}"
            print(success_msg)

        return wrapper

    return decorator


@log()
def my_function(x: Any, y: Any) -> Any:
    """Функция проверки декоратора"""
    return x / y


# my_function(1, 2)