# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.
class NotNull(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(a, b):
    try:
        if b == 0:
            raise NotNull('некорретный ввод делителя !')
    except NotNull as err:
        print(err)
        return 'is Infinite!'
    else:
        print(f'Результат деления числа {a} на число {b} :')
        return a / b


print(div(5, 1))
print(div(5, 0))
