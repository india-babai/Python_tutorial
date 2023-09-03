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
import math


class classVCO: 
    
    def __init__(self,freq,Ts):
        self.freq = freq
        self.Ts = Ts
        self.maxCountVal = self.freq * self.Ts # Length of the period of the signal
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
        if self.countVal == 0: # this where a new cycle starts
            
            
            # random_noise = 0
            random_noise = math.floor(np.random.normal(5,5,1)[0])
            
            self.maxCountVal = self.maxCountVal + random_noise
            self.countVal = self.maxCountVal # Resetting the countval to max value so that the cycle restarts
            
            # random_noise = 0
            # random_noise = math.floor(np.random.normal(0,5,1)[0])
            
            # self.countVal = m + random_noise # Resetting the countval to max value
            # self.noise = self.noise + np.random.normal(loc=0, scale=0.5, size=1)[0] #Accumulating noise
            # self.noise = self.noise + np.random.uniform(low=0, high=10,size=1)[0] #Accumulating noise
            
    
        return edgeFlag, squareGraph


     
         
s1 = classVCO(10,1) #Initializing classVCO



tt = []
VCOout = []
count = []
max_count_val = []



for i in range(0,1000,1): 
       
    # tt.append(i)
    
    temp_countval = s1.countVal
    temp_noise = s1.noise
    temp_max_count_val = s1.maxCountVal
    temp = s1.VCOstep()
    
    
    VCOout.append(temp[1]) # Taking the square graph
    count.append(temp_countval)
    
    max_count_val.append(temp_max_count_val)
    
    
    tt.append(i)
    
    # print("Time, countval , VCOout : ",i , ", ", temp_countval, ",", temp)
   


# plt.plot(tt, VCOout, marker='o') 
plt.step(tt, VCOout)
# plt.xlim(100, 300) 
# plt.stem(tt, count) #marker='o')  
plt.show()







# Period Count function

def period_count(signal):
    '''
    Parameters
    ----------
    signal : Sequence of 1's and 0's
        
    
    Returns
    -------
    T : number of complete cycles/period in the sequence

    '''
    
    
    period_count = 0
    previous_value = None
    
    
    list_of_cycle_lenghts = []
    cycle_length = 0
    
    
    for binary_value in signal:
        
        if previous_value is None:
            previous_value = binary_value #Setting the initial state of previous_value
        

        
        if previous_value == 0 and binary_value == 1 :
            period_count = period_count + 1 # Transition from 0 to 1 indicates a complete cycle
            
            list_of_cycle_lenghts.append(cycle_length + 1)
            
            cycle_length = 0
            
            
        else:
            cycle_length = cycle_length + 1
            
            
    
        previous_value = binary_value # Storing the previous value at the end of the for loop


    
    
    return period_count, list_of_cycle_lenghts


t = period_count(VCOout)

t[0]

t[1]
np.std(t[1])

















