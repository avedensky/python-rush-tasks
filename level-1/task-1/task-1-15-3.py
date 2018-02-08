#!/usr/bin/env python3
#coding: utf-8
"""
pythonic way
"""

a = 1
b = 2
print('a = {}, b = {}'.format(a, b))

#Тут: сначала создается кортеж в правой части, затем он распаковывается в переменные
a, b = b, a 
print('a = {}, b = {}'.format(a, b))
