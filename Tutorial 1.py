# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 00:49:15 2023

@author: ARIJIT
"""


import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import os
import My_List_Of_Funcs as mf


# Topics - 
# 1. Data types -  list , tuple, dictionary
# 2. Looping , Branching , iteration
# 3. Function



def my_sine_curve(x):
    temp = np.sin(x)
    return temp



x = np.linspace(- np.pi, np.pi, 100) # Iterable


# Option 1
empty_list = []

for i in x:
    temp = my_sine_curve(i)
    empty_list.append(temp)


y = np.array(empty_list)


plt.plot(x, y)
plt.scatter(x, y)



# Option 2

sin_vec = list(map(my_sine_curve, x))

plt.plot(x, sin_vec)


def my_3d_func(x, y):
    return (x**2 + y**2)**0.5


x_1 = np.random.uniform(100)
y_1 = np.random.uniform(100)



dist = list(map(my_3d_func, x, y))


# Lambda function (anonymous function)

def cube(x):
    return x**3

lamda_cube = lambda x: x**3  

lamda_sq = lambda x: x**2

  

lamda_cube(4)

print("Using lambda - ", lamda_cube(40))
    
    
mf.lamda_cube(18)


# List comprehension


my_list = list(np.random.uniform(size=100))


empty_list = []
for x in my_list:
    temp = x**2
    empty_list.append(temp)


# Shortcut - list comprehension
my_modified_list = [x**2 for x in my_list]

my_modified_list_v2 = [x**2 for x in my_list if x > 0.5]



# newList = [ expression(element) for element in oldList if condition ] 

def my_func_default(c, a=6, b=8):
    return c*(a+b)


my_func_default(c=3, b=4, a=2) #Good Coding Practice


# *args ; **kwargs



# Trying to define a function which adds the arguments
def my_adder(*numbers):
    # Does addition
    
    
    temp_sum = 0
    
    for x in numbers:
        temp_sum = temp_sum + x
        
    return temp_sum
    



my_adder(1,2,3,10)
my_adder(1,2)
my_adder(1,2,10, 15, 18, 19)





x = [1,2,3,5,6,1,3,45,14]

temp = 0
for i in x:
    temp = temp + i





def my_mult(*x):
    
    temp = 1
    for i in x:
        temp = temp*i
        
    return temp



my_mult(2,5,4,6)
my_mult(2,6)


# Dictionary - Python data type

# List
a = [1, 10, 12]
b = ["Ami", "Apple", 6]
c = [1, 10 , True, False, None]



d = [True, True, False, True]

output = [1,1,0,1]



emp = []

for x in d:
    if x == True:
        emp.append(1)
    else:
        emp.append(0)




list(map(lambda x: 1 if x == True else 0, d))






# Dictionary -  key/value pair

Dict = {1:"Ami", "My_Key":6, 3:"Apple"}

print(Dict)
Dict.values()



































 









