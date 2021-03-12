# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
# @type_logger
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
from functools import wraps


def type_logger(func):
    print(func)

    @wraps(func)  # маскируем работу декоратора
    def _logger(**kwargs):
        result = [f'{func.__name__}({i}:{type(i)}),' for i in kwargs.values()]  # выводим имя функции и тип параметров
        print(*result)
    return _logger


@type_logger
def calc_cube(**kwargs):
    return kwargs['x'] ** 3


a = calc_cube(x=5, y=3.3, z='11')  # решим вариант для именнованых параметров
