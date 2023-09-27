#!/usr/bin/python3
class Book:
    def __init__(self, name):
        self.__name = name
    @property    
    def name(self):
        print(" in getter")
        return self.__name
    @name.setter
    def name(self, new):
        print("in setter")
        self.__name= new   


m1 = Book("aaaaa")
print(m1.name)
m2 = Book("hhhhhhhhh")
print(m2.name)
