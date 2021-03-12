# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение
# ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?
import re
re_mail = re.compile(r'(^[\w\.\+\-]+)\@([\w]+\.[a-z]{2,4}$)')


def mail_is_valid(name):
    if re_mail.match(name) is None:
        raise ValueError(f'wrong email: {name}')
    else:
        mail_list = re_mail.findall(name)
        return {'username': mail_list[0][0], 'domain': mail_list[0][1]}

print(mail_is_valid('someone@geekbrains.ru'))
print(mail_is_valid('my_m.ail1980@mail.ru'))
print(mail_is_valid('some222one@s2p2k2.com'))
# print(mail_is_valid('someone@geekbrainsru'))  # неверный ввод - демонстрация ValueError

