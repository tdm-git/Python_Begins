class Data:
    def __init__(self, text_data):
        self.data = text_data

    @classmethod
    def digit_data(cls, text_data: str):
        d, m, y = map(int, text_data.split('-'))
        if cls.true_data(d, m, y):
            return d, m, y
        return 0, 0, 0

    @staticmethod
    def true_data(d, m, y):
        true_date = True
        if d < 1 or d > 31:
            print('некорректный ввод дня месяца!')
            true_date = False
        if m < 1 or m > 12:
            print('некорректный ввод месяца!')
            true_date = False
        if y < 1980 or y > 2021:
            print('некорректный ввод года!')
            true_date = False
        return true_date

d1 = Data("13-00-2021")
d2 = Data("25-03-2021")

print(f'получаем из даты {d1.data} кортеж чисел - {Data.digit_data(d1.data)}')
print(f'получаем из даты {d2.data} кортеж чисел - {Data.digit_data(d2.data)}')
