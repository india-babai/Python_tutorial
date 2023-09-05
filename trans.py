# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:39:26 2023

@author: Rehana Sultana
"""

import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir("D:\\Project\\script") # Setting the folder as current working directory
os.getcwd() 



import classVCO as cv
import probe as prb



s1 = cv.classVCO(10,1) #Initializing classVCO



tt = []
VCOout = []
count = []

for i in range(0,100,1): 
       
    # tt.append(i)
    
    tempCountval = s1.countVal
    tempNoise = s1.noise
    temp = s1.VCOstep()
    
    
    VCOout.append(temp[1]) # Taking the square graph
    count.append(tempCountval)
    
    tt.append(i)
    
    print("Time, countval , VCOout : ",i , ", ", tempCountval, ",", temp)
   

# plt.plot(tt, VCOout, marker='o') 
plt.step(tt, VCOout)
plt.xlim(100, 300) 
plt.stem(tt, count) #marker='o')  
plt.show()






t = prb.periodCount(VCOout)

t[0]

t[1]
np.mean(t[1])
np.std(t[1])


# plt.plot(tt, VCOout, marker='o') 
plt.step(tt, VCOout)
plt.xlim(100, 300) 
plt.stem(tt, count) #marker='o')  
plt.show()