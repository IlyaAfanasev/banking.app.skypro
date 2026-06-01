from typing import List


def filter_by_state(banking_operations: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """Функция принимает список словарей банковских операций и опционально значение state
    по которому будет производиться фильтрация"""

    return [i for i in banking_operations if i["state"] == state]


def sort_by_date(banking_operations: List[dict], rev: bool = False) -> List[dict]:
    """Функция принимает список словарей банковских операций и опционально булево значение rev,
     сортирует список по дате и реверс по значению rev, по умолчанию False"""

    return sorted(banking_operations, key=lambda x: x["date"], reverse=rev)

