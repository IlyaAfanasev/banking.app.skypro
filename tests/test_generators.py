import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions, transactions_with_currency_code_usd):
    assert list(filter_by_currency(transactions, "USD")) == transactions_with_currency_code_usd


def test_filter_by_currency_with_empty_list():
    with pytest.raises(StopIteration):
        next(filter_by_currency([], "USD"))


def test_filter_by_currency_code_not_included(transactions):
    with pytest.raises(StopIteration):
        next(filter_by_currency(transactions, "CNY"))


def test_transaction_descriptions(transactions, description_of_transactions):
    assert list(transaction_descriptions(transactions)) == description_of_transactions


def test_transaction_descriptions_with_empty_list(transactions):
    with pytest.raises(StopIteration):
        next(transaction_descriptions([]))


def test_card_number_generator(card_numbers):
    assert list(card_number_generator(1, 5)) == card_numbers


def test_card_number_generator_with_wrong_parameters():
    with pytest.raises(ValueError):
        next(card_number_generator(-1, 6))
        next(card_number_generator(8, 6))
        next(card_number_generator(1_0001_1111_1111_1111, 1_0001_1111_1111_1113))
