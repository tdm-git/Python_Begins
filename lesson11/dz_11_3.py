# Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
# работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
class NotDigit(Exception):
    def __init__(self, txt):
        self.txt = txt

result = []
while True:
    user_num = input('введите число (0-прервать ввод): ')
    try:
        if not user_num.isdigit():
            raise NotDigit('Некорректный ввод! повторите ввод!')
        user_num = int(user_num)
        if not user_num:
            break
        result.append(user_num)
    except (ValueError, NotDigit) as err:
        print(err)

print(result)
