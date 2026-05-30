import re
from mailbox import FormatError

import masks


def get_mask_account_card(account_info: str) -> str:
    """Функция принимает строку, в которой передается информация о типе данных(счет/карта) и номере данных,
    определяет тип данных и использует фунции для маскировки номера соответствуе типу данных"""

    number_info = ""

    # выводим номер карты в переменную
    match = re.search(r"[0-9]+", account_info)

    # проверка на совпадение поиска
    if match:
        number_info = match.group()

    # определяем к какому типу данных относится номер по длине строки и возвращаем маску номера
    try:
        if len(number_info) == 16:
            return masks.get_mask_card_number(number_info)

        elif len(number_info) == 20:
            return masks.get_mask_account(number_info)
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
