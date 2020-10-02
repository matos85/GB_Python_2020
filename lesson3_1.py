def division(var1, var2):
    try:
        print(var1 / var2)
    except ZeroDivisionError:
        print('Деление на 0 запрещено!')


a = int(input('Введите переменую 1: '))
b = int(input('Введите переменую 2: '))
division(a, b)
