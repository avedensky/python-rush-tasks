#!/usr/bin/env python3
#coding: utf-8
import random

class Singlton():
    """клсассический синглтон"""
    __instance = None

    def __init__(self):        
        self.number = random.randint(1, 10)

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Singlton)
        return cls.__instance


class A():
    """ Обычный класс, для сравенения"""
    def __init__(self, *args, **kwargs):        
        self.number = random.randint(1, 10)


def testing():
    #Проверка, создаем 5 объектов типа синглтон
    print('Экземпляры от Singlton')
    lst = [Singlton() for i in range(0, 5)]
    for obj in lst:
        print ('Name : {}  id : {}'.format(obj.number, id(obj)))

    print()
    print('Экземпляры от A')
    #Проверка, создаем 5 объектов обычного типа A
    lst = [A() for i in range(0, 5)]
    for obj in lst:
        print ('Name : {}  id : {}'.format(obj.number, id(obj)))          


if __name__=='__main__':
    testing()