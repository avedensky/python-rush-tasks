#!/usr/bin/env python3
#coding: utf-8
"""
pythonic way
"""

a = [1,2,3]
b = [6,4,0]

c = [a[i]+b[i] for i in range(0,len(a))]

print(c)

