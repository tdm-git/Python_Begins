# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
import os
from shutil import copytree


def copy_dir():
    source_dir = 'my_project'  # каталог откуда копируем
    dir_name = 'templates'     # имя искомой папки которую копируем

    for root, dirs, files in os.walk(source_dir):
        if root.find(dir_name) > 0 and len(files) == 0:  # нужна строка с родительской директорией и нужным названием
            copytree(os.path.join(root), dir_name, dirs_exist_ok=True)    # еще один метод из библиотеки копирующий каталог

if __name__ == '__main__':
    copy_dir()
