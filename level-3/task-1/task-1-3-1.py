#!/usr/bin/env python3
#coding: utf-8
"""
Решение в лоб, попытка написать код не на python :)
"""

text = input('Введите строку:')
s = ''
for i in range(len(text)-1, -1, -1):
    s+=text[i]

print(s)    



