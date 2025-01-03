from functools import wraps
from typing import Any, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор автоматически логирует начало и конец выполнения функции,
    ее результаты или возникшие ошибки. Декоратор принимает необязательный аргумент filename.
     Если filename задан логи будут записываться в файл, иначе в консоль:
    Пример логирования:
     Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении: my_function ок
     Ожидаемый вывод при ошибке: my_function error: тип ошибки.
      Inputs: (1, 2), {} Где тип ошибки заменяется на текст ошибки."""

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # Вызов оригинальной функции
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"

                # Логирование результата
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

                # Логирование ошибки
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)

                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator
