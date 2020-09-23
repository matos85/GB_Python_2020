# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:53:29 2020

@author: Матосян
"""

start_result = int(input('Сколько километров пробежал в первый день? '))
target_result = int(input('Укажите целевое растояние: '))
result_day = start_result
dai = 0
while True:
    dai += 1
    result_day = result_day + (result_day * (10 / 100))
    print(f'{dai}-й день: {"%.2f" % (result_day)}')
    if result_day > target_result:
        print('На {} день спортсмен достиг результата - не менее {} км'.format(dai, "%.0f" % (result_day)))
        break
