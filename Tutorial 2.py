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



# Clock 29AUG2023

# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt



class classVCO:
    def __init__(self, freq, Ts):
        self.freq = freq
        self.Ts = Ts
        self.maxCountVal = self.freq * self.Ts
        self.countVal = self.maxCountVal
     
        
     
        
    def VCOstep(self):
        c = self.countVal
        m = self.maxCountVal
        
        if c == 0.5*m:
            edgeFlag = -1
            
        elif  c == m:
            edgeFlag = 1
            
        else:
            edgeFlag = 0
            
        self.countVal = self.countVal - 1
        
        
        
        # Resetting the countval
        if self.countVal == 0:
            self.countVal = m
            
        return edgeFlag   




    

s1 = classVCO(4,1) #Initializing classVCO


tt = []
tt_with_jitter = []
pulse = []
count = []

for i in range(0,16,1): 
    tt.append(i)
    tt_with_jitter.append(i + np.random.normal(0, 0.5, 1))
    pulse.append(s1.VCOstep())
    count.append(s1.countVal)
    
    
    # print("Time, countval , pulse : ",i, ", ", s1.countVal, ",", s1.VCOstep())

        
    
plt.scatter(tt, pulse, marker='o')
plt.scatter(tt_with_jitter, pulse, marker='o')
     
       










































