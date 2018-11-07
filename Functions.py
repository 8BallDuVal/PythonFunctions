'''
Created on May 21, 2018

@author: daduva
'''

#define the function with the keyword 'def' and then the function's name:

#functions can return a value, but don't have to... 

def add_two_nums(a, b):
    return a + b

def multipy_two_nums(a, b):
    return a * b

import math

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
    
class Triangle():
    def __init__(self, a, b):
        self.base = a
        self.height = b
    
    def area(self):
        return .5*self.base*self.height
    
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*math.pi
    
    def perimeter(self):
        return 2*self.radius*math.pi
    
class Cylinder():
    def __init__(self, r, h):
        self.radius = r
        self.height = h
    
    def area(self):
        return ((2*math.pi*self.radius*self.height)+(2*math.pi*self.radius**2))
    
    def volume(self):
        return (math.pi*(self.radius**2)*self.height)
    
def bubblesort_ascending(list):
    #swap the elements to arrange in order:
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i+1] = temp
                


def bubblesort_descending(list):
    #swap the elements to arrange in order:
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i]<list[i+1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i+1] = temp

def decimal_to_binary(decimalnumber):
    binary_num = bin(decimalnumber)
    binary_num = str(binary_num)
    binary_num = binary_num[2:]
    binary_num = int(binary_num)
    return binary_num

def binary_to_decimal(binarynumber):
    binarynumber = str(binarynumber)
    return int(binarynumber, 2)
