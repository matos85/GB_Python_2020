def fact(n):
    i = 0
    while True:
        i = i + 1
        yield i


n = int(input('Введите факториал искомого числа: '))
j = 1
for el in fact(n):
    j = j * el
    if el == n:
        break
print(f'Факториал числа {n} равен: {j}')
