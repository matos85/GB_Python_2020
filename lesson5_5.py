from functools import reduce

with open('for_dz_5.txt', 'w+') as f:
    f.write(' '.join([str(i) for i in range(25) if i % 2 == 0]))
    f.seek(0)
    nums=[int(i) for i in f.read().strip().split()]
print(reduce(lambda x, y: x + y, nums))
