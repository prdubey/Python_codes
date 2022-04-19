# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:51:15 2022

@author: prdubey

OOP
"""

class Coordinate (object): #'object' is used for binding all basic python methods.
    #<Class Name> <class parent>
    #<Define Attributes here>
        #Data Attributes
        #Procedural Attributes
    def __init__(self,x,y):
        self.x = x #binding X and Y to class x y value automatically.
        self.y = y
        
    def distance(self,other): #Passing second argument through 'other'. other has same attributes as defined in __init__
        x_diff = (self.x - other.x)**2
        y_diff = (self.y - other.y)**2
        return (x_diff + y_diff)**0.5
    
    def __str__(self):
        #return "<" + str(self.x) + "," + str(self.y) + ">"
        return "<" + str(self.x) + "," + str(self.y) + ">"

c = Coordinate(0, 0)
origin =Coordinate(3, 4)     
print(c)

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)

clock = Clock('5:30')
clock.print_time()     

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(self.time," is not the same ",time)

clock = Clock('5:30') #initialization
clock.print_time('10:30') #calling method and method here needs two argument, 5:30 through init and 10:30 through method call.

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()




        