#!/usr/bin/env python3
#coding: utf-8
"""
pythonic way
"""

lst = ['aaabb', 'caca', 'dabc', 'acc', 'abbb']
res = ','.join(i for i in lst if i.find('c')!=-1)
print(res)
