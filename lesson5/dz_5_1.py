# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
def odd_nums(num):
    for i in range(1, num + 1, 2):
        yield i

odd_to_15 = odd_nums(15)
print(odd_to_15)  # - <generator object odd_nums at 0x000001475E5DBF90>
# print(*odd_to_15)  # - распакует весь список, и дальнейшее обращение будет невозможно, т.к. yield это состояние
print(next(odd_to_15))
# 1
print(next(odd_to_15))
# 3
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
print(next(odd_to_15))
# 15
# next(odd_to_15)  # - следущее обращение приведёт к сообщению ...StopIteration...

















