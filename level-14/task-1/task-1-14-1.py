#!/usr/bin/env python3
#coding: utf-8
"""
1. Используя множественное наследование переопределите метод базового класса
2. Как можно вызвать переопределнный метод базового класса
"""

class Base():   
    def run(self):
        print ('Base: I can run' )


class Mixin1():
    def run(self):
        print ("Mixin:I can fly")


class SuperMan(Mixin1, Base):
    def doing(self):        
        self.run()       #Замещение базового метода, методом из миксина       
        Base.run(self)   #Вызов Родителя Base с передачей текущего инстанса
        Base.run(Base()) #Вызов Родителя Base с передачей инстанса Base


def main():
    super_man = SuperMan()
    super_man.doing()


if __name__=='__main__':
    main()

