from functools import reduce

lst = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda x, y: x + y, lst))
