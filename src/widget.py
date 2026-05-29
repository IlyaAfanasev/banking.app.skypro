import re
from mailbox import FormatError

import masks


def get_mask_account_card(account_info: str) -> str:
    """Функция принимает строку, в которой передается информация о типе данных(счет/карта) и номере данных,
    определяет тип данных и использует фунции для маскировки номера соответствуе типу данных"""

    # выводим номер карты в переменную
    number_info = re.search(r"[0-9]?", account_info).group()

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