class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in range(len(self.matrix)):
            print(' \n')
            for z in range(len(self.matrix[i])):
                return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        f = 0
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) == len(other.matrix[i]):
                f += 1
        if f == len(self.matrix):
            for i in range(len(self.matrix)):
                for z in range(len(self.matrix[i])):
                    self.matrix[i][z] = self.matrix[i][z] + other.matrix[i][z]
        else:
            print('Матрицы разной длины нельзы складывать')


a = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
b = Matrix([[1, 5, 9], [5, 6, 7], [8, 9, 0, 22]])

a + b
print(a)
