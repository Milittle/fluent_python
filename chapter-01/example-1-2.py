#!/usr/bin/python
#-*- coding: utf-8 -*-
# author: milittle
# A simple 2D vector class

from math import hypot

class Vecotr:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    # when we call str(vector), if the __str__ method not implement then the interpretor will call __repr__
    def __repr__(self): # it will be directly invoke the vector instance. 
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self): # support abs method
        return hypot(self.x, self.y)


    # if the vector instance in the if-statement or something condition statement, the interpretor will call this method
    # if this method not implement, the interpretor will call __len__, if len return 0, False, Otherwise, True
    def __bool__(self): # bool method
        return bool(abs(self))

    def __add__(self, other): # plus
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar): # multiply
        return Vector(self.x * scalar, self.y * scalar)
