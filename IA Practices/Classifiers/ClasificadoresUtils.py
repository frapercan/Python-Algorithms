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
    print('pesos',pesos)
    W = pesos
    print('W',W)
    dim = len(pesos)
    n_data = len(entr)
    print('entr',entr)
    print('class_entr',clas_entr)
    
    
    
    shuffled_entr,shuffled_clas_entr = shuffling_xy(entr,clas_entr)
    print('shuffled_entr',shuffled_entr)
    print('shuffled_class',shuffled_clas_entr)
    negative_one_row = np.full((n_data,1),-1)
    print(negative_one_row)
    shuffled_x0_entr =np.column_stack((negative_one_row,shuffled_entr))
    print(shuffled_x0_entr)
    
    for (vectorx,y) in zip(shuffled_x0_entr,shuffled_clas_entr):
        o = umbral( np.dot(pesos,vectorx) )
        for w,x,n in zip(W,vectorx,range(dim)):
            W[n] = w + rate*(y-o)*x
    return W

def shuffling_xy(x,y):
    tam = len(x)
    xy = np.column_stack( (x,y) )
    np.random.shuffle(xy)
    return np.hsplit(xy, np.array([tam-1]))
    