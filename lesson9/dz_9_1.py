from time import sleep


class bcolors:
    ENDC = '\033[0m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
# задаём режим работы светофора - порядок цветов и продолжительность каждого
traffic_color: dict = {'red': ('yellow', 7, bcolors.RED),
                       'yellow': ('green', 2, bcolors.YELLOW),
                       'green': ('red', 8, bcolors.GREEN)}


class TrafficLight:
    __color = 'red'

    def running(self, kol: int = 7):  # параметр - количество циклов работы светофора
        print(f'{bcolors.ENDC}# светофор включен! - #{self.__color}# сигнал ')
        for i in range(kol):
            self.__color = traffic_color[self.__color][0]
            print(f'{traffic_color[self.__color][2]} #{self.__color}# сигнал светофора ({traffic_color[self.__color][1]} cек)')
            sleep(traffic_color[self.__color][1])
        print(f'{bcolors.ENDC}# светофор выключен!')


s = TrafficLight()  # создаём объект, экземпляр класса сфетоворов
s.running()  # демонстрируем работу
s.running(3)  # продолжит работу светофора
