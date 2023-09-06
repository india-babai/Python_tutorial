# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:39:26 2023

@author: Rehana Sultana
"""


import matplotlib.pyplot as plt
import numpy as np
import os



os.chdir("D:\\DS\\Python Tutorial\\VCO project") # Setting the folder as current working directory
os.getcwd() 



import classVCO as cv
import probe as prb





# Section 1 Generating a complete signal ----


# 1 Creating a classVCO object
freq = 10
s1 = cv.classVCO(freq, 1) #Initializing classVCO

# Generating a complete signal with 1000 sec length based on s1 object 
s1CompleteSignal = prb.completeClockSignal(s1, totlLength=100000)
plt.step(range(1000), s1CompleteSignal)





# Section 2 Measuring various parameters ----

# Measuring periods
periodInfo = prb.periodCount(s1CompleteSignal)

listOfPeriod = periodInfo[1]


s1jitter = prb.measureJitter(s1CompleteSignal, nominalPeriod=s1.maxCountVal)








plt.hist(s1jitter)



# Empirical verification of summary stats
meanPeriod = np.mean(listOfPeriod)
sdPeriod = np.std(listOfPeriod)


meanJitter = np.mean(s1jitter)
sdPeriod = np.std(s1jitter)



# Rough
check = np.random.normal(0, 0.5, 100000)
checkFloor = np.floor(check)



plt.stem()