old = input('Введите через пробел числа: ').split()
print([j for i, j in zip(old, old[1:]) if j > i])

