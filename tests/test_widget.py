from mailbox import FormatError

import pytest

from src.widget import get_mask_account_card, get_date


@pytest.mark.parametrize("masking_data, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 64686473678894779589", "Счет **9589")
])
def test_get_mask_account_card(masking_data, expected):
    assert get_mask_account_card(masking_data) == expected


def test_get_mask_account_card_with_empty_data():
    with pytest.raises(FormatError):
        get_mask_account_card("")


def test_get_mask_account_card_with_incorrect_number():
    with pytest.raises(FormatError):
        get_mask_account_card("Visa Platinum 70007922896063")


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_with_incorrect_date():
    with pytest.raises(FormatError):
        get_mask_account_card("2024-03-T02:26:18.671407")
