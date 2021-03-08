# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а значения
# кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
import os
import json
import django


def dir_info():
    root_dir = django.__path__[0]  # используем библиотеку django
    django_files = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))  # размер как ключ
            ext = file.rsplit('.', maxsplit=1)[-1].lower()                    # расширение файла
            if size in django_files:
                django_files[size][0] += 1            # суммируем количество
                if ext not in django_files[size][1]:  # если расширение не найдено то давляем в список
                    django_files[size][1].append(ext)
            else:
                django_files[size] = [1, [ext]]
    result = {}
    for size, list_log in sorted(django_files.items()):  # сортируем и переписываем список в кортеж
        result[size] = tuple(list_log)
        print(f'{size}: {tuple(list_log)}')
    folder_name = os.path.dirname(__file__).split('\\')[-1] + '_summary.json'  # получаем имя папки
    with open(folder_name, 'w', encoding='utf-8') as f:  # Сохраняем словарь в файл
        json.dump(result, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    dir_info()
