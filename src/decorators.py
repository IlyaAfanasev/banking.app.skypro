from functools import wraps
from typing import Callable, TypeVar, ParamSpec, Optional

P = ParamSpec("P")
T = TypeVar("T")


def log(filename: Optional[str] = None) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Декоратор для логирования результата выполнения функции: ок/ Ошибка: текст ошибки"""

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            log_text = ""
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_text = f"{type(e).__name__}: {e}. Inputs: {args}, {kwargs}"
                raise
            else:
                log_text = "ok"
                return result
            finally:
                message = f"{func.__name__} {log_text}"
                if filename:
                    with open(f"../{filename}", "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)

        return wrapper

    return decorator
