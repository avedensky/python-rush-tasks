#!/usr/bin/env python3
#coding: utf-8
"""
pythonic way
"""

lst = ['aaabb', 'caca', 'dabc', 'acc', 'abbb']
res = [s.count('a') for s in lst]
print(res)
