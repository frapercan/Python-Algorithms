# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:41:23 2018

@author: xaxi
"""
import numpy as np

def read_file(filename):
    with open(filename, 'r') as f:
        LINE = f.readline()
        ROWS, COLUMS, FLOAT_SIZE, NUM_RIDES, BONUS, STEPS = [int(n) for n in LINE.split()]
        RIDES = []
        for n in range(NUM_RIDES):
            LINE = f.readline()
            X_SOURCE, Y_SOURCE, X_DESTINATION, Y_DESTINATION, START, FINISH = [int(n) for n in LINE.split()]
            RIDES.append([X_SOURCE, Y_SOURCE, X_DESTINATION, Y_DESTINATION, START, FINISH])
        RIDES = np.array(RIDES)
        X_SOURCES = np.reshape(RIDES[:,0],[NUM_RIDES,1])
        Y_SOURCES = np.reshape(RIDES[:,1],[NUM_RIDES,1])
        SOURCES = np.hstack([X_SOURCES,Y_SOURCES])

        X_DESTINATIONS = np.reshape(RIDES[:,2],[NUM_RIDES,1])
        Y_DESTINATIONS = np.reshape(RIDES[:,3],[NUM_RIDES,1])
        DESTINATIONS = np.hstack([X_DESTINATIONS,Y_DESTINATIONS])
        STARTS = np.reshape(RIDES[:,4],[NUM_RIDES,1])
        FINISHES = np.reshape(RIDES[:,5],[NUM_RIDES,1])
                
    return FLOAT_SIZE, NUM_RIDES, BONUS, STEPS, SOURCES,DESTINATIONS,STARTS,FINISHES      

            
            
            