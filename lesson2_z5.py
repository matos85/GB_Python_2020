# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:05:01 2020

@author: Матосян
"""

rating = [97, 56, 34, 34, 33, 32, 20, 19, 11]
i = int(input('Введите элемент для рейтинга. Вы ввели: '))
rating.append(i)
rating.sort()
rating.reverse()
print(rating)