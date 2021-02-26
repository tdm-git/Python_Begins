from time import perf_counter
import sys
# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
start = perf_counter()  # 1й вариант List Comprehensions & zip
result = [ex for el, ex in zip(src, src[1:]) if el < ex]
print(result)
print('время выполнения 1: ', perf_counter() - start, sys.getsizeof(result))

start = perf_counter()  # 2й вариант со списком
ex = src[0]
result = []
for el in src:
    if el > ex:
        result.append(el)
    ex = el
print(result)
print('время выполнения 2: ', perf_counter() - start, sys.getsizeof(result))

start = perf_counter()  # 3й вариант со множеством
ex = src[0]
result = set()
for el in src:
    if el > ex:
        result.add(el)
    ex = el
print(result)  # НО порядок произвольный((( и с неуникальными уже будет некорректно
print('время выполнения 3: ', perf_counter() - start, sys.getsizeof(result))
