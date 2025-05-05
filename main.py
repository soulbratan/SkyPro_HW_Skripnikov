from src import utils
from src import read_tables
from src import processing

def main():
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    choice_1 = input("Ваш выбор: ")
    if choice_1 == "1":
        print("Для обработки выбран JSON-файл.")
        result_1 = utils.load_transactions_list("data/operations.json")
    elif choice_1 == "2":
        print("Для обработки выбран CSV-файл.")
        result_1 = read_tables.csv_to_dict("data/transactions.csv")
    elif choice_1 == "3":
        print("Для обработки выбран XLSX-файл.")
        result_1 = read_tables.excel_to_dicts("data/transactions_excel.xlsx")
    else:
        print("Вы не выбрали ничего из предложенного списка")
        return [{}]
    print("Введите статус, по которому необходимо выполнить фильтрацию. "
          "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    choice_2 = input("Ваш выбор: ").upper()
    print(f"Операции отфильтрованы по статусу {choice_2}")
    result_2 = processing.filter_by_state(result_1, choice_2)
    return result_2


x = main()
print(x)