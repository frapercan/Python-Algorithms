# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:10:53 2018

@author: xaxi
"""
import numpy as np
class rides(object):
    def __init__(self,SOURCES,DESTINATIONS,STARTS,FINISHES):
        self.SOURCES = SOURCES 
        self.DESTINATIONS = DESTINATIONS
        self.STARTS = STARTS
        self.FINISHES = FINISHES
        self.RIDE_DISTANCES = self.calculate_ride_distances()

        
#        
#    def __rmul__(self,other):
#        return other
#    def __mul__(self,other):
#        return other
    
    def calculate_ride_distances(self):
        XY = np.abs(self.SOURCES-self.DESTINATIONS)
        return np.sum(XY,axis = 1)
   
    
    def is_empty(self):
        if len(self.SOURCES == 0):
            return True
        else:
            return False
        

        

        
        
    