class Coat:
    def __init__(self, size):
        self.size = size

    @property
    def need_cloth(self):
        return self.size / 6.5 + 0.5


class Suit:
    def __init__(self, height):
        self.height = height

    @property
    def need_cloth(self):
        return self.height * 2 + 0.3


class Clothes:
    def __init__(self, name):
        self.name = name
        self.sort = []
        self.cloth = 0

    def add_sort(self, cloth):
        self.cloth += cloth.need_cloth
        self.sort.append(cloth)

new_set = Clothes('Гардероб')
new_set.add_sort(Coat(12))
new_set.add_sort(Suit(8))
new_set.add_sort(Coat(15))

print(new_set.name, 'всего требуется - ',  round(new_set.cloth,2), 'м ткани')
print(*[(type(i).__name__, round(i.need_cloth, 2)) for i in new_set.sort])

