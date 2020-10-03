from sys import argv
from itertools import count

param = argv[1:3]
for i in count(int(param[0]), int(param[0])):
    print(i)
    if i > (int(param[0]) + int(param[0])):
        break
