from itertools import zip_longest


def summa(x, y):
    try:
        return x + y
    except:
        return str(x) + str(y)


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return ''.join([f'{list(i)}\n' for i in zip(*self.data)])

    def __add__(self, other):
        return Matrix([[summa(x, y) for x, y in zip_longest(i, j, fillvalue=0)]
                       for i, j in zip_longest(self.data, other.data, fillvalue=[])])


m1 = Matrix([['a', 'b', 'c'], [1, 2, 3]])
print(m1)
m2 = Matrix([[2, 2, 2], [3, 3, 3], [4, 4, 4]])
print(m2)
print(m2 + m1)
