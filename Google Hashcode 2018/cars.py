# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 13:54:03 2018

@author: xaxi
"""
import numpy as np
class cars(object):
    def __init__(self,FLEET_SIZE):
        self.POSITIONS = np.zeros([FLEET_SIZE,2])
        self.COMPLETED_RIDES = [[]for _ in range(FLEET_SIZE)]
        
        
    def get_positions(self):
        return self.POSITIONS
    
    def set_positions(self):
        return self.POSITIONS
    
    def add_ride(self,VEHICLE_INDEX,RIDE_INDEX):
        self.COMPLETED_RIDES[VEHICLE_INDEX].append(RIDE_INDEX)
        
#    def assign_ride(self,VEHICLE_INDEX,RIDE_INDEX):
#        self.AVALIABILITY[VEHICLE_INDEX] = 0

    def all_bussy(self):
        mask = [1 if av <= 0 else 0 for av in self.AVALIABILITY ]
#        print(mask)
        
        if any(mask):
            return False
        else:
            return True
        
    def get_position_indexes_cars_avaliable(self):
        mask = [1 if av <= 0 else 0 for av in self.AVALIABILITY ]
        
        
        
        INDEXES = [i  for i,pos in enumerate(self.AVALIABILITY) if pos <= 0 ]
        POSITIONS = self.POSITIONS[INDEXES]
#        print('tam',len(INDEXES))
        return POSITIONS,INDEXES
            
    

    
    