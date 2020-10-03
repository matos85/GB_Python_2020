old = input('Введите через пробел числа: ').split()
print(f'Исходный список: {old}')
new = [int(i) + 1 for i in old]
print(new)
