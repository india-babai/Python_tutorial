# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 14:46:38 2023

@author: Rehana Sultana
"""

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
        #self.halfPeriod = 0
     
    def VCOstep(self):
        
        halfPeriod = math.floor(0.5*self.maxCountVal)
        
        # trigger graph logic
        if self.countVal == halfPeriod:
            edgeFlag = -1
            
        elif  self.countVal == self.maxCountVal:
            edgeFlag = 1
            
        else:
            edgeFlag = 0
            
        
        
        # Square graph logic    
        if(self.countVal > halfPeriod):
            squareGraph = 1 
        else:
            squareGraph = 0   
        
        # Decrement of countval by 1     
        self.countVal = self.countVal - 1
        
        # self.noise = self.noise + np.random.uniform(low=5, high=10, size=1)[0]
        
        # Resetting step (AFTER ONE CYCLY)
        if self.countVal == 0:# this where a new cycle starts
            halfPeriod = math.floor(0.5*self.maxCountVal)
            print(f"HALFPERIOD = {halfPeriod}") 
            randomNoise = math.floor(np.random.normal(0,0.5,1)[0])
            # halfPeriod = math.floor(0.5*self.maxCountVal)
            # print(f"HALFPERIOD = {halfPeriod}" )
            
            self.maxCountVal = self.maxCountVal + randomNoise
            self.countVal = self.maxCountVal # Resetting the countval to max value so that the cycle restarts
            # halfPeriod = math.floor(0.5*self.maxCountVal)
            # print(f"HALFPERIOD = {halfPeriod}" )
            
            # random_noise = 0
            # random_noise = math.floor(np.random.normal(0,5,1)[0])
            
            # self.countVal = m + random_noise # Resetting the countval to max value
            # self.noise = self.noise + np.random.normal(loc=0, scale=0.5, size=1)[0] #Accumulating noise
            # self.noise = self.noise + np.random.uniform(low=0, high=10,size=1)[0] #Accumulating noise
            
    
        return edgeFlag, squareGraph
    
    

     
         
