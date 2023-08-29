# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 23:55:32 2023

@author: ARIJIT
"""


# PYTHON TUTORIAL 30AUG2023

#############################################################
# Main topics to remember/learn in Python :
# 
#    1. Data types/ Data structure : list, array, int, float, string, tuple, dict, plot
#    2. Control flow : Branching : if-else, iteration : forloop, while etc
#    3. Functions/class : built-in functions, functions from imported module, User Defined Functions - def, lambda
# 
#    4. Interaction among 1, 2, and 3
#############################################################




# https://pynative.com/python-object-oriented-programming-oop-exercise/


# Class Exercises 01
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.


class Vehicle:
    
    def __init__(self, ms, mlg, clr="White"):
        self.max_speed = ms
        self.milage = mlg
        self.color = clr



polo = Vehicle(240, 20)
polo.max_speed
polo.milage


# Class Exercise 02
# Create a Vehicle class without any variables and methods


class Vehicle:
    pass



# Class Ex 03
# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    
    def __init__(self, ms, mlg):
        self.max_speed = ms
        self.milage = mlg
        



class Bus(Vehicle):
    
    def odo(self, km):
        self.total_km = km
        




polo_bus = Bus(100, 10)
polo_bus.odo(1000)



volo_bus = Bus(200, 20)




# Q - Define a property that must have the same value for every class instance (object)


class Vehicle:
    
    colour = "White" # Hard coding the colour into the class definition
    
    def __init__(self, ms, mlg):
        self.max_speed = ms
        self.milage = mlg
        



bus = Vehicle(10, 2)
bus2 = Vehicle(100, 22)
 



# Q Program to write factorial of a number.

# n ! = n * n-1 * n-2 * ... * 1


def facto(n):
    
    # default_num = n
    
    prod = 1
    
    
    for x in range(n):
        y = x + 1

        prod = prod * y
    
    return prod














































