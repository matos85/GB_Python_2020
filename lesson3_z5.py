def summing():
    flag = True
    z = []
    while flag:
        n = input('Ввоодите числа через пробел. Введено: ').split()
        for i in n:
            if i != 'q':
                z.append(int(i))
            if i == 'q':
                flag = False
        print(sum(z))


summing()
