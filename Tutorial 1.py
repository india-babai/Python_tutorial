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



# Complex Dot product

a = np.array([complex(0,1),2,3])
b = np.array([4, 2, 5])


np.vdot(b, a)


# Sinusoidal time series
n=1000
f = 0.2
s = np.array(list(map(lambda t: np.sin(2*np.pi*f*t), range(0,n))))
plt.plot(s)

noise_s = s + np.random.normal(size=n)
plt.plot(noise_s)



f, Pxx_den = signal.periodogram(noise_s)
plt.semilogy(f, Pxx_den)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()






# FFT ------------------------------
import matplotlib.pyplot as plt
import numpy as np



# sampling rate
sr = 2000

# sampling interval
ts = 1.0/sr

t = np.arange(0,1,ts)




freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)

plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')        # plot of the raw signal
plt.ylabel('Amplitude')

plt.show() 


# Applying FFT
from numpy.fft import fft, ifft

X = fft(x)
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T 


plt.stem(freq, 2*np.abs(X)/N, 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 10)

    
    
    
# Applying PSD ---------------------
fs = 1000.0 # 1 kHz sampling frequency
F1 = 10 # First signal component at 10 Hz
F2 = 60 # Second signal component at 60 Hz
T = 10 # 10s signal length
N0 = -10 # Noise level (dB)


import numpy as np

t = np.r_[0:T:(1/fs)] # Sample times

# Two Sine signal components at frequencies F1 and F2.
signal = np.sin(2 * F1 * np.pi * t) + np.sin(2 * F2 * np.pi * t) 

# White noise with power N0
signal += np.random.randn(len(signal)) * 10**(N0/20.0) 

plt.plot(signal)
plt.xlim(0,100)


fft_sig = fft(signal)
N = len(fft_sig)
n = np.arange(N)
freq = n/T 



plt.stem(freq, 2*np.abs(fft_sig)/N, 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 100)



import scipy.signal

# f contains the frequency components
# S is the PSD
(f, S) = scipy.signal.periodogram(signal, fs, scaling='density')



import matplotlib.pyplot as plt

plt.semilogy(f, S)
plt.ylim([1e-7, 1e2])
plt.xlim([0,100])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()





# Square wave -----------------------
from scipy import signal

import matplotlib.pyplot as plt

import numpy as np

 

# Sampling rate 1000 hz / second

t = np.linspace(0, 1, 1000, endpoint=True)

 

# Plot the square wave signal
freq = 10

plt.plot(t, signal.square(2 * np.pi * freq * t))

 

# Give a title for the square wave plot

plt.title('Sqaure wave - {} Hz sampled at 1000 Hz /second'.format(freq))

 

# Give x axis label for the square wave plot

plt.xlabel('Time')

 

# Give y axis label for the square wave plot

plt.ylabel('Amplitude')





# Square Wave via for-loop -----------

import matplotlib.pyplot as plt
import numpy as np

freq = 1000 # 1KHz i.e. 1000 cycles per sec
ts = 1 # 1 sec

# One complete cycle
n = freq * ts # total data points in one complete cycle/one complete period


# Specifications
# starting value + 1 at 1000, then 0 upto 501, -1 at 500, then 0 again 499 to 1

# time_frame=np.linspace(1, 1000)

max_count_value = n

sqare_graph = []
trigger_graph = []
counter = max_count_value

for i in np.arange(n):
    
    
    # trigger graph condition
    if(counter == max_count_value):
        trigger_graph.append(1)
    elif(counter == 0.5*max_count_value):
       trigger_graph.append(-1)
    else:
        trigger_graph.append(0)
        
    
    
    # Square graph condition
    if(counter > 0.5*max_count_value):
        sqare_graph.append(1)
    else:
        sqare_graph.append(0)
    

    counter = counter - 1
        
    
  
plt.plot(trigger_graph,marker='o', color='red')
plt.plot(sqare_graph,'--', color='blue')






# Sqaure Waves etc via Class ----------------

class my_car:
    name = "Polo"
    brand = "VW"
    
    def __init__(self, reg_no):
        self.reg_no = reg_no
    


    
Arijit = my_car("2089") # Instansiate of my_car

Monojit = my_car("2090") # Instantiate of my_car



Arijit.reg_no
Monojit.brand



# Python tutorial 26AUG2023


#############################################################
# Main topics to remember/learn in Python :
# 
#    1. Data types/ Data structure : list, array, int, float, string, tuple, dict, plot
#    2. Control flow : Branching : if-else, iteration : forloop, while etc
#    3. Functions/class : built-in functions, functions from imported module, User Defined Functions - def, lambda
# 
#    4. Interaction among 1, 2, and 3
#############################################################



