# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:38:09 2023

@author: Rehana Sultana
"""

import numpy as np
import scipy.signal
from numpy.fft import fft
# from sklearn.linear_model import LinearRegression

def completeClockSignal(objectVCO, totlLength = 1000):
    '''

    Parameters
    ----------
    objectVCO : It must be an object of classVCO
    totlLength : Complete Length of the signal that'd be generated    

    Returns
    -------
    It returns an array of 1's and 0's with length equal to totlLength

    '''
    tt = [] # time stamp
    VCOout = [] # storing the pulse (1/0)
    count = []

    for i in range(0, totlLength, 1): 
           
        tempCountval = objectVCO.countVal
        temp = objectVCO.VCOstep()
        
        tt.append(i)
        VCOout.append(temp[1]) # Taking the square graph
        count.append(tempCountval)

    
    return VCOout



# Measurement functions

# Func:1
def periodCount(signal):
    '''
    Parameters
    ----------
    signal : Sequence of 1's and 0's
        
    
    Returns
    -------
    periodCount : number of complete cycles/period in the sequence\n
    listOfCycleLenghts  : length of each cycles in an array

    '''
    
    
    periodCount = 0
    previousValue = None
    
    
    listOfCycleLenghts = []
    cycleLength = 0
    
    
    for binaryValue in signal: # binary value means "1"
        
        if previousValue is None:
            previousValue = binaryValue #Setting the initial state of previous_value
        

        
        if previousValue == 0 and binaryValue == 1 :
            periodCount = periodCount + 1 # Transition from 0 to 1 indicates a complete cycle
            
            listOfCycleLenghts.append(cycleLength + 1)
            
            cycleLength = 0
            
            
        else:
            cycleLength = cycleLength + 1
            
            
    
        previousValue = binaryValue # Storing the previous value at the end of the for loop


    
    
    return periodCount, listOfCycleLenghts



#Func:2
def measureJitter(completeSignal, nominalPeriod):
    
    # Measuring periods
    periodInfo = periodCount(completeSignal)

    listOfPeriod = periodInfo[1]

    # Measuring jitter
    # Jitter : deviation from nominal period (s1.maxCountVal)


    jitter = np.array(listOfPeriod) - nominalPeriod # NOTE :  This is essentially floored random noise
    
    
    
    return jitter



#func:3
def measurePSD(jitter):
    
    K = fft(jitter)
    N = len(K)
    psd = np.abs(K**2 / N )
    
    return psd



#func:4
def sdJitter(psd):
    '''
    

    Parameters
    ----------
    psd : Pass an array from PSD
        DESCRIPTION.

    Returns
    -------
    sd : TYPE
        DESCRIPTION.

    '''
    
    N = len(psd)
    total_power = np.sum(psd)
    sd = np.sqrt(total_power / N)
    
    return sd

 

#func:5 => N-Period Jitter
def measNPeriod(cmpleteSignal, freq, totalLength, nomPeriod):
     
    # N = int((totalLength/freq))
    
    periodInfo = periodCount(cmpleteSignal)
    N = len(periodInfo[1])

    #listOfPeriod = periodInfo[1]
    
    sumOfAbsoluteJitters = 0

    for i in range(0, N):
        sumOfAbsoluteJitters = sumOfAbsoluteJitters + periodInfo[1][i]
        

    NPeriodJitter = N*nomPeriod - sumOfAbsoluteJitters
    K = fft(NPeriodJitter)
    
    
    psd = np.abs(K**2 / N )
    total_power = np.sum(psd)
    sd = np.sqrt(total_power / N)
    
    return NPeriodJitter, psd,sd


