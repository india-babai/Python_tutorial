# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 14:46:38 2023

@author: Rehana Sultana
"""
import numpy as np
import math


class classVCO: 
    
    
    
    # Initialize with freq, Ts
    def __init__(self,freq,Ts):
        self.freq = freq
        self.Ts = Ts
        self.maxCountVal = self.freq * self.Ts  # maxCountVal : Length of the period of the signal
        self.countVal = self.maxCountVal        # countVal : indicator at an instance (it changes everytime the VCOstep method is called )

     




    def VCOstep(self):
        
        
        '''
        Parameters
        ----------
        self : an object/instance of classVCO
            
        
        Returns
        -------
        edgeFlag : an instantaneous step pulse (for trigger graph it'll give 1, -1, or 0)\n
        squareGraph : 1 or 0 from the square graph at any instance                                       
        '''
        

        halfPeriod = math.floor(0.5*self.maxCountVal)   # halfPeriod : where 0's changes to 1's or vice versa
        
        
        
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
        

        
        # Resetting step (After one Cycle)
        if self.countVal == 0:# this where a new cycle starts
        
            # Period jitetr
            # randomNoise = math.floor(np.random.normal(0, 5, 1)[0])
            randomNoise = np.round(np.random.normal(0, 0.5, 1)[0],0)

            # Resetting the countval to maxvalue so that the cycle restarts + some period jitters
            self.countVal = self.maxCountVal + randomNoise
            
            
    
        return edgeFlag, squareGraph






















