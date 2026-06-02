import re
from mailbox import FormatError

import masks


def get_mask_account_card(masking_data: str) -> str:
    """Функция принимает строку, в которой передается информация о типе данных(счет/карта) и номере данных,
    определяет тип данных и использует фунции для маскировки номера соответствуе типу данных"""

    name = ""
    number_info = ""

    # выводим номер карты и именование переданных данных в переменные
    match = re.search(r"([a-zA-Zа-яА-Я\s]+)([0-9]+)", masking_data)

    # проверка на совпадение поиска
    if match:
        name = match.group(1)
        number_info = match.group(2)

    # определяем к какому типу данных относится номер по длине строки и возвращаем маску номера
    try:
        if len(number_info) == 16:
            return f"{name}{masks.get_mask_card_number(number_info)}"

        elif len(number_info) == 20:
            return f"{name}{masks.get_mask_account(number_info)}"

        else:
            raise FormatError()

    except FormatError:
        return "Неправильный формат данных"


def get_date(unformatted_date: str) -> str:
    """Функция принимает дату в формате: "2024-03-11T02:26:18.671407",
    возвращает в формате: "ДД.ММ.ГГГГ"."""

    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", unformatted_date)
    format_date = f"{match.group(3)}.{match.group(2)}.{match.group(1)}"

    return format_date
