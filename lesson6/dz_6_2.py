# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.
def parser_string(str_in):
    if str_in.find(' - - ') > 0:  # контролируем что есть требуемая подстрока
        address = str_in.split(' - - ')[0]
    else:
        address = ''
    return address  # по условиям задачи достаточно только адреса


def csv_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            yield line


dict_result = {}  # соберём результат в словарь где посчитаем количество обращений по адресам  {ip:sum}
log_file = csv_reader('nginx_logs.txt')
for file_line in log_file:
    addr = parser_string(file_line)
    if dict_result.get(addr):
        dict_result[addr] += 1
    else:
        dict_result[addr] = 1

max_num = 0  # найдем элемент с максимумом вызовов
spammer = ''
for i, j in dict_result.items():
    if j > max_num:
        max_num = j
        spammer = i
print(f' максимальное число запросов: {max_num} поступило от пользоватлея по адресу - {spammer}')

