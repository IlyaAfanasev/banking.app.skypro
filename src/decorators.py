from functools import wraps


def log(filename=None):
    """Декоратор для логирования результата выполнения функции: ок/ Ошибка: текст ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_text = ""
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_text = f"{type(e).__name__}: {e}. Inputs: {args}, {kwargs}"
            else:
                log_text = "ok"
                return result
            finally:
                message = f"{func.__name__} {log_text}\n"
                if filename:
                    with open(f"../{filename}", "w", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message)

        return wrapper
