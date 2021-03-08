# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
import os


def make_dir():
    path_list = [('my_project', 'settings'), ('my_project', 'mainapp'),
                 ('my_project', 'adminapp'), ('my_project', 'authapp')]
    for path in path_list:
        dir_path = os.path.join(*path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

if __name__ == '__main__':
    make_dir()