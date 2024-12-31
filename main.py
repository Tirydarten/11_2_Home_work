from src.decorators import log

# Ожидаемый вывод в лог-файл `mylog.txt`
# при успешном выполнении: (раскомментируйте следующую строку для тестирования)
# @log(filename="mylog.txt")


# Ожидаемый вывод в консоль "filename=None"
# при успешном выполнении: (раскомментируйте следующую строку для тестирования)
@log(filename=None)
# @log()


def my_function(x, y):
    """Функция сложения двух чисел"""
    return x + y

# Успешный вызов функции: (раскомментируйте следующую строку для тестирования)
# result = my_function(1, 2)

# Вызов с ошибкой (раскомментируйте следующую строку для тестирования)
try: result = my_function(1, 'a')  # Это вызовет ошибку TypeError

except TypeError as e:
    print(f"Caught an exception: {e}")

help(my_function)