from typing import Callable, TypeVar, Optional, Any
from functools import wraps


def log(filename: Optional[str] = None) -> Any:
    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # Вызов оригинальной функции
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"

                # Логирование результата
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)

                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

                # Логирование ошибки
                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_message + '\n')
                else:
                    print(error_message)

                raise  # Пробрасываем исключение дальше

        return wrapper
    return decorator
