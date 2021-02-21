from requests import get, utils


def sub_str(str_in, teg_name):  # выносим повторяющийся код в функцию, для читабельности разбил на три строки
    before = str_in.find('<' + teg_name + '>') + len(teg_name) + 2
    after = str_in.find('</' + teg_name + '>')
    return str_in[before:after]


def currency_rates(*args):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    response.close()
    list_val = content.split("<Valute ID=")
    dict_val = {}
    for i in list_val[1:]:  # первая строка служебная, начинаем со второй
        # для демонстрации что курс это число округлим значение валюты до 2-х знаков, от изначальных 4-х
        # Decimal имеет смысл использовать для упрощения расчетов и пр., но т.к. это учебный пример и мы сумму
        # используем только один раз то вполне можно использовать float и не утяжелять код дополнительным модулем
        dict_val[sub_str(i, 'CharCode')] = f"{sub_str(i, 'Name')},{float(sub_str(i, 'Value').replace(',', '.')):.2f}"
    # print(dict_val)
    result = []
    for i in args:  # переписал на args т.к. каждый вызов приводит к обращению на сайт, чтобы уменьшить кол-во обращений
        result.append(dict_val.get(i))
    return result


print(*currency_rates('USD'))         # работает как единичный так и множественный вызов
print(*currency_rates('EUR'))
print(*currency_rates('USD', 'EUR'))
print(*currency_rates('YYY'))         # несуществующая выводит None
