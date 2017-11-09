# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 01:08:39 2017

@author: xaxi
"""

import numpy as np
import pandas as pd
import datetime
class problemaRobot():
    def __init__(self,posiciones):
        self.posiciones = posiciones
        self.posicion_caja_optima = 0
        self.posición_inicial_final = 0
        self.distancia_recorrida = float('inf')
    def reparte(self):
        distancia = 0
        distancia =  self.posicion_caja_optima
        for posicion in self.posiciones:
            distancia = distancia + (2 * np.abs(posicion - self.posicion_caja_optima))
            
        distancia = distancia + self.posicion_caja_optima
        return distancia
    
    def minimiza_distancia_reparto(self):
        for posicion_caja in range(len(self.posiciones)):
            self.posicion_caja_optima = posicion_caja
            distancia = self.reparte()
            if distancia < self.distancia_recorrida:
                self.distancia_recorrida = distancia
        
    
robotito = problemaRobot([1, 3, 4, 8, 8, 10, 10, 14, 15, 16, 20, 
21, 22, 22, 23, 24, 24, 27, 31, 39
])
#robotito.minimiza_distancia_reparto()
#print('posicion caja optima')
#print(robotito.posicion_caja_optima)
#print('distancia recorrida')
#print(robotito.distancia_recorrida)


class problema_consumo_electrico():
    def __init__(self,hora_inicio,hora_fin):
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    def correr_reloj(self):
        consumo_digitos = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
        acumulador_consumo = 0
        while( self.hora_inicio  < self.hora_fin):
            segundos = format(self.hora_inicio.seconds % 60,'02d')
            minutos = format(self.hora_inicio.seconds // 60 % 60,'02d')
            horas = format(self.hora_inicio.seconds // 3600 % 24,'02d')
            #print(segundos,minutos,horas)
            acumulador_consumo +=  consumo_digitos[int(segundos[0])] + consumo_digitos[int(segundos[1])] + consumo_digitos[int(minutos[0])] + consumo_digitos[int(minutos[1])]+ consumo_digitos[int(horas[0])] + consumo_digitos[int(horas[1])]
            
            self.hora_inicio = self.hora_inicio+datetime.timedelta(seconds=1)
        return acumulador_consumo
            
reloj = problema_consumo_electrico(datetime.timedelta(),datetime.timedelta(seconds = 10))
print(reloj.correr_reloj())    
        
reloj = problema_consumo_electrico(datetime.timedelta(),datetime.timedelta(seconds = 40))
print(reloj.correr_reloj())
            
reloj = problema_consumo_electrico(datetime.timedelta(),datetime.timedelta(minutes = 14, seconds = 20))
print(reloj.correr_reloj())

reloj = problema_consumo_electrico(datetime.timedelta(),datetime.timedelta(days= 365))
print(reloj.correr_reloj())
        
                    
                        
        
        
    