# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 02:16:25 2017

@author: xaxipiruli
"""
import numpy as np
x = [[-1,1,-1,1,1,1,-1,-1,-1,1,0,1,1,1,-1,1],
            [-1,1,-1,1,1,1,-1,-1,-1,-1,-1,1,1,1,-1,0],
            [0,1,1,0,1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1]]
y = [1,2,3]
resultado = np.column_stack( (x,y) )
np.random.shuffle(resultado)
xp = np.hsplit(resultado, np.array([16]))
yp = resultado[len(resultado):]