#!/usr/bin/env python3
#coding: utf-8
"""
pythonic way
"""

a = 1
b = 2
print('a = {}, b = {}'.format(a, b))

a = b ^ a
b = b ^ a
a = b ^ a
print('a = {}, b = {}'.format(a, b))

