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



# Clock 29AUG2023 (By Rehana SULTANA)

# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


class classVCO: 
    
    def __init__(self,freq,Ts):
        self.freq = freq
        self.Ts = Ts
        self.maxCountVal = self.freq * self.Ts
        self.countVal = self.maxCountVal
        self.noise = 0
        
     
    def VCOstep(self):
        
        c = self.countVal
        m = self.maxCountVal
        
        
        # trigger graph logic
        if c == 0.5*m:
            edgeFlag = -1
            
        elif  c == m:
            edgeFlag = 1
            
        else:
            edgeFlag = 0
            
        # Square graph logic    
        if(c > 0.5*m):
            squareGraph = 1
        else:
            squareGraph = 0   
        
        # Decrement of countval by 1     
        self.countVal = self.countVal - 1
        
        # self.noise = self.noise + np.random.uniform(low=5, high=10, size=1)[0]
        
        # Resetting step (AFTER ONE CYCLY)
        if self.countVal == 0:
            self.countVal = m # Resetting the countval to max value
            self.noise = self.noise + np.random.normal(loc=0, scale=0.5, size=1)[0] #Accumulating noise
            # self.noise = self.noise + np.random.uniform(low=0, high=10,size=1)[0] #Accumulating noise
            
    
        return edgeFlag, squareGraph
    
    
    # def randomNumber(self):
    #     time_list = []
    #     n = 2048

    #     for i in range(0, n):
    #         temp_rn = np.random.normal(loc=0, scale=0.5, size=1)
    #         time_list.append(temp_rn) 
            
    #     time_array = np.array(time_list)
        
        



     
         
s1 = classVCO(10,1) #Initializing classVCO



tt = []
VCOout = []
count = []

for i in range(0,50,1): 
       
    # tt.append(i)
    
    temp_countval = s1.countVal
    temp_noise = s1.noise
    temp = s1.VCOstep()
    
    
    VCOout.append(temp[1])
    count.append(temp_countval)
    
    tt.append(i + temp_noise)
    
    print("Time, countval , VCOout : ",i + temp_noise, ", ", temp_countval, ",", temp)
   


plt.plot(tt, VCOout, marker='o') 
plt.xlim(100, 300) 
plt.stem(tt, count) #marker='o')  
plt.show()












