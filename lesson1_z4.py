# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:08:21 2020

@author: Матосян
"""

first = int(input('Введите число: '))
z1 = int(first) // 10
x1 = int(first) % 10
while z1 != 0:
    z1 = int(z1) // 10
    x2 = int(z1) % 10
    if x1 < x2:
        x1 = x2
print(x1)
