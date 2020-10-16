class Cell:
    def __init__(self):
        self.numbers = 12

    def __add__(self, other):  # сложение
        self.numbers += other

    def __sub__(self, other):  # вычитание
        z = 0
        z = z + self.numbers
        self.numbers -= other
        if self.numbers <= 0:
            self.numbers = z
            print('Количестов клеток не может быть равна нуля или быть меньше')


    def __mul__(self, other):  # умножение
        self.numbers *= other

    def __truediv__(self, other):  # деление
        self.numbers = int(self.numbers / other)

    def make_order(self, n):
        z = 0
        for i in range(self.numbers):
            print('*', end='')
            z += 1
            if z == n:
                print(' ', end='\n')
                z = 0


f_cell = Cell()
# f_cell.__add__(1)
# print(f_cell.numbers)
# f_cell.__sub__(2)
# print(f_cell.numbers)
# f_cell.__mul__(3)
# print(f_cell.numbers)
# f_cell.__truediv__(4)
# print(f_cell.numbers)

f_cell.make_order(5)

# return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])
