#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## AIA
## Procesos de Decisión de Markov
## Dpto. de C. de la Computación e I.A. (Univ. de Sevilla)
## ===================================================================

## En esta práctica vamos a implementar algoritmos relacionados con los
## Procesos de Decisión de Markov.

import random

## Supondremos que un Proceso de Decisión de Markov (MDP, por sus siglas
## en inglés) va a ser un objeto de la siguiente clase (o mejor dicho,
## de una subclase de la siguiente clase).
    
class MDP(object):

    """La clase MDP tiene como métodos la función de recompensa
    R sobre los estados, la función A que da la lista de acciones
    aplicables a un estado, y la función T que implementa el modelo de
    transición. Para cada estado y acción aplicable al estado, la
    función T devuelve una lista de pares (ei,pi) que describe los
    posibles estados ei que se pueden obtener al aplicar la acción al
    estado, junto con la probabilidad pi de que esto ocurra. El
    constructor de la clase recibe la lista de estados posibles y el
    factor de descuento.

    En esta clase genérica, las funciones R, A y T aparecen sin
    definir. Un MDP concreto va a ser un objeto de una subclase de esta
    clase MDP, en la que se definirán de manera concreta estas tres
    funciones."""

    def __init__(self,estados,descuento):
        self.estados = estados
        self.descuento = descuento

    def R(self,estado):
        pass

    def A(self,estado):
        pass
        
    def T(self,estado,accion):
        pass
    
## ===================================================================
## Consideramos el siguiente problema:

## A lo largo de su vida, una empresa pasa por situaciones muy
## distintas, que por simplificar resumiremos en que al inicio de cada
## campaña puede estar rica o pobre, y ser conocida o desconocida.
## Para ello puede decidir en cada momento o bien invertir en
## publicidad, o bien optar por no hacer publicidad. Estas dos
## acciones no tienen siempre un resultado fijo, aunque podemos
## describirlo de manera probabilística:

## - Si la empresa es rica y conocida y no invierte en publicidad,
##   seguirá rica, pero existe un 50% de probabilidad de que se vuelva
##   desconocida. Si gasta en publicidad, con toda seguridad seguirá
##   conocida pero pasará a ser pobre.

## - Si la empresa es rica y desconocida y no gasta en publicidad,
##   seguirá desconocida, y existe un 50% de que se vuelva pobre. Si
##   gasta en publicidad, se volverá pobre, pero existe un 50% de
##   probabilidades de que se vuelva conocida.

## - Si la empresa es pobre y conocida y no invierte en publicidad,
##   pasará a ser pobre y desconocida con un 50% de probabilidad, y
##   rica y conocida en caso contrario. Si gasta en publicidad, con
##   toda seguridad seguirá en la misma situación.

## - Si la empresa es pobre y desconocida, y no invierte en
##   publicidad, seguirá en la misma situación con toda seguridad. Si
##   gasta en publicidad, seguirá pobre, pero con un 50% de
##   posibilidades pasará a ser conocida.

## Supondremos que la recompensa en una campaña en la que la empresa
## es rica es de 10, y de 0 en las que sea pobre. El objetivo es
## conseguir la mayor ganancia acumulada a lo largo del tiempo, aunque
## penalizaremos las ganancias obtenidas en campañas muy lejanas,
## introduciendo un factor de descuento de 0.9.

## ===================================================================
## Ejercicio 1
## ===================================================================
## Representar el problema anterior como un proceso de decisión de
## Markov, definiendo una clase Rica_y_Conocida, subclase de la clase
## MDP. El constructor de la clase Rica_y_Conocida sólo recibe como
## entrada el factor de descuento, el valor por defecto será 0.9. En
## la clase Rica_y_Conocida se definen los métodos de la clase MDP, R,
## A y T; según lo descrito.

class Rica_y_Conocida(MDP):
    
    def __init__(self):
        self.estados = ["rd", "rc","pd", "pc"]
        self.descuento = 0.9

    def R(self,estado):
        if (estado[0]=="r"):
            return 10
        else:
            return 0

    def A(self,estado):
        return [True, False]
        
    def T(self,estado,accion):
        opciones= {"rd" : [[("rd", 0.5), ("rc",0.5)],[("pc",1)]],
                   
                   
                   "rc":[[("rd", 0.5),("pd", 0.5)] ,[("pd", 0.5),("pc", 0.5)]],
                   
                         
                   "pc":[[("pd", 0.5), ("rc",0.5)],[("pc",1)]],
                   
                   
                   "pd":[[("pd", 1), ("pd",0.5)],[("pc",0.5)]]}
                   
        return opciones[estado][accion]
    



