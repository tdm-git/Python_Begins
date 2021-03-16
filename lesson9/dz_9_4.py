class Car:
    def __init__(self, name: str = 'bmw', speed: int = 0, color: str = 'red', is_police: bool = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('автомобиль заведён')

    def stop(self):
        print('автомобиль остановился')

    def turn(self, direction: str):
        print(f'автомобиль поворачивает в {direction} направлении')

    def show_speed(self):
        print(f'скорость движения автомобиля : {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'скорость движения: {self.speed} км/ч', '!!! превышение допустимой скорости' if self.speed > 60 else '')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'скорость движения: {self.speed} км/ч', '!!! превышение допустимой скорости' if self.speed > 40 else '')


class PoliceCar(Car):
    def __init__(self, name: str = 'audi', speed: int = 55, color: str = 'blue'):
        super().__init__(name, speed, color)
        self.is_police = True


tc = TownCar(speed=60)
tc.go()
tc.show_speed()
sc = SportCar()
sc.go()
sc.turn('разворот')
wc = WorkCar(speed=50)
wc.go()
wc.show_speed()
pc = PoliceCar()
pc.go()
pc.show_speed()
pc.stop()
