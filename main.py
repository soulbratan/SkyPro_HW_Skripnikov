from src import utils
from src import read_tables
from src import processing
from src import generators

def main():
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    choice_1 = input("Ваш выбор: ") # Выбираем откуда взять информацию о транзакциях
    if choice_1 == "1":
        print("Для обработки выбран JSON-файл.")
        result_1 = utils.load_transactions_list("data/operations.json") # Транзакции из JSON-файла
    elif choice_1 == "2":
        print("Для обработки выбран CSV-файл.")
        result_1 = read_tables.csv_to_dict("data/transactions.csv") # Транзакции из CSV-файла
    elif choice_1 == "3":
        print("Для обработки выбран XLSX-файл.")
        result_1 = read_tables.excel_to_dicts("data/transactions_excel.xlsx") # Транзакции из XLSX-файла
    else:
        print("Вы не выбрали ничего из предложенного списка")
        return [{}] # Пустые данные
    correct = 0 # Для цикла while
    while correct == 0: # Запускаем цикл, пока пользователь не выберет правильно
        print("Введите статус, по которому необходимо выполнить фильтрацию. "
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        choice_2 = input("Ваш выбор: ").upper()
        if choice_2 == "EXECUTED" or choice_2 == "CANCELED" or choice_2 == "PENDING":
            print(f"Операции отфильтрованы по статусу {choice_2}")
            result_2 = processing.filter_by_state(result_1, choice_2) # Фильтруем по статусу
            correct = 1
        else:
            print(f"Статус операции {choice_2} недоступен.") # Если некорректный ввод, то заново
    print("Отсортировать операции по дате? Да/Нет")
    choice_3 = input("Ваш выбор: ").lower()
    if choice_3 == "да":
        print("Отсортировать 'по возрастанию' или 'по убыванию'?")
        choice_31 = input("Ваш выбор: ").lower()
        if choice_31 == "по возрастанию":
            result_3 = processing.sort_by_date(result_2, False) # Сортируем по возрастанию
        elif choice_31 == "по убыванию":
            result_3 = processing.sort_by_date(result_2) # Сортируем по убыванию
    else:
        result_3 = result_2
    print("Выводить только рублевые транзакции? Да/Нет")
    choice_4 = input("Ваш выбор: ").lower()
    if choice_4 == "да":
        result_4 = [i for i in generators.filter_by_currency(result_3, "RUB")] # Фильтруем по рублёвой валюте
    else:
        result_4 = result_3
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    choice_5 = input("Ваш выбор: ").lower()
    if choice_5 == "да":
        choice_51 = input("Введите слово: ")
        result_5 = processing.search_transactions(result_4, choice_51)
    else:
        result_5 = result_4
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(result_5)}")
    return result_5

x = main()
print(x)

