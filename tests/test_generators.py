import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import card_numbers, transactions, transactions_with_currency_code_usd, \
    transactions_with_currency_code_rub


@pytest.mark.parametrize(
    "transactions, currency_code, expected", [
        (transactions(), "USD", transactions_with_currency_code_usd()),
        (transactions(), "RUB", transactions_with_currency_code_rub())
    ]
)
def test_filter_by_currency(transactions, currency_code, expected):
    assert list(filter_by_currency(transactions, currency_code)) == expected


def test_filter_by_currency_with_empty_list():
    with pytest.raises(StopIteration):
        next(filter_by_currency([], "USD"))


def test_filter_by_currency_code_not_included():
    with pytest.raises(StopIteration):
        next(filter_by_currency(transactions(), "CNY"))


def test_transaction_descriptions(description_of_transactions):
    assert list(transaction_descriptions(transactions())) == description_of_transactions


def test_transaction_descriptions_with_empty_list():
    with pytest.raises(StopIteration):
        next(transaction_descriptions([]))


def test_card_number_generator(card_numbers):
    assert list(card_number_generator(1, 5)) == card_numbers

@pytest.mark.parametrize(
    "start, finish",[
        (-1 ,6),
        (8 ,6),
        (1_0001_1111_1111_1111, 1_0001_1111_1111_1113)
    ]
)
def test_card_number_generator_with_wrong_parameters(start, finish):
    with pytest.raises(ValueError):
        next(card_number_generator(start, finish))
