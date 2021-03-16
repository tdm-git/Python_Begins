class Road:
    def __init__(self, length: int = 0, width: int = 0):
        self._length = length
        self._width = width

    def calc_asf(self, thickness: int = 1, ves_asf: int = 25):
        print(f' на строительство дороги потребуется - {self._length * self._width * thickness * ves_asf} кг. асфальта')

route69 = Road(20, 5000)
route69.calc_asf(5)
