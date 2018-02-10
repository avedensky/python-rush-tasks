#!/usr/bin/env python3
#coding: utf-8
"""
Решение с проверкой ввода на корректность данных
"""

def get_float(string):
    """Возращает целое число из строки или None если ошибка"""
    try:
        return float(string)
    except ValueError:
        print('Ошибка: это не число')
        return None

print('Расчет площади и периметра прямоугольника')
a = get_float(input('Длинна стороны А:'))
b = get_float(input('Длинна стороны B:'))
if a and b:
    print("Площадь прямоугольника: ", a * b)
    print("Периметр прямоугольника: ", 2 * (a + b))
else:
    print('Ошибочный ввод')


