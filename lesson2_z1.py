# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 07:59:35 2020

@author: Матосян
"""

lst = [1, 'abx', 1.3, [1.3, 4, 'asd'], {1: 2, 2: 2}, (1, 2, 3, 4), True, complex(95, 6), {1, 2.3, 7, 9}, b'prinvet']
for i in range(len(lst)):
    print(type(lst[i]))