## ===================================================================
## En general, dado un MDP, representaremos una política para el mismo
## como un diccionario cuyas claves son los estados, y los valores las
## acciones. Una política representa una manera concreta de decidir en
## cada estado la acción (de entre las aplicables a ese estado) que ha
## de aplicarse.

## Dado un MDP, un estado de partida, y una política concreta, podemos
## generar (muestrear) una secuencia de estados por los que iríamos
## pasando si vamos aplicando las acciones que nos indica la política:
## dado un estado de la secuencia, aplicamos a ese estado la acción
## que indique la política, y obtenemos un estado siguiente de manera
## aleatoria, pero siguiendo la distribución de probabilidad que
## indica el modelo de transición dado por el método T.

## ===================================================================
## Ejercicio 2
## ===================================================================
## Definir una función "genera_secuencia_estados(mdp,pi,e,n)" que
## devuelva una secuencia de estados de longitud n, obtenida siguiendo
## el método anterior. Aquí mdp es un objeto de la clase MDP, pi es una
## política, e el estado de partida y n la longitud de la secuencia.

## Ejemplo:

## >>> mdp_ryc = Rica_y_Conocida()

## >>> pi_ahorra ={"rc":0,"rd":0,"pc":0,"pd":0}
## >>> genera_secuencia_estados(mdp_ryc, pi_ahorra, "pc", 20)
## ['PC', 'RC', 'RC', 'RC', 'RC', 'RC', 'RD', 'RD', 'RD', 'PD', 'PD',
##  'PD', 'PD', 'PD', 'PD', 'PD', 'PD', 'PD', 'PD', 'PD'] 

## >>> pi_2 = {"RC":"No publicidad","RD":"Gastar en publicidad",
##             "PC":"No publicidad","PD":"Gastar en publicidad"}
## >>> genera_secuencia_estados(ryc, pi_ahorra, "pc", 20)
## ['PC', 'PD', 'PC', 'PD', 'PD', 'PD', 'PC', 'PD', 'PD', 'PD', 'PC',
##  'RC', 'RD', 'PD', 'PC', 'RC', 'RD', 'PC', 'RC', 'RC']
def genera_secuencia_estados(mdp,pi,e,n):
    resultado=list()
    resultado.append(e)
    for i in range(n):
        print(e)
        opciones= mdp.T(e,pi[e])
        print(opciones)
        if (opciones==[]):
            return resultado
        else:
            azar=random.random()
            ac=0
            for (ea,p) in opciones:
                ac+=p
                if (azar - ac < 0):
                    e=ea
                    resultado.append(e)
                    break
    return resultado
                    
                    

    
## ===================================================================
## Dada un MDP y una secuencia de estados, valoramos dicha secuencia
## como la suma de las recompensas de los estados de la secuencia (cada
## una con el correspondiente descuento).

## ===================================================================
## Ejercicio 3
## ===================================================================
## Definir una función "valora_secuencia(seq,mdp)" que calcule la
## valoración de la secuencia.

## Ejemplos:

## >>> valora_secuencia(['PC', 'RC', 'RC', 'RC', 'RC', 'RC', 'RD',
##                       'RD', 'RD', 'PD', 'PD', 'PD', 'PD', 'PD',
##                       'PD', 'PD', 'PD', 'PD', 'PD', 'PD'],mdp_ryc) 
## 51.2579511

## >>> valora_secuencia(['PC', 'PD', 'PC', 'PD', 'PD', 'PD', 'PC',
##                       'PD', 'PD', 'PD', 'PC', 'RC', 'RD', 'PD',
##                       'PC', 'RC', 'RD', 'PC', 'RC', 'RC'],mdp_ryc) 
## 12.72613090615132

def valora_secuencia(seq,mdp):
    return sum(mdp.R(e)*(mdp.descuento**i) for i,e in enumerate(seq))
## ===================================================================
## Dada una política pi, la valoración de un estado, e, respecto de
## esa política, V^{pi}(e), se define como la media esperada de las
## valoraciones de las secuencias que se pueden generar teniendo dicho
## estado como estado de partida.

## ===================================================================
## Ejercicio 4
## ===================================================================
## Usando las funciones de los dos ejercicios anteriores, definir una
## función "estima_valor(e,pi,mdp,m,n)" que realiza una estimación
## aproximada del valor V^{pi}(e), para ello genera n secuencias de
## tamaño m, y calcula la media de sus valoraciones.

## Ejemplos:

## >>> estima_valor("PC",pi_ahorra,mdp_ryc,50,500)
## 14.749222185826712
## >>> estima_valor("PC",pi_2,mdp_ryc,50,500)
## 34.87466976285016

