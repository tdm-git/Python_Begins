class Worker:
    def __init__(self, name: str, surname: str, position: str, **kwargs):
        self.name = name
        self.surname = surname
        self.position = position
        if kwargs:
            self._income = kwargs


class Position(Worker):
    def get_full_name(self):
        print(f'ФИО сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'gross сумма на руки: {sum(self._income.values())}')

p1 = Position('Иван', 'Иванов', 'генеральный директор', wage=500)
p2 = Position('Петр', 'Петров', 'финансовый  директор', wage=250, bonus=250)
p3 = Position('Сидор', 'Сидоров', 'комерческий директор', wage=200, bonus=150, kpi=150)
for p in p1, p2, p3:
    p.get_full_name()
    p.get_total_income()


