# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:16:27 2020

@author: Матосян
"""

print('Введите время в секундах. Но не более 86 400 секунд! Будет больше дня!')
first = int(input('Введите количество секунд: '))

if first < 60:
    print(f'00:00:{first}')
elif first < 3600:
    minutes = first // 60
    seconds = first % 60
    print(f'00:{minutes:02}:{seconds:02}')
elif first <= 86400:
    hours = first // 3600
    minutes = (first // 3600) % 60
    seconds = first % 60
    print(f'{hours:02}: {minutes:02}:{seconds:02}')
else:
    print('Вы вели больше 1 дня.')
