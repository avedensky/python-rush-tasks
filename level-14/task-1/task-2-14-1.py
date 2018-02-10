#!/usr/bin/env python3
#coding: utf-8
"""
2.1 Создать класс для работы со списком случайных значений, 
методы: заполнить список, очистить список, показать список. 
2.2. Добавить класс миксин helper 
с методами: показать среднее значение, показать минимальное значение, 
показать максимальное значение
"""
import random

class SomeBaseList ():
    pass

class Helper():
    """ миксин helper """
    def __init__(self):
        super().__init__()

    def show_min(self):
        print('Min: {}'.format(min(self._lst)))

    def show_max(self):
        print('Max: {}'.format(max(self._lst)))

    def show_avg(self):
        print('Avg: {}'.format(sum(self._lst) / len(self._lst)))    
        

class RandomList(Helper, SomeBaseList):
    """ класс для работы со списком случайных значений """
    def __init__(self):
        super().__init__()
        self._lst = []

    def fill(self):
        self._lst = [random.randint(0, 100) for i in range(0,10)]

    def clear(self):
        self._lst = []        

    def show(self):
        print(self._lst)


def main():
    r = RandomList()
    r.fill()
    r.show()
    r.show_min()
    r.show_max()
    r.show_avg()


if __name__=='__main__':
    main()

