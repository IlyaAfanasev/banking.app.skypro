import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_with_letter_data():
    with pytest.raises(ValueError):
        get_mask_card_number("Visa 1596837868705199")


def test_get_mask_card_number_with_incorrect_length():
    with pytest.raises(ValueError):
        get_mask_card_number("15968378687051")

    with pytest.raises(ValueError):
        get_mask_card_number(15968378687051)


@pytest.mark.parametrize(
    "account, expected",
    [
        ("15968378687025785199", "**5199"),
        ("71583007347256896758", "**6758"),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


def test_get_mask_account_with_letter_data():
    with pytest.raises(ValueError):
        get_mask_account("Счет 15968378687025765199")


def test_get_mask_account_with_incorrect_length():
    with pytest.raises(ValueError):
        get_mask_account("968378687025765199")

    with pytest.raises(ValueError):
        get_mask_account(1596837868702576519)
