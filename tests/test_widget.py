import pytest

from src import widget

# Тестируем функцию "mask_account_card":
# 1) С помощью фикстур;
# 2) С помощью параметризации;
# 3) Тест ошибок (большой номер, маленький номер, буквы в номере, пустой).


# 1)
def test_mask_account_1(inf_account_1: str) -> None:
    assert widget.mask_account_card(inf_account_1) == "Счет **4305"


def test_mask_account_2(inf_account_2: str) -> None:
    assert widget.mask_account_card(inf_account_2) == "Maestro 7000 79** **** 6361"


# 2)
@pytest.mark.parametrize(
    "inf_accounts, expected",
    [
        ("Счет 35383033474447895560", "Счет **5560"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_accounts(inf_accounts: str, expected: str) -> None:
    assert widget.mask_account_card(inf_accounts) == expected


# 3)


@pytest.mark.parametrize(
    "wrong_inf_accounts",
    [("Счет 353830334744478955602"), ("Maestro 159683786870519"), ("Счет 353830334744478955ad"), ()],
)
def test_mask_accounts_wrong(wrong_inf_accounts: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        widget.mask_account_card(wrong_inf_accounts)
    assert str(exc_info.value) == "Неккоректный номер счёта или карты"


# Тестируем функцию "get_date":
# 1) С помощью фикстур;
# 2) С помощью параметризации;
# 3) Тест ошибок (заграничные даты, буквы в дате, пустая).


# 1)
def test_get_date_1(date_1: str) -> None:
    assert widget.get_date(date_1) == "11.03.2024"


# 2)
@pytest.mark.parametrize(
    "dates, expected",
    [
        ("2022-12-24T02:26:18.671407", "24.12.2022"),
        ("2014-10-25T02:26:18.671407", "25.10.2014"),
        ("2001-01-01T02:26:18.671407", "01.01.2001"),
    ],
)
def test_get_dates(dates: str, expected: str) -> None:
    assert widget.get_date(dates) == expected


# 3)


@pytest.mark.parametrize(
    "wrong_get_dates",
    [("2022-13-24T02:26:18.671407"), ("2014-10-32T02:26:18.671407"), ("2ac1-01-01T02:26:18.671407"), ()],
)
def test_get_dates_wrong(wrong_get_dates: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        widget.get_date(wrong_get_dates)
    assert str(exc_info.value) == "Некорректная дата"