## >>> estima_valor("RC",pi_ahorra,mdp_ryc,60,700)
## 32.75657500158564
## >>> estima_valor("RC",pi_2,mdp_ryc,60,700)
## 50.6501047311598

def estima_valor(e,pi,mdp,m,n):
    return sum(valora_secuencia(genera_secuencia_estados(mdp,pi,e,m),mdp) for _ in range(n))/n 

## ===================================================================
## Ejercicio 5
## ===================================================================

## Usando la función anterior, estimar la valoración de cada estado
## del problema "Rica y conocida", con las siguientes políticas:

## * Aquella que sea cual sea el estado, siempre decide invertir en
##   publicidad.

## * Aquella que sea cual sea el estado, siempre decide ahorrar.

## ¿Cuál crees que es mejor? ¿Habrá alguna mejor que estas dos? ¿Cuál
## crees que sería la mejor política de todas?



## ===================================================================
## La función de valoración no se suele calcular mediante la técnica
## de muestreo vista en el ejercicio 4, sino como resultado de
## resolver un sistema de ecuaciones (ver diapositiva 74 del tema
## 2). Dicho sistema de ecuaciones se puede resolver de manera
## aproximada de manera iterativa, tal y como se explica en el tema 2.

## ===================================================================
## Ejercicio 6
## ===================================================================
## Definir una función "valoración_respecto_política(pi,mdp, n)" que
## aplica dicho método iterativo (n iteraciones) para calcular la
## valoración V^{pi}. Dicha valoración debe devolverse como un
## diccionario que a cada estado e le asocia el valor "V^{pi}(e)"
## calculado.

## Aplicar la función para calcular la valoración asociada a las dos
## políticas que se dan en el ejercicio anterior, y comparara los
## valores obtenidos con los obtenidos mediante muestreo.

def valoracion_respecto_politica(pi,mdp,k):
    R,T,gamma = mdp.R, mdp.T, mdp.descuento
    V = {e:0 for e in mdp.estados}
    #pongo _ porque me da igual el i q sea, no lo uso, solo quiero recorrer
    for _ in range(k):
        v1 = V.copy()
        for s in mdp.estados:
            print(s)
            V[s]= R(s)+gamma*sum(p*v1[s1] for (s1,p)in T(s,pi[s]))
    return V

## ###################################################################
## Los siguientes apartados se proponen como ejercicio de programación
## que contará para la evaluación de la asignatura. Se podrá entregar
## a través de la página de la asignatura, en el formulario a tal
## efecto que estará disponible junto a la ficha de alumno.
## ###################################################################
## HONESTIDAD ACADÉMICA Y COPIAS: la realización de los ejercicios es
## un trabajo personal, por lo que deben completarse por cada
## estudiante de manera individual.  La discusión y el intercambio de
## información de carácter general con los compañeros se permite (e
## incluso se recomienda), pero NO AL NIVEL DE CÓDIGO. Igualmente el
## remitir código de terceros, obtenido a través de la red o cualquier
## otro medio, se considerará plagio.

## Cualquier plagio o compartición de código que se detecte
## significará automáticamente la calificación de CERO EN LA
## ASIGNATURA para TODOS los alumnos involucrados. Por tanto a estos
## alumnos NO se les conservará, para futuras convocatorias, ninguna
## nota que hubiesen obtenido hasta el momento. Independientemente de
## otras acciones de carácter disciplinario que se pudieran tomar.
## ###################################################################

## La implementación que sigue debe hacerse de manera general, y en
## ningún caso dependiente de un MDP concreto.

## En el tema 2 se ha visto que la recompensa que se obtiene depende,
## únicamente, del estado alcanzado. En general, se puede considerar
## que la recompensa puede depender de la acción utilizada y el estado
## de anterior.

## Por ejemplo, consideremos el siguiente juego de cartas:

## Tienes una baraja de cartas con valores 2, 3 y 4 (infinitas, pero
## con el doble de 2 que del resto). El juego se inicia con una carta
## 3 sobre la mesa. Puedes elegir apostar a "superior" o
## "inferior". Una vez que has apostado se extrae una nueva carta de
## la baraja. Si has acertado; es decir, has apostado "superior"
## (resp. "inferior") y la carta es mayor (resp. menor) que la que
## había sobre la mesa ganas tantos puntos como valor tenga la nueva
## carta y vuelves a apostar. Si sale una carta del mismo valor que la
## que ya había sobre la mesa no obtienes puntos pero vuelves a
## apostar. Si fallas, el juego termina.

## ===================================================================
## Ejercicio 7
## ===================================================================

