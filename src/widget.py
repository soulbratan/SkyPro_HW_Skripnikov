from src import masks  # import get_mask_card_number and get_mask_account


def mask_account_card(inf_account: str) -> str:
    """Функция обработки информации о картах и счетах"""
    inf_account_number: str = ""
    inf_account_text: str = ""
    for item in inf_account:  # Перебираем входную информацию и разделяем название и номер
        if item.isdigit():
            inf_account_number += item
        elif item.isalpha():
            inf_account_text += item
    if len(inf_account_number) == 16:  # Проверка соответствия длины номера карты
        inf_account_number = masks.get_mask_card_number(inf_account_number)
    elif len(inf_account_number) == 20:  # Проверка соответствия длины номера счёта
        inf_account_number = masks.get_mask_account(inf_account_number)
    else:
        raise ValueError("Неккоректный номер счёта или карты")
    mask_inf = inf_account_text + " " + inf_account_number  # Сборка названия и маскированного номера счёта или карты
    return mask_inf


def get_date(input_date: str) -> str:
    """Функция преобразования даты к привычному формату"""
    if len(input_date) < 1 or int(input_date[8:10]) > 31 or int(input_date[5:7]) > 12 or not input_date[0:4].isdigit():
        raise ValueError("Некорректная дата")
    new_date: str = ""
    new_date = input_date[8:10] + "." + input_date[5:7] + "." + input_date[0:4]
    return new_date
