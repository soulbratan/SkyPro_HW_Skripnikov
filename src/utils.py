import json
# from typing import Any


def load_transactions_list(file_name: str) -> list:
    """
    Функция принимает на вход (file_name) путь до JSON-файла и
     возвращает список словарей с данными о финансовых транзакциях.
     Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:  # Обращаемся к файлу по заданному пути
            data = json.load(f)  # Преобразуем JSON-файл в файл Python
            if isinstance(data, list):  # Проверка на соответствие типа данных
                return data  # Если соответствует, возвращаем список словарей
            return []  # В обратном случае возвращаем пустой список
    except (FileNotFoundError, json.JSONDecodeError):  # Если не найден, или не список возвращаем []
        return []


# file_names = "../data/operations.json"
#
# result = load_transactions_list(file_names)
#
# print(result[0])