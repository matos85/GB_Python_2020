# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:03:56 2020

@author: Матосян
"""

words = input('Введите некоторое количетсво слов по желанию. Ваши слова: ').split()
for i in range(len(words)):
    if len(words[i]) > 10:
        print(f'Срока номер:{i} - cлово: {words[i][:10]}')
    else:
        print(f'Срока номер:{i} - cлово: {words[i]}')