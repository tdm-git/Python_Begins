# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы - результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

rus_words = {
    'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семь', 'eighth': 'восемь', 'nine': 'девять', 'ten': 'десять'
}
new_words = {}                      # пошел по простому пути  для отработки методов работы со словарями
new_words.update(rus_words)         # копируем предыдущий словарь
for i, v in rus_words.items():      # перебираем items() и дополняем его новыми элементами
    new_words[i.capitalize()] = v.capitalize()
rus_words.clear()                   # очищаем старый за ненадобностью


def num_translate(word):
    print(new_words.get(word, 'None'))


user_word = input('введите число (англ.) - ')
num_translate(user_word)
