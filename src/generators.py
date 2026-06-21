from typing import Generator, Iterable


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterable:
    """Функция принимает список словарей с транзакциями и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    return (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency_code)


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, finish: int) -> Generator:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров."""

    if start > finish:
        raise ValueError

    for number in range(start, finish + 1):
        str_number = str(number).zfill(16)

        if number > 9999_9999_9999_9999 or number < 0:
            raise ValueError

        yield f"{str_number[:4]} {str_number[4:8]} {str_number[8:12]} {str_number[12:]}"