# List/Array
# type - this is a very important testing function

l1 = [1, 2,"AL", True] #
l2 = ["k", 1 , l1] 

# iterator - this means you can run for-loop/while-loop through it

for x in l1: # x will go into l1 and pick up its elements one by one
    print(x)




# _______________________________________________________

length = len(l1)
my_iter= np.arange(length)


for x in my_iter:
    print(l1[x])

# LOOP - replacement of repetitions


# _______________________________________________________

# Q : write a program which will take a list as input and print the values which are integer/bool.

Input_list = [1, 10, "AK", "OOP", True, None, 19, 45] #Input list


for l in Input_list:
    if isinstance(l, int):
        print("These are int-", l)
        
    else:
        print("These are not int - ",l)

        
# Q : write a program that will take an integer as input and if it's non-prime, provide the factors.



def list_of_prime_factors(n=48):
    
    empty_list = []
    
    
    # Print the number of two's that divide n
    while n % 2 == 0:
        empty_list.append(2)
        n = n/2
        
    
    
    # n ---- n must be ODD number at this step
    
    my_list_odds = range(3, int(np.sqrt(n))+1,  2)
    
    for i in my_list_odds:
        
        while n % i == 0:
            empty_list.append(i)
            n = n/i
            
            
    
    if n > 2:
        empty_list.append(n)
    
    

    return empty_list




def is_it_a_prime(n):
    
    if len(list_of_prime_factors(n)) == 1:
        return True
        
    else:
        return False
    



Input_integer = 19

if is_it_a_prime(Input_integer):
    print("It's a prime = ", Input_integer)
    
else:
    i = 1
    empty_factors = []
    while i <= Input_integer:
        if Input_integer % i == 0:
            empty_factors.append(i)
        i = i + 1
            
        
print(empty_factors)



# Infinite loop

w = 5
while w <=10:
    print(w)
    w = w+ 1




## Python tutorial 27AUG2023

#############################################################
# Main topics to remember/learn in Python :
# 
#    1. Data types/ Data structure : list, array, int, float, string, tuple, dict, plot
#    2. Control flow : Branching : if-else, iteration : forloop, while etc
#    3. Functions/class : built-in functions, functions from imported module, User Defined Functions - def, lambda
# 
#    4. Interaction among 1, 2, and 3
#############################################################



# Q : Write a function, which takes an integer as input , and gives the Fibonacci sequence up to it.

# Fibonacci : 1, 1, 2, 3, 5, 8, 13, 21, 34, ....
# f (1) =1
#  f(2) = 1
#  f(3) = f(1) + f(2)
#  f(n) = f(n-1) + f(n-2) # recursion equation


def my_fibo(input_integer=10):
    
    empty_list = [1,1]
    
    for x in np.arange(input_integer):
        if x > 1:
            temp = empty_list[x-1] + empty_list[x-2]
            empty_list.append(temp)
        
    
    return temp
    
    
    
my_fibo(20)   
     




# PYTHON TUTORIAL 29AUG2023

#############################################################
# Main topics to remember/learn in Python :
# 
#    1. Data types/ Data structure : list, array, int, float, string, tuple, dict, plot
#    2. Control flow : Branching : if-else, iteration : forloop, while etc
#    3. Functions/class : built-in functions, functions from imported module, User Defined Functions - def, lambda
# 
#    4. Interaction among 1, 2, and 3
#############################################################




import numpy as np
# C drive  --- > numpy python script


# Defining a function
def my_func(b, a=10):
    return a+b

my_func(2,5) # Calling a function



# _____________________________CLASS__________________________________________


# defining step
class DOG: # Abstract concept

# Method defining - it's same as function but, when called from inside a class, we call it a 'Method'
    def __init__(self, name, legs=4): #this is a special method
        self.naam = name
        self.paa = legs
        
        
# 
    def color(self, col):
        self.rong = col



# def ---> methods
# self.somethhing ---> attribute of the class.



# Creating an instance of 'DOG' class - instantiate/initialize
# Volu = DOG()
 
Volu = DOG("Volu Doggy")

Golu = DOG("Golu Doggo", 4)


# Before color competetion

Volu.color("red")
Volu.rong



# After color competetion
Volu.color("Blue")
Volu.rong





# Clock


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




    

s1 = classVCO(100,1) #Initializing classVCO


tt = []
pulse = []
count = []

for i in range(0,100,1):        
    tt.append(i)
    pulse.append(s1.VCOstep())
    count.append(s1.countVal)
    
    
    # print("Time, countval , pulse : ",i, ", ", s1.countVal, ",", s1.VCOstep())

        
    
plt.plot(tt, pulse, marker='o')
 
             
      













