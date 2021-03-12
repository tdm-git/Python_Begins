# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?
from functools import wraps


def val_checker(check_func):
    def new_calc(func):
        @wraps(func)  # маскируем работу декоратора
        def check_val(x):
            if check_func(x):
                return func(x)
            else:
                raise ValueError(f'wrong val: {x}')
        return check_val
    return new_calc


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
print(a)  # вернет - 125
# a = calc_cube(-5)
# print(a)  # вернет - ValueError: wrong val: -5
