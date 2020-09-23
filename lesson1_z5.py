# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:04:51 2020

@author: Матосян
"""
# не уверен в точности экономических расчетов но думаю суть отразил
revenue = int(input('Введите значение выручки:'))
cost = int(input('Введите значение издержек:'))
profit = revenue - cost
if profit > 0:
    print('Ваша выручка больше издержек')
    print(f'Рентабельность вашей выручки: {(profit / revenue) * 100}')
    num_employees = int(input('Введите численость сотрудников для расчета прибыли из расчета на сотрудника: '))
    profit_num_employees = profit / num_employees
    print(f'Ваша прибыль в рассчете на 1 сотрудника: {profit_num_employees}')
else:
    print('Ваша выручка меньше издержек')
