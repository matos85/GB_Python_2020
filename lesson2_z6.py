# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:05:55 2020

@author: Матосян
"""

import copy

products = []
k_product = ()
name = []
price = []
number = []
unit = []
analytics = {}
j = 1
i = 0
dictionaries = {}

while True:
    i = 0
    product = input(
        'Введите через пробел: Название, Цену, Количество и ед. измерение товара.Для выхода введите 0. Введено: ').split()
    if product[0] == '0':
        print('\n')
        break
    dictionaries['название'] = product[i]
    dictionaries['цена'] = product[i + 1]
    dictionaries['количество'] = product[i + 2]
    dictionaries['ед'] = product[i + 3]
    k_product = (j, dictionaries)
    sa = copy.deepcopy(k_product)
    products.append(sa)
    j += 1

print('[')
for i in products:
    print(i)
print(']')
# print(f'Тип данных products: {type(products)}')
# print(products) - для вывода 1 строкой. просто не понял надо было копироват вывод как в постановке задачи или нет

print('\n')

print('Аналитика:')
for i in range(len(products)):
    ss = products[i][1]
    name.append(ss['название'])
    price.append(ss['цена'])
    number.append(ss['количество'])
    unit.append(ss['ед'])
analytics['название'] = name
analytics['цена'] = price
analytics['количество'] = number
analytics['ед'] = unit

print('{')
for key, val in analytics.items():
    print(f'"{key}": {val}', end='\n')
print('}')
# print(f'Тип данных products: {type(analytics)}')
# print(analytics) - для вывода 1 строкой. просто не понял надо было копироват вывод как в постановке задачи или нет
