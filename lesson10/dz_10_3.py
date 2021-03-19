class Cell:
    def __init__(self, nums: int = 5):
        self.nums = nums

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums - other.nums > 0:
            self.nums -= other.nums
        else:
            print('!!!вычитание клеток возможно только если первая больше второй')
        return Cell(self.nums)

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell((self.nums + other.nums)//2)

    def make_order(self, kol: int = 5):
        return str(self.nums)+'\n'+''.join(['*\n' if (i + 1) % kol == 0 else '*' for i in range(self.nums)])

c1 = Cell(8)
c2 = Cell(5)

print((c1 + c2).make_order(7))
print((c1 * c2).make_order(7))
print((c1 / c2).make_order(7))
print((c1 - c2).make_order(7))
