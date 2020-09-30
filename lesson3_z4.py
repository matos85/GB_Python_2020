def my_func(x, y):
    return x ** y


def my_func2(x, y):
    i = 1
    a = x
    while i != abs(y):
        a = a * x
        i += 1
    z = 1 / a
    return z


varible1 = int(input('Введите положительное число '))
varible2 = int(input('Введите отрицательно число '))
print(my_func(varible1, varible2))
print(my_func2(varible1, varible2))
