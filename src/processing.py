from typing import List


def filter_by_state(banking_operations: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """Функция принимает список словарей банковских операций и опционально значение state
    по которому будет производиться фильтрация"""

    return [operation for operation in banking_operations if operation["state"] == state]


def sort_by_date(banking_operations: List[dict], reverse: bool = True) -> List[dict]:
    """Функция принимает список словарей банковских операций и опционально булево значение reverse,
     сортирует список по дате и реверс по значению rev, по умолчанию False"""

    return sorted(banking_operations, key=lambda x: x["date"], reverse=reverse)
