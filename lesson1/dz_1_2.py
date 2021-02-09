# Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции! # К каждому элементу списка добавить 17 и заново вычислить
# сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Внимание: новый список не создавать!!!
list_result = []
summator = 0
summator17 = 0
for i in range(1, 1000, 2):
    result = i**3
    list_result.append(result)

    sum_result = 0
    for ch in str(result):
        sum_result += int(ch)
    if sum_result % 7 == 0:
        summator += result
    # summator += (result if sum(map(int, str(result))) % 7 == 0 else 0)

    sum_result17 = 0
    for ch in str(result + 17):
        sum_result17 += int(ch)
    if sum_result17 % 7 == 0:
        summator17 += result
    # print(result, '-', sum_result, ":", result + 17, "-", sum_result17)
print("список кубов нечетных чисел -", list_result)
print("сумма чисел из списка, сумма чисел которого кратна 7 - ", summator)
print("сумма чисел из списка, к которым добавлено число 17 и сумма чисел которого кратна  7 - ", summator17)
