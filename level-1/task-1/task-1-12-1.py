#!/usr/bin/env python3
#coding: utf-8
"""
pythonic way
"""
N = 20
M = 20
for i in range(1,N):    
    print(''.join(['{:>3} '.format(i*j) for j in range(1,M)]))
    
        


