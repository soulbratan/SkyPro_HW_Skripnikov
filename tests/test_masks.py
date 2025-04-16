from typing import Union

import pytest

from src import masks

# Тестируем функцию "get_mask_card_numbers":
# 1) С помощью фикстуры;
# 2) С помощью параметризации;
# 3) Тест ошибок (большой номер, маленький номер, буквы в номере, пустой).


# 1)
def test_get_mask_card_number(card_number: Union[str, int]) -> None:
    assert masks.get_mask_card_number(card_number) == "1234 56** **** 4567"


# 2)
@pytest.mark.parametrize(
    "card_numb, expected",
    [
        ("5332 5332 1234 1234", "5332 53** **** 1234"),
        ("5243 5243 5678 5678", "5243 52** **** 5678"),
        ("5154 5154 9876 9876", "5154 51** **** 9876"),
    ],
)
def test_get_mask_card_numbers(card_numb: Union[str, int], expected: str) -> None:
    assert masks.get_mask_card_number(card_numb) == expected


# 3)
@pytest.mark.parametrize("wrong_number", [("5243 5243 5678 56781"), ("5332 5332 1234"), ("5154 5154 ascs 9876"), ()])
def test_get_mask_card_number_wrong(wrong_number: Union[str, int]) -> None:
    with pytest.raises(ValueError) as exc_info:
        masks.get_mask_card_number(wrong_number)
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр"


# Тестируем функцию "get_mask_card_account":
# 1) С помощью фикстуры;
# 2) С помощью параметризации;
# 3) Тест ошибок (большой номер, маленький номер, буквы в номере, пустой).


# 1)
def test_get_mask_account(account_number: Union[str, int]) -> None:
    assert masks.get_mask_account(account_number) == "**4267"


# 2)
@pytest.mark.parametrize(
    "account_numbers, expected",
    [("12345345345345255321", "**5321"), ("98765432112345678945", "**8945"), ("11111111111111111111", "**1111")],
)
def test_get_mask_accounts(account_numbers: Union[str, int], expected: str) -> None:
    assert masks.get_mask_account(account_numbers) == expected


# 3)
@pytest.mark.parametrize(
    "wrong_account", [("123453453453452553213"), ("9876543211234567894"), ("1111111111avds111111"), ()]
)
def test_get_mask_account_wrong(wrong_account: Union[str, int]) -> None:
    with pytest.raises(ValueError) as exc_info:
        masks.get_mask_account(wrong_account)
    assert str(exc_info.value) == "Номер карты должен содержать 20 цифр"
