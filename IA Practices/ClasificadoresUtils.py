# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 02:33:05 2017

@author: xaxipiruli
"""
import numpy as np

def umbral(x):
    return 1 if x > 0 else 0

def hiperPlano_aleatorio(dim):
    return np.random.sample(dim)

def normaliza(vector):
    media = np.mean(vector)
    desviacion_tipica = np.std(vector)
    return [(componente-media)/desviacion_tipica for componente in vector]
    
def EntrenamientoDePerceptron(pesos,entr,clas_entr,rate):
    W = pesos
    w0 = W[0]
    x0 = -1
    np.delete(W,0)
    for (vectorx,y) in zip(entr,clas_entr):
        o = umbral( (w0*x0) + np.dot(pesos,vectorx) )
        w0 = w0 + rate*(y-o)*x0
        for w,x,n in zip(pesos,vectorx,range(len(pesos))):
            W[n] = w + rate*(y-o)*x
    return pesos

def shuffling_xy(x,y):
    tam = len(x)
    xy = np.column_stack( (x,y) )
    np.random.shuffle(xy)
    return np.hsplit(xy, np.array([tam-1]))
    