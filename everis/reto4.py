# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:24:19 2017

@author: xaxi
"""
import numpy as np
matrix = [[1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0]]

matrix = np.reshape(matrix,[7,7])

matrix2 = [ [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 0]
]
matrix2 = np.reshape(matrix2,[7,7])

matrix4 = [ [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
matrix4 =  np.reshape(matrix4,[3,3])


matrix3 = [[1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1]]


matrix3 = np.reshape(matrix3,[15,15])

def recorre_camino(matriz):
    anchura = matriz.shape[0]
    altura = matriz.shape[1]
    borde = [ [i,j]  for i in range(anchura) for j in range(altura) if (i == anchura-1 or i == 0 or j == altura-1 or j == 0 ) ]
    posicion_inicial = [anchura //2 , altura //2]
    return rec(matriz,posicion_inicial,borde,[])


    
def rec(matriz,posicion,borde,recorrido):
    
    
    nuevo_recorrido = recorrido.copy()
    if matriz[posicion[0]][posicion[1]]:
        return 999999
    if posicion in borde:
        nuevo_recorrido.append(posicion)
        return len(nuevo_recorrido)
    if posicion in recorrido:
        return 99999
    
    
    
    
    nuevo_recorrido.append(posicion)
    return min(min(rec(matriz,[posicion[0]+1,posicion[1]],borde,nuevo_recorrido),rec(matriz,[posicion[0]-1,posicion[1]],borde,nuevo_recorrido)),min(rec(matriz,[posicion[0],posicion[1]+1],borde,nuevo_recorrido),rec(matriz,[posicion[0],posicion[1]-1],borde,nuevo_recorrido)))
    
print(recorre_camino(matrix3))

    
    
    