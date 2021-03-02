from sys import argv
# *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи
# и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.


def update_sales(line_num, sales):
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        for i in range(int(line_num)-1):  # пролистываем нужное кол-во строк
            f.readline()
        f.seek(f.tell())  # переносим указатель в нужную позицию
        f.write(sales)    # работает только для случаев с такой же длиной

if __name__ == '__main__':
    program, line_num, sales = argv
    update_sales(line_num, sales)


