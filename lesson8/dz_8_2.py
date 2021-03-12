# Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt для получения
# информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,<response_size>)
# ,например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?
import re
RE_NAME = re.compile(r'([\w\.\+\:\/]+)')


def parcer_log(str_line):
    log_list = RE_NAME.findall(str_line)  # разбиваем на блоки по шаблону,т.к. findall возвращает список
    print((log_list[0], log_list[1]+log_list[2], log_list[3], log_list[4], log_list[6], log_list[7]))


def csv_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            yield line


log_file = csv_reader('nginx_logs.txt')
for file_line in log_file:
    parcer_log(file_line)


