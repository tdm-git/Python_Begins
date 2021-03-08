# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер
# которых не превышает этой границы, но больше предыдущей (начинаем с 0)
import os
from collections import defaultdict
import django


def dir_info():
    root_dir = django.__path__[0]    # используем файловую структуру библиотеки django
    django_files = defaultdict(int)  # используем помошник создания справочника
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))  # длина числа в 10-ой системе его размер
            django_files[size] += 1                                           # суммируем количество

    for size, nums in sorted(django_files.items()):  # выводим в отсортированном порядке
        print(f'{size}: {nums}')

if __name__ == '__main__':
    dir_info()
