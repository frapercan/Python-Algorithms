# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 02:33:05 2017

@author: xaxipiruli
"""
import numpy as np

def umbral(x):
    return 1 if x > 0 else 0

def hiperPlano_aleatorio(dim):
    return np.random.randint(-1,2,dim)

def normaliza(vector):
    media = np.mean(vector)
    desviacion_tipica = np.std(vector)
    return [(componente-media)/desviacion_tipica for componente in vector]
    
def EntrenamientoDePerceptron(pesos,entr,clas_entr,rate):
    W = pesos
    dim = len(pesos)
    n_data = int(len(entr))
    shuffled_entr,shuffled_clas_entr = shuffle_xy(entr,clas_entr)
    
    negative_one_row = np.full((n_data,1),-1.)
    shuffled_x0_entr =np.column_stack((negative_one_row,shuffled_entr))

    
    for (vectorx,y) in zip(shuffled_x0_entr,shuffled_clas_entr):
        o = umbral( np.dot(W,vectorx) )
        for w,x,n in zip(W,vectorx,range(dim)):
            W[n] = w + rate*(y-o)*x
    return W

def shuffle_xy(x,y):
    dim = len(x[0])
    xy = np.column_stack( (x,y) )
    np.random.shuffle(xy)
    return np.hsplit(xy, np.array([dim]))
    