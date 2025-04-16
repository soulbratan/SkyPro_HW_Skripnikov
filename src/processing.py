# Новый модуль для функций обработки данных


def filter_by_state(unfiltered_list: list, filtering_state: str = "EXECUTED") -> list:
    """Функция фильтрующая входящий список по ключу "state". По умолчанию ключ равен "EXECUTED"."""
    if filtering_state != "EXECUTED" and filtering_state != "CANCELED":
        raise ValueError("Неправильное имя фильтра")
    return [
        i for i in unfiltered_list if i["state"] == filtering_state
    ]  # Возвращаем отфильтрованный по ключу 'state' список с помощью list comprehension


def sort_by_date(unsorted_list: list, reverse: bool = True) -> list:
    """Функция сортирует список словарей по дате. По умолчанию сортировка по убыванию."""
    for i in unsorted_list:
        if len(i["date"]) < 1 or int(i["date"][8:10]) > 31 or int(i["date"][5:7]) > 12 or not i["date"][0:4].isdigit():
            raise ValueError("Некорректная дата")
    return sorted(
        unsorted_list, key=lambda x: x["date"], reverse=reverse
    )  # Возвращаем отсортированный по дате список с помощью sorted


test_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
