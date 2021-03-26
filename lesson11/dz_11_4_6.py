class Warehouse:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.device = {}  # оргтехника - описание - клиент

    def recive_eq(self):
        """ прием техники от клиента и размещение её в справочнике класса склад """
        print('Выберите вид оргтехники:')
        type_eq = int(input('[0] - отмена...\n[1] - принтер \n[2] - сканер\n[3] - копир\nвведите порядковый номер - '))
        if type_eq == 0:
            return
        elif type_eq == 1:
            eq_def = Scanner
        elif type_eq == 2:
            eq_def = Scanner
        elif type_eq == 3:
            eq_def = Xerox
        maker = input(' производитель: ')
        model = input(' модель техники: ')
        breakdowm = input('краткое описание проблемы: ')
        self.device[eq_def(maker, model)] = breakdowm

    def move_eq(self, other):
        """ перемещение в ремонт после диагностики с кратким описанием требуемых работ """
        if len(self.device) == 0:
            print(f'на складе "{self.description}" отсутствуют остатки')
            input('\n...нажмите Enter чтобы продолжить...')
            return
        ch = select_eq(self.device)
        if ch is None:
            return
        del self.device[ch]
        other.device[ch] = input('введите список работ: ')

    def make_eq(self, other):
        """ завершение работ и фиксация стоимости работ мастера, для предьявления клиенту """
        if len(self.device) == 0:
            print(f'на складе "{self.description}" отсутствуют остатки')
            input('\n...нажмите Enter чтобы продолжить...')
            return
        ch = select_eq(self.device)
        if ch is None:
            return
        del self.device[ch]
        other.device[ch] = f'к оплате - {input("введите стоимость работ: ")} руб'

    def return_eq(self):
        """ демонстрация работы техники и выдача клиенту, со списанием из остатков """
        if len(self.device) == 0:
            print(f'на складе "{self.description}" отсутствуют остатки')
            input('\n...нажмите Enter чтобы продолжить...')
            return
        ch = select_eq(self.device)
        if ch is None:
            return
        print('демонстрация работы техники:')
        ch.test()
        del self.device[ch]

    def show_eq(self):
        """ текущие остатки по всем складам """
        if len(self.device) == 0:
            return
        print('ОСТАТОК ПО СКЛАДУ: ', self.description)
        for i, j in self.device.items():
            print(f'- {type(i).__name__} (фирмы {i.maker} , модель:{i.model}) - комментарий: {j}')


class Equipment:
    def __init__(self, maker='HP', model='x-1000'):
        self.maker = maker
        self.model = model


class Printer(Equipment):
    def test(self):
        print('PRINT: Testing page.')
        input('\n...нажмите Enter чтобы продолжить...')


class Scanner(Equipment):
    def test(self):
        print('SCANNING: Testing page.')
        input('\n...нажмите Enter чтобы продолжить...')


class Xerox(Equipment):
    def test(self):
        print('COPING: Testing page.')
        input('\n...нажмите Enter чтобы продолжить...')


def select_eq(eq_dict):
    """предоставляет выбор элемента оргтехники из остатков склада хранимых в справочнике"""
    ex_list = list(eq_dict.keys())
    str_choice = '[0] - отмена, вернуться в предыдущее меню...\n'
    for i, k in enumerate(ex_list):
        str_choice += f'[{i + 1}] - {type(k).__name__} ({k.maker} , {k.model}) - комментарий: {eq_dict[k]}\n'
    key = input(str_choice + 'введите порядковый номер - ')
    if not key.isdigit() or int(key) > len(ex_list) or int(key) < 0:
        print('некорректный выбор, вы будете возвращены в предыдущее меню...')
        input('нажмите Enter чтобы продолжить...')
        return None
    key = int(key)
    if key == 0:
        return None
    return ex_list[key - 1]


cls = lambda: print('\n' * 30)  # не нашел очистку экрана, поэтому буду использовать перенос на несколько строк вниз
ware_dict = {1: Warehouse('Этап 1', 'Принято на диагностику'),
             2: Warehouse('Этап 2', 'В ремонте'),
             3: Warehouse('Этап 3', 'К выдаче клиенту')}
menu = {1: 'Прием техники от клиента',
        2: 'Передача в ремонт',
        3: 'Завершение ремонта',
        4: 'Выдача клиенту',
        5: 'Остатки техники на складах',
        0: 'Выход из программы'}
str_menu = '\n'.join([f'[{i}] - {j}' for i, j in menu.items()])
# начальное заполнение складов:
ware_dict[1].device[Printer('HP', 'LJ1000')] = 'заменить картридж'
ware_dict[1].device[Scanner('HP', 'SXN3200')] = 'не включается'
ware_dict[1].device[Xerox('Xerox', 'X2500')] = 'произвести диагностику'
ware_dict[2].device[Scanner('HP', 'SXN3200')] = 'произвести замена барабана'
ware_dict[2].device[Xerox('Xerox', 'X2500')] = 'установить новый ремкомплект'
ware_dict[3].device[Scanner('HP', 'SXN3200')] = 'к оплате - 1000 руб'
ware_dict[3].device[Xerox('Xerox', 'X2500')] = 'к оплате - 2000 руб'
# основная часть программы
while True:
    print('ГЛАВНОЕ МЕНЮ:')
    print(str_menu)
    user_choise = input('\nвведите номер операции: ')
    if not user_choise.isdigit() or int(user_choise) > 5 or int(user_choise) < 0:
        print('некорректный выбор...повторите ввод...')
        input('\n...нажмите Enter чтобы продолжить...')
        cls()
        continue
    cls()
    user_choise = int(user_choise)
    if user_choise == 0:
        break
    elif user_choise == 1:
        ware_dict[1].recive_eq()  # прием техники в ремонт
    elif user_choise == 2:
        ware_dict[1].move_eq(ware_dict[2])  # перемещение в ремонт
    elif user_choise == 3:
        ware_dict[2].make_eq(ware_dict[3])  # завершение ремонта
    elif user_choise == 4:
        ware_dict[3].return_eq()  # выдача клиенту
    elif user_choise == 5:
        for w in ware_dict.values():  # печать остатков
            w.show_eq()
        input('\n...нажмите Enter чтобы продолжить...')
    cls()
