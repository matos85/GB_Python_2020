def my_func(var1, var2, var3):
    z = 0
    var_local = [var1, var2, var3]
    v1 = min(var_local)
    for i in var_local:
        if i == v1:
            i = 0
        z = z + i
    return z


varible = input('Введите 3 переменые через пробел ').split()
var1 = int(varible[0])
var2 = int(varible[1])
var3 = int(varible[2])

print(my_func(var1, var2, var3))
