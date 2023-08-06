# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 00:49:15 2023

@author: ARIJIT
"""


# 24JUL2023

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import os
import My_List_Of_Funcs as mf

os.getcwd()
# 'D:\\DS\\Python Tutorial'

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




# 28JUL2023


#############################################################
# Main topics to remember/learn in Python :
# 
#    1. Data types/ Data structure : list, array, int, float, string, tuple, dict, plot
#    2. Control flow : if-else, forloop, while etc
#    3. Functions/class : built-in functions, functions from imported module, User Defined Functions - def, lambda
# 
#    4. Interaction among 1, 2, and 3
#############################################################





def my_sine_curve(x):
    temp = np.sin(x)
    return temp

# Computation
x = np.linspace(- np.pi, np.pi, 100) # Iterable
sin_vec = np.array(list(map(my_sine_curve, x)))

# Plot
plt.plot(x, sin_vec)
plt.plot(x+10, 0.25 + sin_vec)





def my_curve(a):
    
    # Computation
    x = np.linspace(- np.pi, np.pi, 100) # Iterable
    sin_vec = np.array(list(map(my_sine_curve, x)))

    # Plot
    plt.plot(x, a + sin_vec)
    # plt.plot(x, a + sin_vec, label= "a = " + str(a))
    # plt.legend()
    
my_curve(2)



l = np.array([1, 2, 4, 6])



for i in l:
    my_curve(a = i)
    
    plt.show()
plt.legend(l) 

   
# 07AUG2023 Tutorial - Random number generation

# Random Experiment - {a, b, c, d}
# Random variable : 
    # Discrete - Coin toss (H, T or 0, 1), die throw (1, 2, 3, ..., 6) ;
    # Continuous - range/interval ;
    
# How many random numbers should be generated ?

n = 2048 # number of samples


## Option 1 - using Size (Advanced) ----------------------
# Drawing sample from uniform distribution
y = np.random.uniform(-5, 5, size=n)


# Drawing sample from normal distribution
y2 = np.random.normal(loc=0, scale=0.01, size=n)


# plotting
plt.plot(y)
plt.show()
plt.hist(y)






plt.plot(y2)
plt.show()
plt.hist(y2)


# Drawing sample from bernoulli distribution
y3 = np.random.binomial(n=1, p=0.5, size=n)
plt.hist(y3)
plt.scatter(y3)



## Option 2 - Detailed method ----------------------
time_list = []
n = 2049

for i in range(0, n):
    time_list.append(0) # Initialization to zero
    

time_array = np.array(time_list)


# Use of np.zeroes
time_array_v2 = np.zeros(n)
 

# Looping over time array
for i in range(0, n): # 0, 1, 2, ... 2048
    # time_array_v2[i] = np.random.uniform(low=-5, high=5, size=1)
    time_array_v2[i] = np.random.normal(loc=0, scale=0.01, size=1)

time_array_v2


## Option 3 - Without initialization ----------------
time_list = []
n = 2049

for i in range(0, n):
    temp_rn = np.random.uniform(low=0, high=1, size=1)
    time_list.append(temp_rn) # Initialization to zero
    

time_array = np.array(time_list)



# @nd Step - Calculating Empirical variance/mean/sd


# Mean - for loop
empty_value = 0

for i in range(0, n):
    empty_value = empty_value + time_array[i]


# Mu formula
mu = empty_value[0]/n
print(mu) # Answer 1


# SD formula
empty_sd = 0

for i in range(0,n):
    empty_sd = empty_sd + (time_array[i] - mu)**2


sigma = ( empty_sd[0]/n )**0.5
print(sigma) # Answer 2






# y = F(voltage) # System dependent on Voltage

# F - complicated function


# Q - Input Noisy voltage
# How does the output varry?

def F(x):
    return np.sin(x)

n = 10000
random_noise = np.random.normal(loc=0, scale=0.01, size=n)
mean_voltage = 10


empty_output=[]
for i in range(0, n):
    
    temp_output = F(mean_voltage + random_noise[i])
    
    empty_output.append(temp_output)
    


# Simplest form Monte Carlo Simulation
empty_output
plt.hist(empty_output)

np.average(empty_output) #mu
np.std(empty_output) #sd




