class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем {self.title} карандашом')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем {self.title} ручкой')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем {self.title} маркер')


Stationery1 = Pen('Parker')
Stationery2 = Pencil('Kohinoor')
Stationery3 = Handle('Brauberg')
for st in Stationery1, Stationery2, Stationery3:
    st.draw()
