from typing import Any

from src import generators, processing, read_tables, utils, widget


def main() -> Any:
    """Функция основной логики проекта, которая связывает функциональности между собой. Реализует выборку транзакций"""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    choice_1 = input("Ваш выбор: ")  # Выбираем откуда взять информацию о транзакциях
    if choice_1 == "1":
        print("Для обработки выбран JSON-файл.")
        result_1 = utils.load_transactions_list("data/operations.json")  # Транзакции из JSON-файла
    elif choice_1 == "2":
        print("Для обработки выбран CSV-файл.")
        result_1 = read_tables.csv_to_dict("data/transactions.csv")  # Транзакции из CSV-файла
    elif choice_1 == "3":
        print("Для обработки выбран XLSX-файл.")
        result_1 = read_tables.excel_to_dicts("data/transactions_excel.xlsx")  # Транзакции из XLSX-файла
    else:
        print("Вы не выбрали ничего из предложенного списка")
        return [{}]  # Пустые данные
    correct = 0  # Для цикла while
    result_2 = None
    while correct == 0:  # Запускаем цикл, пока пользователь не выберет правильно
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        choice_2 = input("Ваш выбор: ").upper()  # Приводим ввод пользователя в верхний регистр
        if choice_2 == "EXECUTED" or choice_2 == "CANCELED" or choice_2 == "PENDING":  # Сравниваем ответ
            print(f"Операции отфильтрованы по статусу {choice_2}")
            result_2 = processing.filter_by_state(result_1, choice_2)  # Фильтруем по статусу
            correct = 1  # Для выхода из цикла
        else:
            print(f"Статус операции {choice_2} недоступен.")  # Если некорректный ввод, то заново
    print("Отсортировать операции по дате? Да/Нет")
    choice_3 = input("Ваш выбор: ").lower()
    result_3 = None
    if choice_3 == "да":
        print("Отсортировать 'по возрастанию' или 'по убыванию'?")
        choice_31 = input("Ваш выбор: ").lower()
        if choice_31 == "по возрастанию":  # Сортируем по дате, по возрастанию
            result_3 = processing.sort_by_date(result_2, False)  # Сортируем по возрастанию
        elif choice_31 == "по убыванию":  # Сортируем по дате, по убыванию
            result_3 = processing.sort_by_date(result_2)  # Сортируем по убыванию
    else:
        result_3 = result_2  # Если 'нет', то идём дальше без сортировки
    print("Выводить только рублевые транзакции? Да/Нет")
    choice_4 = input("Ваш выбор: ").lower()
    result_4: Any = None
    if choice_4 == "да":
        result_4 = [i for i in generators.filter_by_currency(result_3, "RUB")]  # Фильтр по рублёвой валюте
    else:
        result_4 = result_3  # Без фильтрации по валюте
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    choice_5 = input("Ваш выбор: ").lower()
    if choice_5 == "да":
        choice_51 = input("Введите слово: ")
        result_5 = processing.search_transactions(result_4, choice_51)  # Фильтруем по слову
    else:
        result_5 = result_4  # Если нет, то идём дальше
    print("Распечатываю итоговый список транзакций...\n")
    if len(result_5) == 0:  # Если ничего не найдено, печатаем
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(result_5)}\n")
        for i in result_5:  # Печатаем операции
            first_line = f"{widget.get_date(i['date'])} {i.get('description')}\n"  # Первая строчка (дата и описание)
            if i["description"].lower() == "открытие вклада":  # Если открытие вклада, то...
                second_line = f"{widget.mask_account_card(i.get('to'))}\n"  # Вторая строчка (куда)
            else:
                second_line = (
                    f"{widget.mask_account_card(i.get('from', "Новый"))} "
                    f"-> {widget.mask_account_card(i.get('to'))}\n"
                )  # Вторая строчка (откуда и куда)
            try:
                third_line = (
                    f"Сумма: {i['operationAmount'].get('amount')} "
                    f"{i['operationAmount'].get('currency').get('name')}\n"
                )  # Проверка ключа в зависимости от вида транзакции (JSON, CSV, XLSX)
            except KeyError:
                third_line = f"Сумма: {i.get('amount')} {i.get('currency_name')}\n"
            print(f"{first_line}{second_line}{third_line}")
    return result_5


x = main()