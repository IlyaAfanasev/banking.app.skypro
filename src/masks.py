def get_mask_card_number(card_number: int | str) -> str:
    """Функци, возвращает маску номера карты"""

    # преобразовываем преременную в список из строки символов
    list_card_number = list(str(card_number))
    correct_card_number = []
    # шаблон маски
    mask_template = "---- --** **** ----"
    # старт среза для преобразования номеры карты
    start = 0

    # добавление пробелов в список цифр номера карты
    while True:
        correct_card_number += list_card_number[start : start + 4]
        start += 4
        if start >= len(list_card_number) - 1:
            break
        correct_card_number.append(" ")

    # возвращаем маску, преобразовывая ее из списка, который получается путем замещения цифр
    # в номере карты звоздочками из шаблона маски при одновременной итерации номера карты и шаблона
    return "".join(
        "*" if mask_char == "*" else card_char for mask_char, card_char in zip(mask_template, correct_card_number)
    )


def get_mask_account(account: int | str) -> str:
    """Функция, возвращает маску номера банковского счета"""

    # возвращаем маску номера банковского счета, которая получается путем конкатенации звездочек
    # и среза номера банковского счета
    return "**" + str(account)[-4:]
