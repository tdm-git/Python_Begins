from time import perf_counter
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации

start = perf_counter()  # 1й вариант с перебором только уникальных значений
result = [el for el in set(src) if src.count(el) == 1]
print(result)
print('время выполнения 1: ', perf_counter() - start)


start = perf_counter()  # 2й вариант со множеством
result = set()
tmp = set()
for el in src:
    if el not in tmp:
        result.add(el)
    else:
        result.discard(el)
    tmp.add(el)
print([*result])  # переупакуем множество в список
print('время выполнения 2: ', perf_counter() - start)
