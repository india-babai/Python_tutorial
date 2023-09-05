# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 11:38:09 2023

@author: Rehana Sultana
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import classVCO



def periodCount(signal):
    '''
    Parameters
    ----------
    signal : Sequence of 1's and 0's
        
    
    Returns
    -------
    T : number of complete cycles/period in the sequence

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