## Definir una nueva clase MDPG para los Procesos de Decisión de
## Markov que permita utilizar una función genérica de recompensa, RG,
## que dados un estado, una acción y el estado obtenido al aplicar la
## acción devuelva un valor numérico (la recompensa que se obtiene con
## ese suceso). El resto de métodos de la clase MDP (A y T) deben
## seguir comportándose de la manera descrita.

class MDPG(object):
    def __init__(self,estados,descuento):
        self.estados = estados
        self.descuento = descuento

    def RG(self,estado,accion,estadoActualizado):
        pass

    def A(self,estado):
        pass
        
    def T(self,estado,accion):
        pass

## ===================================================================
## Ejercicio 8
## ===================================================================

## Representar el juego planteado como un proceso de decisión de
## Markov, definiendo una clase Apuesta, subclase de la clase MDPG,
## cuyo constructor recibe como entrada únicamente el factor de
## descuento, y en la que se definen de manera concreta los métodos
## RG, A y T, según lo descrito.

## Ejemplo:

## >>> mdp_apuesta = Apuesta()

## >>> pi_sup = {2:1,3:1,4:1,0:1}
## >>> genera_secuencia_estados(mdp_apuesta, pi_sup, 3, 20)
## [3, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  

## >>> pi_inf = {2:0,3:0,4:0,0:0}
## >>> genera_secuencia_estados(mdp_apuesta, pi_inf, 3, 20)
## [3, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

class Apuesta(MDPG):
    
    def __init__(self, descuento = 0.9):
        self.estados = [2,3,4,0]
        self.descuento = descuento
    
    def RG(self,e,accion,ea):
        res = 0
        if(ea < e and accion == 0):
            res = ea
        if (ea > e and accion == 1):
            res = ea
        
        return res

        
  
 
            
    def A(self,estado):
        return [True,False]
        
    def T(self,estado,accion):
        
        opciones= {2 : [[(2,0.5),(0,0.5),],[(2,0.5),(3,0.25),(4,0.25)]],
                         3:[[(2,0.5),(3,0.25),(0,0.25)],[(0,0.5),(3,0.25),(4,0.25)]],
                         4:[[(2,0.5),(3,0.25),(4,0.25)],[(4,0.25),(0,0.75)]],
                         0:[[],[]]}
                   
        return opciones[estado][accion]
        
        

    
 
## ===================================================================
## El sistema de ecuaciones utilizado para aproximar de manera
## iterativa la valoración de un estado, para esta variante de
## Procesos de Decisión de Markov es el mismo. Pero falta indicar como
## se calcula R(s)

## R (s) <- sum_{s1} (P(s1| s, pi(s)) * RG(s, pi(s), s1))

## ===================================================================
## Ejercicio 9
## ===================================================================

## Definir una función "valoraciónG_respecto_política(pi,mdp, n)" que
## aplique dicho método iterativo (n iteraciones) para calcular la
## valoración V^{pi}. Dicha valoración debe devolverse como un
## diccionario que a cada estado, s, le asocia el valor "V^{pi}(s)"
## calculado.

## Aplicar la función para calcular la valoración asociada a las dos
## políticas que se dan en el ejemplo del ejercicio anterior.
def valoracion_respecto_politicaG(pi,mdpg,k):
    RG,T,gamma = mdpg.RG, mdpg.T, mdpg.descuento
    V = {e:0 for e in mdpg.estados}
    #pongo _ porque me da igual el i q sea, no lo uso, solo quiero recorrer
    for _ in range(k):
        v1 = V.copy()
        for s in mdpg.estados:
            def R(s):
                return sum(p*RG(s,pi[s],s1) for (s1,p)in T(s,pi[s]))
            V[s]= R(s)+gamma*sum(p*v1[s1] for (s1,p)in T(s,pi[s]))
    return V
    
## mdp_apuesta = Apuesta()
## pi_sup = {2:1,3:1,4:1,0:1}
## pi_inf = {2:"0",3:"0",4:"0",0:"0"}
## valoracion_respecto_politicaG(pi_sup,mdp_apuesta,50)
##    {0: 0.0, 2: 3.7096774193548385, 3: 1.2903225806451613, 4: 0.0}
## valoracion_respecto_politicaG(pi_inf,mdp_apuesta,50)
##   {0: 0.0, 2: 0.0, 3: 1.2903225806451613, 4: 2.63267429760666}
    
    
    
