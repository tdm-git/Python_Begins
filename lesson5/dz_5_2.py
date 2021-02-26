# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
num = 15
odd_to_15 = (i for i in range(1, num + 1, 2))

print(odd_to_15)  # - <generator object odd_nums at 0x000001475E5DBF90>
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