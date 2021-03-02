from sys import argv
# *(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных
# файлов и имя выходного файла. Проверить работу скрипта.


def csv_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as _file:
        for line in _file:
            yield line


def users_hobby(users, hobby, users_hobby):
    with open(users_hobby, 'w+', encoding='utf-8') as f:  # перезаписываем файл
        for u, h in zip(csv_reader(users), csv_reader(hobby)):
            f.write(f'{u.strip()}: {h.strip()}\n')


if __name__ == '__main__':
    program, users, hobby, result = argv
    users_hobby(users, hobby, result)
# python dz_6_5.py users.csv hobby.csv users_hobby.txt  - проверочная строка
