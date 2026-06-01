from typing import List


def filter_by_state(banking_operations: List[dict], state: str='EXECUTED') -> List[dict]:
    """Функция принимает список словарей банковских операций и опционально значение state
    по которому будет производиться фильтрация"""

    return [i for i in banking_operations if i["state"]==state]