## ===================================================================
## Por otro lado, en el tema 2 se ha visto que la valoración de un
## estado se define como la mejor valoración que pueda tener el
## estado, respecto a todas las políticas posibles. Y la política
## óptima es aquella que en cada estado realiza la acción con la mejor
## valoración esperada (entendiendo por valoración esperada la suma de
## las valoraciones de los estados que podrían resultar al aplicar
## dicha acción, ponderadas por la probabilidad de que ocurra eso). De
## esta manera, la valoración de un estado es la valoración que la
## política óptima asigna al estado.

## Para calcular tanto la valoración de los estados, como la política
## óptima, se han visto dos algoritmos: iteración de valores e
## iteración de políticas. En este ejercicio se pide implementar el
## algoritmo de iteración de políticas.

## ===================================================================
## Ejercicio 10
## ===================================================================

## Definir una función "iteración_de_políticasG(mdp,k)" que implementa
## el algoritmo de iteración de políticas, y devuelve dos
## diccionarios, uno con la valoración de los estados y otro con la
## política óptima.

## Calcular la mejor política y su valoración con el MDPG de
## Apuesta. Comparar los resultados respecto de las valoraciones
## obtenidas con las políticas que se vieron en el ejercicios 9.   

def iteracion_de_politicasG(mdp,k):
    T = mdp.T
    pi = genera_politica_aleatoria(mdp)
    actualizada = True
    while actualizada != False:
        vpi = valoracion_respecto_politicaG(pi,mdp,k)
        actualizada = False
        for s in mdp.estados:
            lh = max(( (sum(p*vpi[s1] for (s1,p)in T(s,a)),a) ) for a in mdp.A(s))
            rh = sum(p*vpi[s1] for (s1,p)in T(s,pi[s]))
            if lh[0] > rh:
                pi[s]=lh[1]
                actualizada = True
    return pi,vpi

            
    
          
          
        
    
    
def genera_politica_aleatoria(mdp):
    estados = mdp.estados
    acciones = mdp.A
    return {e:random.choice(acciones(e)) for e in estados}
    
## mdp_apuesta = Apuesta()
## pi_opt = iteracion_de_politicasG(mdp_apuesta,30)[0]
## pi_sup = {2:1,3:1,4:1,0:1}
## pi_inf = {2:"0",3:"0",4:"0",0:"0"}
## valoracion_respecto_politicaG(pi_opt,mdp_apuesta,50)
## {0: 0.0, 2: 10.496250292123722, 3: 7.38466591711266, 4: 10.496250292123722}
## valoracion_respecto_politicaG(pi_sup,mdp_apuesta,50)
##    {0: 0.0, 2: 3.7096774193548385, 3: 1.2903225806451613, 4: 0.0}
## valoracion_respecto_politicaG(pi_inf,mdp_apuesta,50)
##   {0: 0.0, 2: 0.0, 3: 1.2903225806451613, 4: 2.63267429760666}
## devuelve_recompensas(mdp_apuesta,pi_opt,3,100)
## ===================================================================
## Ejercicio 11
## ===================================================================

## Calcular la media de los puntos obtenidos (¡ojo! no la valoración) en
## 100 partidas para cada una de las politicas consideradas; las dos del
## ejercicio 9 y la obtenida en el ejercicio 10.

def devuelve_media_puntos(mdp,pi,e,n):
    totalpuntos = 0
    for _ in range(n):
        totalpuntos = totalpuntos + devuelve_puntos(mdp,pi,e)[1]
    return totalpuntos/n
        




def devuelve_puntos(mdp,pi,e,n = 999):
    resultado=list()
    resultado.append(e)
    puntos = 0
    for i in range(n):
        opciones= mdp.T(e,pi[e]) 
        if (opciones==[]):
            return resultado,puntos
        else:
            azar=random.random()
            ac=0
            for (ea,p) in opciones:
                ac+=p
                if (azar - ac < 0):
                    puntos = puntos+ mdp.RG(e,pi[e],ea)
                    e=ea
                    resultado.append(e)
                    break 
    return resultado,puntos
## ===================================================================
## mdp_apuesta = Apuesta()
## pi_opt = iteracion_de_politicasG(mdp_apuesta,30)[0]
## pi_sup = {2:1,3:1,4:1,0:1}
## pi_inf = {2:0,3:0,4:0,0:0}
## >>> devuelve_media_puntos(mdp_apuesta,pi_opt,random.choice(list(set(mdp_apuesta.estados)-(set([0])))),100)
## 25
## >>> devuelve_media_puntos(mdp_apuesta,pi_inf,random.choice(list(set(mdp_apuesta.estados)-(set([0])))),100)
## 1
## >>> devuelve_media_puntos(mdp_apuesta,pi_sup,random.choice(list(set(mdp_apuesta.estados)-(set([0])))),100)
## 4

