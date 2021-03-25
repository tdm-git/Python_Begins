class Complex:
    def __init__(self, d, dd):
        self.d = d
        self.dd = dd

    def __str__(self):
        return f'({self.d}+{self.dd}j)'

    def __add__(self, other):
        return Complex(self.d + other.d, self.dd + other.dd)

    def __mul__(self, other):
        return Complex(self.d * other.d - self.dd * other.dd, self.d * other.d + self.dd * other.dd)


x = Complex(1, 2)
y = Complex(3, 4)
print('x =', x)
print('y =', y)
print('x+y =', x + y)
print('x*y =', x * y)
