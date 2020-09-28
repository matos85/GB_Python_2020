# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:01:41 2020

@author: Матосян
"""

inpt=input('Введите элементы списка, через пробел! Введены: ').split()
j=0
res=[]
if len(inpt)%2!=0:
    z=inpt.pop(len(inpt)-1)
for y in range(len(inpt)-1):
    if j ==len(inpt):
        break
    el=inpt[j]
    el1=inpt[j+1]
    el,el1=el1,el
    res.insert(j,el)
    res.insert(j+1,el1)
    j+=2
res.append(z)
print(f'res= {res}')