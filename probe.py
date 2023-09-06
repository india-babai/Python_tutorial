# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:38:09 2023

@author: Rehana Sultana
"""

import numpy as np

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



def measureJitter(completeSignal, nominalPeriod):
    
    # Measuring periods
    periodInfo = periodCount(completeSignal)

    listOfPeriod = periodInfo[1]

    # Measuring jitter
    # Jitter : deviation from nominal period (s1.maxCountVal)


    jitter = np.array(listOfPeriod) - nominalPeriod # NOTE :  This is essentially floored random noise
    
    
    
    return jitter
































