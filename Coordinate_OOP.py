# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:40:35 2022

@author: prdubey
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return "Coordinate(%d,%d)" % (self.x,self.y)
    
c1 = Coordinate(1, -8)
c2 = Coordinate(1, -8)

print(repr(c1))