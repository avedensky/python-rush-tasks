#!/usr/bin/env python3
#coding: utf-8
"""
Решение с проверкой ввода на корректность данных
"""

def get_integer(string):
    """Возращает целое число из строки или None если ошибка"""
    try:
        return int(string)
    except ValueError:
        print('Ошибка: это не число')
        return None

print('Перемножить два целых числа.')
a = get_integer(input('Введите первое число:'))
b = get_integer(input('Введите второе число:'))
if a and b:
    print(a * b)
else:
    print('Ошибочный ввод')


