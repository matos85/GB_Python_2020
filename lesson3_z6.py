# функция написана так что бы не было важно какое количество слов пришло на вход.
def int_func(words):   
    res = []
    for i in words.split():
        res.append(i.title())
    return res


n = input('Ввоодите числа через пробел. Введено: ')
print(*int_func(n))
