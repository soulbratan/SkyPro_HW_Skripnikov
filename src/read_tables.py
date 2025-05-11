import csv

import pandas as pd


def csv_to_dict(path_file: str) -> list[dict]:
    """Функция преобразования CSV файла в список словарей"""
    try:
        transactions_list = list()  # Создаём пустой список
        with open(path_file, encoding="UTF-8") as f:  # Открываем файл CSV
            reader = csv.DictReader(f, delimiter=";")  # Преобразуем файл с разделителем ";", в словари
            for row in reader:
                transactions_list.append(row)  # Записываем каждый словарь в список
        return transactions_list
    except (FileNotFoundError, csv.Error):
        return []


def excel_to_dicts(file_path: str) -> list[dict]:
    """Функция преобразования Excel файла в список словарей"""
    try:
        df = pd.read_excel(file_path)  # Читаем Excel файл методом pandas
        return df.to_dict("records")  # Преобразуем в список словарей структурируя (orient='records')
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []


# result = csv_to_dict("../data/transactions.csv")
# result = excel_to_dicts("../data/transactions_excel.xlsx")
# print(result[0])
