# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:39:26 2023

@author: Rehana Sultana
"""


import matplotlib.pyplot as plt
import numpy as np
import os



os.chdir("D:\DS\Python Tutorial\VCO project") # Setting the folder as current working directory
os.getcwd() 


import classVCO as cv
import probe as prb
# import classVCO as cv
# import probe as prb




# Section 1 Generating a complete signal ----


# 1 Creating a classVCO object
freq = 10
Freq = freq
#TotalLength = totlLength
s1 = cv.classVCO(freq, 1) #Initializing classVCO

# Generating a complete signal with 1000 sec length based on s1 object 
CompleteSignal = prb.completeClockSignal(s1, totlLength=100000)
#TotalLength = totlLength
#plt.step(range(100000), s1CompleteSignal)





# Section 2 Measuring various parameters ----

# Measuring periods
periodInfo = prb.periodCount(CompleteSignal)

listOfPeriod = periodInfo[1]


#Measuring Jitter
jitter = prb.measureJitter(CompleteSignal, nominalPeriod=s1.maxCountVal)


#Measuring PSD of Jitter
psd = prb.measurePSD(jitter)


#Measuring SD of Jitter 
SD  = prb.sdJitter(psd)


#Measuring N-Period Jitter and other parameters of it------
NPeriodJitterInfo = prb.measNPeriod(CompleteSignal, Freq, totalLength=100000, nomPeriod=s1.maxCountVal)

NPeriodJitter = NPeriodJitterInfo[0]
psdNPeriodJitter = NPeriodJitterInfo[1]
sdNPeriodJitter = NPeriodJitterInfo[2]


plt.plot(NPeriodJitter)

plt.plot(psdNPeriodJitter)
K = np.arange(len(psdNPeriodJitter))
plt.stem(K,psdNPeriodJitter)
plt.xlabel('Freq (Hz)')
plt.ylabel('PSD [V**2/Hz]')
#plt.ylim(0, 10)

plt.plot(sdNPeriodJitter)



# Empirical verification of summary stats
meanPeriod = np.mean(listOfPeriod)
sdPeriod = np.std(listOfPeriod)

meanJitter = np.mean(jitter)
sdJitter = np.std(jitter)

sdJitterFromPSD = SD

sd1NPeriodJitter = np.std(NPeriodJitter)


print("Mean Period of Jittery Periods : ", meanPeriod)
print("SD from raw jitters data : ", sdJitter)
print("SD from PSD : ", sdJitterFromPSD)
plt.plot(psd)

K = np.arange(len(psd))
plt.stem(K,psd)
plt.xlabel('Freq (Hz)')
plt.ylabel('PSD [V**2/Hz]')
plt.ylim(0, 10)

print("SD from raw NP-jitters data : ", sd1NPeriodJitter)
print("SD from NP-PSD : ", sdNPeriodJitter)



# Rough
check = np.random.normal(0, 0.5, 10000)
checkFloor = np.floor(check)



#def measNPeriod(cmpleteSignal, freq,totalLength, nomPeriod):
    
# totalLength = 100000    
     
# N = len((totalLength/freq))
# #periodInfo = periodCount(cmpleteSignal)

# listOfPeriod = periodInfo[1]
# nomPeriod=s1.maxCountVal
    
# sumOfAbsoluteJitters = 0
# Empty_list = []

# for i in range(0, N):
#  sumOfAbsoluteJitters = sumOfAbsoluteJitters + periodInfo[1][i]
#  NPeriodJitter = N*nomPeriod - sumOfAbsoluteJitters
#  Empty_list.append(NPeriodJitter)       

# # NPeriodJitter = N*nomPeriod - sumOfAbsoluteJitters
# # Empty_list.append(NPeriodJitter)
# from numpy.fft import fft
# K = fft(Empty_list)
# O = len(K)
# psd = np.abs(K**2 / O )
# total_power = np.sum(psd)
# sd = np.sqrt(total_power / O)

# sd1NPeriodJitter = np.std(Empty_list )


# print("SD from raw NP-jitters data : ", sd1NPeriodJitter)
# print("SD from NP-PSD : ", sd)

# plt.plot(Empty_list)
# L = np.arange(len(psd))
# plt.plot(L,psd )
# #L = np.arange(len(psd))
# #L = np.arange(len(sd))
# plt.stem(L,psd)
# plt.xlabel('Freq (Hz)')
# plt.ylabel('PSD [V**2/Hz]')
# #plt.ylim(0, 10)

# plt.plot(sd)
# plt.show()


    
    #return NPeriodJitter, psd,sd




    
#totalLength = 100000    
     
# N = int((totalLength/freq))
#periodInfo = periodCount(cmpleteSignal)

listOfPeriod = periodInfo[1]
nomPeriod = s1.maxCountVal
N = len(listOfPeriod)
#K = np.logspace(-2,6,1000)


NPeriodJitter = jitter.cumsum()
plt.plot(NPeriodJitter)
# plt.xlim(0,1000)
# plt.stem(jitter)
#plt.xlim(0,100)

NPeriodJitterPSD = prb.measurePSD(NPeriodJitter)
plt.xscale("log")
plt.yscale("log")
#plt.phase_spectrum(NPeriodJitterPSD)
plt.plot(NPeriodJitterPSD)
# fig, (ax1, ax2) = plt.plot(1, 2)
# ax1.set_xscale("log")
# ax1.set_yscale("log")
# ax1.set_xlim(1e1, 1e3)
# ax1.set_ylim(1e2, 1e3)
# ax1.set_aspect(1)
# ax1.set_title("adjustable = box")
#plt.xlim(0,10)

prb.sdJitter(NPeriodJitterPSD)



t = prb.measurePSD(NPeriodJitterPSD)
rot_var = prb.sdJitter(t)

rt_Varn = np.std(NPeriodJitterPSD)

prb.sdJitter(NPeriodJitterPSD)
np.sqrt(np.std(NPeriodJitter) - np.mean(NPeriodJitter)**2)


    
sumOfAbsoluteJitters = 0
Empty_list = []

for i in range(0, N):
 sumOfAbsoluteJitters = sumOfAbsoluteJitters + periodInfo[1][i]
 NPeriodJitter = N*nomPeriod - sumOfAbsoluteJitters
 Empty_list.append(NPeriodJitter)       

# NPeriodJitter = N*nomPeriod - sumOfAbsoluteJitters
# Empty_list.append(NPeriodJitter)
from numpy.fft import fft
K = fft(Empty_list)
O = len(K)
psd = np.abs(K**2 / O )
total_power = np.sum(psd)
sd = np.sqrt(total_power / O)

sd1NPeriodJitter = np.std(Empty_list )


print("SD from raw NP-jitters data : ", rt_Varn)
print("SD from NP-PSD : ", rot_var)

plt.plot(Empty_list)

plt.plot(psd )
L = np.arange(len(psd))
#L = np.arange(len(sd))
plt.stem(L,psd)
plt.xlabel('Freq (Hz)')
plt.ylabel('PSD [V**2/Hz]')
#plt.ylim(0, 10)

plt.plot(sd)
plt.show()