import csv


def csv_to_dict(path_file: str) -> list[dict]:
    """Функция преобразования CSV файла в список словарей"""
    try:
        transactions_list = list()  # Создаём пустой список
        with open(path_file, encoding="UTF-8") as f:  # Открываем файл CSV
            reader = csv.DictReader(f, delimiter=";")  # Преобразуем файл с разделителем ";", в словари
            for row in reader:
                transactions_list.append(row)  # Записываем каждый словарь в список
        return transactions_list
    except FileNotFoundError:
        return []

# result = csv_to_dict("../data/transactions.csv")
# print(result[0])