import pytest

# Фикстура для теста функции "get_mask_card_number":


@pytest.fixture
def card_number() -> int:
    return 1234567891234567


# Фикстура для теста функции "get_mask_account_number":
@pytest.fixture
def account_number() -> int:
    return 12345345345345254267


# Фикстуры для теста функции "mask_account_card":
@pytest.fixture
def inf_account_1() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def inf_account_2() -> str:
    return "Maestro 7000792289606361"


# Фикстура для теста функции "get_date":
@pytest.fixture
def date_1() -> str:
    return "2024-03-11T02:26:18.671407"


# Фикстура для теста функций "filter_by_state" и "sort_by_date":
@pytest.fixture
def list_1() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_2() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
