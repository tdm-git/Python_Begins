import random

# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
# можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


def get_joke(not_repeat):
    """ функция возвращает случайно сгенерированные шутки по спискам, имеет возможность контроля уникальности """
    if not_repeat and (len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0):
        return ' -/-/-'           # если включен режим уникальности контролируем длину списка, иначе пустая строка
    noun = random.choice(nouns)   # аналог ручного - nouns[random.randint(0, len(nouns) - 1)]
    adverb = random.choice(adverbs)
    adjective = random.choice(adjectives)
    if not_repeat:                # железный контроль уникальности - удаляем слова
        adjectives.remove(adjective)
        nouns.remove(noun)
        adverbs.remove(adverb)
    return f'{noun} {adverb} {adjective}'


def get_jokes(num=1, not_repeat=False):
    global nouns
    global adverbs
    global adjectives                                  # тема областей видимости переменных
    list_word = [nouns[:], adverbs[:], adjectives[:]]  # сохраним их для дальнейшего использования
    list_jokes = []
    for i in range(num):
        list_jokes.append(get_joke(not_repeat))        # очистим список слов, в случае контроля уникальности
    print(list_jokes)
    nouns = list_word[0]                               # восстановим глобальную переменную
    adverbs = list_word[1]
    adjectives = list_word[2]


get_jokes(num=5)                   # демонстрация передачи именнованых аргументов
get_jokes(not_repeat=True, num=5)  # не зависит от порядка передачи
get_jokes(6, True)                 # при превышении размера списка ошибки не будет
get_jokes(4)
