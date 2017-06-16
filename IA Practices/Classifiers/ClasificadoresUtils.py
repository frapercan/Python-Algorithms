# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 02:33:05 2017

@author: xaxipiruli
"""
import math
import numpy as np
import random as rd

def umbral(x):
    return 1 if x > 0 else 0

def hiperPlano_aleatorio(dim):
    return np.array([rd.uniform(-1,1) for _ in range(dim)])

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

def sigmoide(x):
    return 1/(1+np.e**x)

def L2(pesos,entr,clas_entr):
    return sum([((y-sigmoide(np.dot(pesos,x)))**2) for (x,y) in zip(shuffle_xy(entr,clas_entr))])

def ReglaDelta(pesos,entr,clas_entr,rate):
    W = pesos
    dim = len(pesos)
    shuffled_entr,shuffled_clas_entr = shuffle_xy(entr,clas_entr)
    for (vectorx,y) in zip(shuffled_entr,shuffled_clas_entr):
        o = sigmoide( np.dot(W,vectorx) )
        for w,x,n in zip(W,vectorx,range(dim)):
            W[n] = w + (rate*(y-o)*x*o*(1-o))

    return W


#
def Descenso_Gradiente(pesos,entr,clas_entr,rate,tipo):
    W = pesos
    dim = len(pesos)
    for n in range(dim):
        if tipo == "Minimizando_L2":
            Vector_Gradiente = Genera_Vector_Gradiente_L2(n,pesos,entr,clas_entr)
        if tipo == "Maximizar_Verosimilitud":
            Vector_Gradiente = Genera_Vector_Gradiente_ML(n,pesos,entr,clas_entr)
        W[n] = W[n] - (rate*Vector_Gradiente)
    return W




def Genera_Vector_Gradiente_L2(n,pesos,entr,clas_entr):
    return -2 * sum( 
            (y - sigmoide(np.dot(vectorx,pesos) ))
                    * vectorx[n] * sigmoide(np.dot(vectorx,pesos))
                    * ( 1 - sigmoide(np.dot(vectorx,pesos  ))
                    ) for vectorx,y in zip(entr,clas_entr))
    
def Genera_Vector_Gradiente_ML(n,pesos,entr,clas_entr):
    return -sum(-vectorx[n] * math.e**(-np.dot(pesos,vectorx))/ (1 + math.e**(-np.dot(pesos,vectorx)))for vectorx,y in zip(np.where(y>0,[entr,clas_entr]),clas_entr))
    
    
    
    
    
        