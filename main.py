from src import utils
from src import read_tables

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
        result_1 = utils.load_transactions_list("data/operations.json")
        return result_1
    elif choice_1 == "2":
        result_2 = read_tables.csv_to_dict("data/transactions.csv")
        return result_2
    elif choice_1 == "3":
        result_3 = read_tables.excel_to_dicts("data/transactions_excel.xlsx")
        return result_3
    else:
        return "Вы не выбрали ничего из предложенного списка"

x = main()
print(x[0])