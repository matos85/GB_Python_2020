from sys import argv
from itertools import cycle

param = cycle(argv[1:])
k=0
for i in param:
    print(i)
    k+=1
    if k >15:
        break
