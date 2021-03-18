class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return ''.join([f'{list(i)}\n' for i in zip(*self.data)])

    def __add__(self, other):
        return Matrix([[x+y for x, y in zip(i, j)] for i, j in zip(self.data, other.data)])


m1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(m1)
m2 = Matrix([[3, 4, 5], [6, 7, 8], [5, 5, 5]])
print(m2)
m3 = m1 + m2
print(m3)
