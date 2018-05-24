# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:47:46 2018

@author: xaxi
"""
import numpy as np
from cars import cars
from rides import rides
import utils

EVALUATIONS_PER_STEP = 4

class SD_Problem(object):
    def __init__(self):
        self.STEPS = None
        self.STEP = None
        self.CARS = None
        self.RIDES = None
        self.REMAINING_RIDES = None
        self.AVALIABILITY = None   #Descendent time measured in steps for vehicles to be free
        
        
    def initialize(self,FILE_NAME):
        FLEET_SIZE, NUM_RIDES, BONUS, STEPS, SOURCES,DESTINATIONS,STARTS,FINISHES = utils.read_file(FILE_NAME)
#        print(SOURCES)
        self.STEPS = STEPS
        self.STEP = 0
        self.BONUS = BONUS
        self.CARS = cars(FLEET_SIZE)
        SORTED_SOURCES,SORTED_DESTINATIONS,SORTED_STARTS,SORTED_FINISHES = sort_by_starting_time(SOURCES,DESTINATIONS,STARTS,FINISHES)
        self.RIDES = rides(SORTED_SOURCES,SORTED_DESTINATIONS,SORTED_STARTS,SORTED_FINISHES)
        self.REMAINING_RIDES = [i for i in range(NUM_RIDES)]
        self.AVALIABILITY = np.array([0 for _ in range(FLEET_SIZE)]) 
        
    def start(self):
        while (self.STEP < self.STEPS):
            if self.STEP != 0 :
                self.AVALIABILITY -= 1
            if not self.all_bussy():

                FREE_VEHICLES_INDEXES = self.get_indexes_cars_avaliable()
                NUM_VEHICLES_AVALIABLE = len(FREE_VEHICLES_INDEXES)
                NUM_RIDES_REMAINING = len(self.REMAINING_RIDES)
                NUM_EVALUATIONS = min(EVALUATIONS_PER_STEP,NUM_RIDES_REMAINING)
                RIDES_INDEX = np.array(self.REMAINING_RIDES[:NUM_EVALUATIONS])
                if NUM_VEHICLES_AVALIABLE != 1:
                    SCORES_STEPS = np.array([self.get_score(FREE_VEHICLES_INDEXES[0],ride_index) for ride_index in RIDES_INDEX])
#                    print(SCORES_STEPS)
#                    SCORES = SCORES_STEPS[:,:,0]
#                    STEPS =  SCORES_STEPS[:,:,1]
#                    SCORES_STEPS = SCORES/STEPS 
                
                

            self.STEP = self.STEP+1
            
            
                    
        
    def all_bussy(self):
        mask = [1 if av <= 0 else 0 for av in self.AVALIABILITY ]        
        if any(mask):
            return False
        else:
            return True
        
    def get_indexes_cars_avaliable(self):
        INDEXES = [i  for i,pos in enumerate(self.AVALIABILITY) if pos <= 0 ]
        return INDEXES
    
    def more_rides_than_cars(self,FREE_VEHICLES_POSITION):
        return len(FREE_VEHICLES_POSITION)  <=  len(self.REMAINING_RIDES)
    
    def get_score(self,vehicle_index,ride_index):
        DISTANCE = distance(self.CARS.POSITIONS[vehicle_index],self.RIDES.SOURCES[ride_index])
        EASE = (self.RIDES.STARTS[ride_index] -self.STEP)
        RIDE_DISTANCE = self.RIDES.RIDE_DISTANCES[ride_index]
        if DISTANCE <= EASE:
            POINTS =  RIDE_DISTANCE + self.BONUS
            STEPS_NEEDED = RIDE_DISTANCE + EASE
            return POINTS,STEPS_NEEDED
        
        if EASE < DISTANCE:
            if DISTANCE + EASE < self.RIDES.FINISHES[ride_index]:
                POINTS =  RIDE_DISTANCE
                STEPS_NEEDED = RIDE_DISTANCE + DISTANCE
                return POINTS,STEPS_NEEDED
            else:
                return 0,9999
    def save_results(self):
        with open('a.out', 'w') as f:
            for rides in self.CARS.COMPLETED_RIDES:
                asigns = ""
        
                for r in rides:
                    asigns += " " + str(r)
        
                f.write(str(len(rides)) + asigns + "\n")    
            
def distance(VEHICLE_POSITION,RIDE_POSITION):
        return np.sum(abs(VEHICLE_POSITION[0] - RIDE_POSITION[0]) + abs(VEHICLE_POSITION[1] - RIDE_POSITION[1]),axis = 0)       
    
def sort_by_starting_time(SOURCES,DESTINATIONS,STARTS,FINISHES):
    ORDER = np.argsort(STARTS,axis = 0)
    NUM = len(SOURCES)
    return np.reshape(SOURCES[ORDER],[NUM,2]),np.reshape(DESTINATIONS[ORDER],[NUM,2]),np.reshape(STARTS[ORDER],[NUM,1]),np.reshape(FINISHES[ORDER],[NUM,1])



#def sort_by_ease(SOURCES,DESTINATIONS,STARTS,FINISHES): #ease - holgura
  

P = SD_Problem()    

P.initialize('b_should_be_easy.in')

#print(P.REMAINING_RIDES)
P.start()
