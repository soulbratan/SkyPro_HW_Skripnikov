import pytest

from src import processing

# Тестируем функцию "filter_by_state":
# 1) С помощью фикстур;
# 2) С помощью параметризации;
# 3) Тест ошибок (неправильное имя фильтра, пустое имя фильтра).


# 1)
def test_filter_by_state_1(list_1: list) -> None:
    assert processing.filter_by_state(list_1) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_2(list_1: list) -> None:
    assert processing.filter_by_state(list_1, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# 2)
@pytest.mark.parametrize(
    "lists, expected",
    [
        (
            [
                {"id": 4142832, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 9397123570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594127, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 61504591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [{"id": 4142832, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        ((), []),
    ],
)
def test_filter_by_states(lists: list, expected: list) -> None:
    assert processing.filter_by_state(lists) == expected


# 3)
def test_filter_by_state_wrong_1() -> None:
    with pytest.raises(ValueError) as exc_info:
        processing.filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCLED",
        )
    assert str(exc_info.value) == "Неправильное имя фильтра"


def test_filter_by_state_wrong_2() -> None:
    with pytest.raises(ValueError) as exc_info:
        processing.filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "",
        )
    assert str(exc_info.value) == "Неправильное имя фильтра"


# Тестируем функцию "sort_by_date":
# 1) С помощью фикстур (прямая и обратная сортировка;
# 2) С помощью параметризации;
# 3) Тест ошибок (заграничные даты, буквы в дате, пустая дата).


# 1)
def test_sort_by_date_1(list_2: list) -> None:
    assert processing.sort_by_date(list_2) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_2(list_2: list) -> None:
    assert processing.sort_by_date(list_2, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# 2)
@pytest.mark.parametrize(
    "lists_2, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2017-05-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2012-04-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2014-03-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2011-02-12T21:27:25.241689"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2017-05-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2014-03-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2012-04-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2011-02-12T21:27:25.241689"},
            ],
        ),
        ((), []),
    ],
)
def test_sort_by_dates(lists_2: list, expected: list) -> None:
    assert processing.sort_by_date(lists_2) == expected


# 3)
def test_sort_by_date_wrong_1() -> None:
    with pytest.raises(ValueError) as exc_info:
        processing.sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": ""},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": ""},
                {"id": 615064591, "state": "CANCELED", "date": ""},
            ]
        )
    assert str(exc_info.value) == "Некорректная дата"


def test_sort_by_date_wrong_2() -> None:
    with pytest.raises(ValueError) as exc_info:
        processing.sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2011-02-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2CA8-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2014-03-32T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2017-13-03T18:35:29.512364"},
            ]
        )
    assert str(exc_info.value) == "Некорректная дата"
