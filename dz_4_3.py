from requests import get, utils
import datetime


def sub_str(str_in, teg_name):
    before = str_in.find('<' + teg_name + '>') + len(teg_name) + 2
    after = str_in.find('</' + teg_name + '>')
    return str(str_in[before:after])


def currency_rates(*args):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    response.close()
    list_val = content.split("<Valute ID=")
    str_data = list_val[0].split('Date="')[1][:10]     # работаем с датой - первая строка начиная с метки 10 символов
    # print(str_data[6:], str_data[3:5], str_data[:2])  # используя datetime формируем дату
    server_date = datetime.date(int(str_data[6:]), int(str_data[3:5]), int(str_data[:2]))  # год, месяц, число
    dict_val = {}
    for i in list_val[1:]:
        kurs = float(sub_str(i, 'Value').replace(',', '.'))
        dict_val[sub_str(i, 'CharCode')] = f"{sub_str(i, 'Name')},{kurs:.2f},{server_date}"
    result = []
    for i in args:
        result.append(dict_val.get(i))
    return result


print(currency_rates('USD', 'EUR', 'GBP', 'CNY'))
