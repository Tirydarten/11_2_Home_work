from src.decorators import log


# Ожидаемый вывод в лог-файл `mylog.txt`
# при успешном выполнении: (закомментируйте/раскомментируйте следующую строку для тестирования)
# @log(filename="mylog.txt")
# def my_function(x, y):
#     """Функция сложения двух чисел"""
#     return x + y


# Ожидаемый вывод в консоль "filename=None" или "()"
# при успешном выполнении: (закомментируйте/раскомментируйте следующую строку для тестирования)
@log(filename=None)
# @log()
def my_function(x: int, y: int) -> int:
    """Функция сложения двух чисел"""
    return x + y


# Успешный вызов функции: (закомментируйте/раскомментируйте следующую строку для тестирования)
# result = my_function(1, 2)


# Вызов с ошибкой (закомментируйте/раскомментируйте следующую строку для тестирования)
try:
    result = my_function(1, "a")  # Это вызовет ошибку TypeError

except TypeError as e:

    print(f"Caught an exception: {e}")

help(my_function)
