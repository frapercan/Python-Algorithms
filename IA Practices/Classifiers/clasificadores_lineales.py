# ==========================================================
# Ampliaciรณn de Inteligencia Artificial. Tercer curso. 
# Grado en Ingenierรญa Informรกtica - Tecnologรญas Informรกticas
# Curso 2016-17
# Trabajo prรกctico
# ===========================================================
import numpy as np
import random as rd
import ClasificadoresUtils as utils

# --------------------------------------------------------------------------
# Autor del trabajo:
#
# APELLIDOS:
# NOMBRE: 
#
# Segundo componente (si se trata de un grupo):
#
# APELLIDOS
# NOMBRE:
# ----------------------------------------------------------------------------


# *****************************************************************************
# HONESTIDAD ACADรMICA Y COPIAS: un trabajo prรกctico es un examen, por lo que
# debe realizarse de manera individual. La discusiรณn y el intercambio de
# informaciรณn de carรกcter general con los compaรฑeros se permite (e incluso se
# recomienda), pero NO AL NIVEL DE CรDIGO. Igualmente el remitir cรณdigo de
# terceros, OBTENIDO A TRAVรS DE LA RED o cualquier otro medio, se considerarรก
# plagio. 

# Cualquier plagio o comparticiรณn de cรณdigo que se detecte significarรก
# automรกticamente la calificaciรณn de CERO EN LA ASIGNATURA para TODOS los
# alumnos involucrados. Por tanto a estos alumnos NO se les conservarรก, para
# futuras convocatorias, ninguna nota que hubiesen obtenido hasta el
# momento. SIN PERJUICIO DE OTRAS MEDIDAS DE CARรCTER DISCIPLINARIO QUE SE
# PUDIERAN TOMAR.  
# *****************************************************************************


# IMPORTANTE: NO CAMBIAR EL NOMBRE NI A ESTE ARCHIVO NI A LAS CLASES Y MรTODOS
# QUE SE PIDEN

# NOTA: En este trabajo no se permite usar scikit-learn

# ====================================================
# PARTE I: MODELOS LINEALES PARA CLASIFICACIรN BINARIA
# ====================================================

# En esta primera parte se pide implementar en Python los siguientes
# clasificadores BINARIOS, todos ellos vistos en el tema 5.

# - Perceptron umbral
# - Regresiรณn logรญstica minimizando el error cuadrรกtico:
#      * Versiรณn batch
#      * Versiรณn estocรกstica (regla delta)
# - Regresiรณn logรญstica maximizando la verosimilitud:
#      * Versiรณn batch
#      * Versiรณn estocรกstica


# --------------------------------------------
# I.1. Generando conjuntos de datos aleatorios
# --------------------------------------------

# Previamente a la implementaciรณn de los clasificadores, conviene tener
# funciones que generen aleatoriamente conjuntos de datos fictรญcios. 
# En concreto, se pide implementar estas dos funciones:

# * Funciรณn genera_conjunto_de_datos_l_s(rango,dim,n_datos): 
def genera_conjunto_de_datos_l_s(rango,dim,n_datos):
    X = np.random.randint(-rango,rango+1, size=( n_datos,dim))
    W = utils.hiperPlano_aleatorio(dim)  
    Y = [1 if np.dot(x,W) > 0 else 0 for x in X]
    Y =np.array(Y)
    return X,Y
    


    
    

#   Debe devolver dos listas X e Y, generadas aleatoriamente. La lista X debe
#   tener un nรบmero total n_datos de elelemntos, siendo cada uno de ellos una
#   lista (un ejemplo) de dim componentes, con valores entre -rango y rango. El
#   conjunto Y debe tener la clasificaciรณn binaria (1 o 0) de cada ejemplo del
#   conjunto X, en el mismo orden. El conjunto de datos debe ser linealmente
#   separable.

#   SUGERENCIA: generar en primer lugar un hiperplano aleatorio (mediante sus
#   coeficientes, elegidos aleatoriamente entre -rango y rango). Luego generar
#   aleatoriamente cada ejemplo de igual manera y clasificarlo como 1 o 0
#   dependiendo del lado del hiperplano en el que se situe. Eso asegura que el
#   conjunto de datos es linealmente separable.


# * Funciรณn genera_conjunto_de_datos_n_l_s(rango,dim,size,prop_n_l_s=0.1):

#   Como la anterior, pero el conjunto de datos debe ser no linealmente
#   separable. Para ello generar el conjunto de datos con la funciรณn anterior
#   y cambiar de clase a una proporciรณn pequeรฑa del total de ejemplos (por
#   ejemplo el 10%). La proporciรณn se da con prop_n_l_s. 



def genera_conjunto_de_datos_n_l_s(rango,dim,n_datos,prop_n_l_s=0.5):
    c_datos = genera_conjunto_de_datos_l_s(rango,dim,n_datos)
    num_y_a_cambiar = int(n_datos * prop_n_l_s)
    
    lista_indices_aleatorios = rd.sample(range(n_datos),num_y_a_cambiar)
    for indice in lista_indices_aleatorios:
        if c_datos[1][indice] == 0:
            c_datos[1][indice] = 1
        else: 
            c_datos[1][indice] = 0
    
    return c_datos[0],c_datos[1]
        
    


# -----------------------------------
# I.2. Clases y mรฉtodos a implementar
# -----------------------------------

# En esta secciรณn se pide implementar cada uno de los clasificadores lineales
# mencionados al principio. Cada uno de estos clasificadores se implementa a
# travรฉs de una clase python, que ha de tener la siguiente estructura general:

class Clasificador():
    def __init__(self,clases,normalizacion=False):
        self.clases = clases
        self.normalizacion = normalizacion
        self.pesos = []
        
    def entrena(self,entr,clas_entr,n_epochs,rate=0.1,
            pesos_iniciales=None,
            rate_decay=False):
        pass
    
    def clasifica_prob(self,ej):
        pass
    
    def clasifica(self,ej):
        pass
# class NOMBRE_DEL_CLASIFICADOR():

#     def __init__(self,clases,normalizacion=False):

#          .....
         
#     def entrena(self,entr,clas_entr,n_epochs,rate=0.1,
#                 pesos_iniciales=None,
#                 rate_decay=False):

#         ......

#     def clasifica_prob(self,ej):


#         ......

#     def clasifica(self,ej):


#         ......
        

# Explicamos a continuaciรณn cada uno de estos elementos:

# * NOMBRE_DEL_CLASIFICADOR:
# --------------------------


#  Este es el nombre de la clase que implementa el clasificador. 
#  Obligatoriamente se han de usar cada uno de los siguientes
#  nombres:

#  - Perceptrรณn umbral: 
#                       Clasificador_Perceptron
#  - Regresiรณn logรญstica, minimizando L2, batch: 
#                       Clasificador_RL_L2_Batch
#  - Regresiรณn logรญstica, minimizando L2, estocรกstico: 
#                       Clasificador_RL_L2_St
#  - Regresiรณn logรญstica, maximizando verosimilitud, batch: 
#                       Clasificador_RL_ML_Batch
#  - Regresiรณn logรญstica, maximizando verosimilitud, estocรกstico: 
#                       Clasificador_RL_ML_St



# * Constructor de la clase:
# --------------------------

#  El constructor debe tener los siguientes argumentos de entrada:

#  - Una lista clases con los nombres de las clases del problema de
#    clasificaciรณn, tal y como aparecen en el conjunto de datos. 
#    Por ejemplo, en el caso del problema de las votaciones, 
#    esta lista serรญa ["republicano","democrata"]

#  - El parรกmetro normalizacion, que puede ser True o False (False por
#    defecto). Indica si los datos se tienen que normalizar, tanto para el
#    entrenamiento como para la clasificaciรณn de nuevas instancias.  La
#    normalizaciรณn es una tรฉcnica que suele ser รบtil cuando los distintos
#    atributos reflejan cantidades numรฉricas de muy distinta magnitud.
#    En ese caso, antes de entrenar se calcula la media m_i y la desviaciรณn
#    tรญpica d_i en cada componente i-esima (es decir, en cada atributo) de los
#    datos del conjunto de entrenamiento.  A continuaciรณn, y antes del
#    entrenamiento, esos datos se transforman de manera que cada componente
#    x_i se cambia por (x_i - m_i)/d_i. Esta misma transformaciรณn se realiza
#    sobre las nuevas instancias que se quieran clasificar.  NOTA: se permite
#    usar la biblioteca numpy para calcular la media, la desviaciรณn tรญpica, y
#    en general para cualquier cรกlculo matemรกtico.


class Clasificador_Perceptron(Clasificador):
    def entrena(self,entr,clas_entr,n_epochs,rate=0.1,
            pesos_iniciales=None,
            rate_decay=False):
        if pesos_iniciales == None:
            #len +1 debido a que necesitamos una entrada ficticia x0 = -1
            pesos = utils.hiperPlano_aleatorio(len(entr[0])+1),
        else:
            pesos = pesos_iniciales
        
        n = 1
        while n < n_epochs:
            if(rate_decay):
                rate_n= rate + (2/n**(1.5))
                pesos = utils.EntrenamientoDePerceptron(pesos,entr,clas_entr,rate_n)
            else:
                pesos = utils.EntrenamientoDePerceptron(pesos,entr,clas_entr,rate)
            n = n+1
        self.pesos = pesos
                   
    def clasifica(self,ej):
        ## w0 es un peso ficticio asociado a la entrada ficticia del algoritmo de entrenamiento. 
        return utils.umbral(np.dot(self.pesos[1:],ej))
                    
class Clasificador_RL_L2_Estocastico(Clasificador):
    def entrena(self,entr,clas_entr,n_epochs,rate=0.1,
            pesos_iniciales=None,
            rate_decay=False):
        if pesos_iniciales == None:
            pesos = utils.hiperPlano_aleatorio(len(entr[0]))
        else:
            pesos = pesos_iniciales            
        n = 1           
        while n < n_epochs:
            if( rate_decay ):
                rate_n= rate + (2/n**(1.5))         
                pesos = utils.ReglaDelta(pesos,entr,clas_entr,rate_n)
            else:
                pesos = utils.ReglaDelta(pesos,entr,clas_entr,rate)
            n = n+1
        self.pesos = pesos
    
    def clasifica(self,ej):
        return utils.umbral(np.dot(self.pesos,ej))
    
class Clasificador_RL_L2_Batch(Clasificador):
    def entrena(self,entr,clas_entr,n_epochs,rate=0.1,
            pesos_iniciales=None,
            rate_decay=False):
        if pesos_iniciales == None:
            pesos = utils.hiperPlano_aleatorio(len(entr[0]))
        else:
            pesos = pesos_iniciales            
        n = 1           
        while n < n_epochs:
            if( rate_decay ):
                rate_n= rate + (2/n**(1.5))         
                pesos = utils.Descenso_Gradiente(pesos,entr,clas_entr,rate_n,tipo="Minimizando_L2")
            else:
                pesos = utils.Descenso_Gradiente(pesos,entr,tipo="Minimizando_L2")
            n = n+1
        self.pesos = pesos
    
    def clasifica(self,ej):
        return utils.umbral(np.dot(self.pesos,ej))    
    
class Clasificador_RL_ML_Batch(Clasificador):
    def entrena(self,entr,clas_entr,n_epochs,rate=0.1,
            pesos_iniciales=None,
            rate_decay=False):
        if pesos_iniciales == None:
            pesos = utils.hiperPlano_aleatorio(len(entr[0]))
        else:
            pesos = pesos_iniciales            
        n = 1           
        while n < n_epochs:
            if( rate_decay ):
                rate_n= rate + (2/n**(1.5))         
                pesos = utils.Descenso_Gradiente_ML(pesos,entr,clas_entr,rate_n,tipo="Maximizando_Verosimilitud")
            else:
                pesos = utils.Descenso_Gradiente_ML(pesos,entr,clas_entr,rate,tipo="Maximizando_Verosimilitud")
            n = n+1
        self.pesos = pesos
    
    def clasifica(self,ej):
        return utils.umbral(np.dot(self.pesos,ej))   







# * Mรฉtodo entrena:
# -----------------

#  Este mรฉtodo es el que realiza el entrenamiento del clasificador. 
#  Debe calcular un conjunto de pesos, mediante el correspondiente
#  algoritmo de entrenamiento. Describimos a continuaciรณn los parรกmetros de
#  entrada:  

#  - entr y clas_entr, son los datos del conjunto de entrenamiento y su
#    clasificaciรณn, respectivamente. El primero es una lista con los ejemplos,
#    y el segundo una lista con las clasificaciones de esos ejemplos, en el
#    mismo orden. 

#  - n_epochs: nรบmero de veces que se itera sobre todo el conjunto de
#    entrenamiento.

#  - rate: si rate_decay es False, rate es la tasa de aprendizaje fija usada
#    durante todo el aprendizaje. Si rate_decay es True, rate marca una cota
#    mรญnima de la tasa de aprendizaje, como se explica a continuaciรณn. 

#  - rate_decay, indica si la tasa de aprendizaje debe disminuir a medida que
#    se van realizando actualizaciones de los pases. En concreto, si
#    rate_decay es True, la tasa de aprendizaje que se usa en cada
#    actualizaciรณn se debe de calcular con la siguiente fรณrmula:
#       rate_n= rate_0 + (2/n**(1.5)) 
#    donde n es el nรบmero de actualizaciones de pesos realizadas hasta el
#    momento, y rate_0 es la cantidad introducida en el parรกmetro rate
#    anterior.   
#
#  - pesos_iniciales: si es None, se indica que los pesos deben iniciarse
#    aleatoriamente (por ejemplo, valores aleatorios entre -1 y 1). Si no es
#    None, entonces se debe proporcionar la lista de pesos iniciales. Esto
#    puede ser รบtil para continuar el aprendizaje a partir de un aprendizaje
#    anterior, si por ejemplo se dispone de nuevos datos.    

#  NOTA: En las versiones estocรกsticas, y en el perceptrรณn umbral, en cada
#  epoch recorrer todos los ejemplos del conjunto de entrenamiento en un orden
#  aleatorio distinto cada vez.  

    
                    
        
        
        
        
        
    

# * Mรฉtodo clasifica_prob:
# ------------------------

#  El mรฉtodo que devuelve la probabilidad de pertenecer a la clase (la que se
#  ha tomado como clase 1), calculada para un nuevo ejemplo. Este mรฉtodo no es
#  necesario incluirlo para el perceptrรณn umbral.


        
# * Mรฉtodo clasifica:
# -------------------
    
#  El mรฉtodo que devuelve la clase que se predice para un nuevo ejemplo. La
#  clase debe ser una de las clases del problema (por ejemplo, "republicano" o
#  "democrata" en el problema de los votos).  


# Si el clasificador aรบn no ha sido entrenado, tanto "clasifica" como
# "clasifica_prob" deben devolver una excepciรณn del siguiente tipo:

#class ClasificadorNoEntrenado(Exception): 

#  NOTA: Se aconseja probar el funcionamiento de los clasificadores con
#  conjuntos de datos generados por las funciones del apartado anterior. 

# Ejemplo de uso:

# ------------------------------------------------------------

# Generamos un conjunto de datos linealmente separables, 
X1,Y1=genera_conjunto_de_datos_l_s(4,8,400)

# Lo partimos en dos trozos:
X1e,Y1e=X1[:300],Y1[:300]

X1t,Y1t=X1[300:],Y1[300:]

# Creamos el clasificador (perceptrรณn umbral en este caso): 
#clas_pb1=Clasificador_Perceptron([0,1])
clas_pb1=Clasificador_RL_L2_Batch([0,1])


# Lo entrenamos con elprimero de los conjuntos de datos:
clas_pb1.entrena(X1e,Y1e,100,rate_decay=False,rate=0.001)

# Clasificamos un ejemplo del otro conjunto, y lo comparamos con su clase real:
#clas_pb1.clasifica(X1t[0]),Y1t[0]
# Out[6]: (1, 1)

# Comprobamos el porcentaje de aciertos sobre todos los ejemplos de X2t
print((sum(clas_pb1.clasifica(x) == y for x,y in zip(X1t,Y1t))/len(Y1t)))
# Out[7]: 1.0

# Repetimos el experimento, pero ahora con un conjunto de datos que no es
# linealmente separable: 
#X2,Y2=genera_conjunto_de_datos_n_l_s(4,8,400,0.1)

#X2e,Y2e=X2[:300],Y2[:300]

#X2t,Y2t=X2[300:],Y2[300:]

#clas_pb2=Clasificador_Perceptron([0,1])

#clas_pb2.entrena(X2e,Y2e,200,rate_decay=True,rate=0.001)

# In [12]: clas_pb2.clasifica(X2t[0]),Y2t[0]
# Out[12]: (1, 0)

#print(sum(clas_pb2.clasifica(x) == y for x,y in zip(X2t,Y2t))/len(Y2t))
# Out[13]: 0.82
# ----------------------------------------------------------------




















    

    




# --------------------------
# I.3. Curvas de aprendizaje
# --------------------------

# Se pide mostrar mediante grรกficas la evoluciรณn del aprendizaje de los
# distintos algoritmos. En concreto, para cada clasificador usado con un
# conjunto de datos generado aleatoriamente con las funciones anteriores, las
# dos siguientes grรกficas: 

# - Una grรกfica que indique cรณmo evoluciona el porcentaje de errores que
#   comete el clasificador sobre el conjunto de entrenamiento, en cada epoch.    
# - Otra grรกfica que indique cรณmo evoluciona el error cuadrรกtico o la log
#   verosimilitud del clasificador (dependiendo de lo que se estรฉ optimizando
#   en cada proceso de entrenamiento), en cada epoch.

# Para realizar grรกficas, se recomiendo usar la biblioteca matplotlib de
# python: 

import matplotlib.pyplot as plt


# Lo que sigue es un ejemplo de uso, para realizar una grรกfica sencilla a 
# partir de una lista "errores", que por ejemplo podrรญa contener los sucesivos
# porcentajes de error que comete el clasificador, en los sucesivos epochs: 


# plt.plot(range(1,len(errores)+1),errores,marker='o')
# plt.xlabel('Epochs')
# plt.ylabel('Porcentaje de errores')
# plt.show()

# Basta con incluir un cรณdigo similar a este en el fichero python, para que en
# la terminal de Ipython se genere la correspondiente grรกfica.

# Se pide generar una serie de grรกficas que permitan explicar el
# comportamiento de los algoritmos, con las distintas opciones, y con
# conjuntos separables y no separables. Comentar la interpretaciรณn de las
# distintas grรกficas obtenidas. 

# NOTA: Para poder realizar las grรกficas, debemos modificar los
# algoritmos de entrenamiento para que ademas de realizar el cรกlculo de los
# pesos, tambiรฉn calcule las listas con los sucesivos valores (de errores, de
# verosimilitud,etc.) que vamos obteniendo en cada epoch. Esta funcionalidad
# extra puede enlentecer algo el proceso de entrenamiento y si fuera necesario
# puede quitarse una vez se realize este apartado.










# ==================================
# PARTE II: CLASIFICACIรN MULTICLASE
# ==================================

# Se pide implementar algoritmos de regresiรณn logรญstica para problemas de
# clasificaciรณn en los que hay mรกs de dos clases. Para ello, usar las dos
# siguientes aproximaciones: 

# ------------------------------------------------
# II.1 Tรฉcnica "One vs Rest" (Uno frente al Resto)
# ------------------------------------------------

#  Esta tรฉcnica construye un clasificador multiclase a partir de
#  clasificadores binarios que devuelven probabilidades (como es el caso de la
#  regresiรณn logรญstica). Para cada posible valor de clasificaciรณn, se
#  entrena un clasificador que estime cรณmo de probable es pertemecer a esa
#  clase, frente al resto. Este conjunto de clasificadores binarios se usa
#  para dar la clasificaciรณn de un ejemplo nuevo, sin mรกs que devolver la
#  clase para la que su correspondiente clasificador binario da una mayor
#  probabilidad. 

#  En concreto, se pide implementar una clase python Clasificador_RL_OvR con
#  la siguiente estructura, y que implemente el entrenamiento y la
#  clasificaciรณn como se ha explicado. 

# class Clasificador_RL_OvR():

#     def __init__(self,class_clasif,clases):

#        .....
#     def entrena(self,entr,clas_entr,n_epochs,rate=0.1,rate_decay=False):

#        .....

#     def clasifica(self,ej):

#        .....            

#  Excepto "class_clasif", los restantes parรกmetros de los mรฉtodos significan
#  lo mismo que en el apartado anterior, excepto que ahora "clases" puede ser
#  una lista con mรกs de dos elementos. El parรกmetro class_clasif es el nombre
#  de la clase que implementa el clasificador binario a partir del cual se
#  forma el clasificador multiclase.   

#  Un ejemplo de sesiรณn, con el problema del iris:

# ---------------------------------------------------------------
# In [28]: from iris import *

# In [29]: iris_clases=["Iris-setosa","Iris-virginica","Iris-versicolor"]

# Creamos el clasificador, a partir de RL binaria estocรกstico:
# In [30]: clas_rlml1=Clasificador_RL_OvR(Clasificador_RL_ML_St,iris_clases)

# Lo entrenamos: 
# In [32]: clas_rlml1.entrena(iris_entr,iris_entr_clas,100,rate_decay=True,rate=0.01)

# Clasificamos un par de ejemplos, comparรกndolo con su clase real:
# In [33]: clas_rlml1.clasifica(iris_entr[25]),iris_entr_clas[25]
# Out[33]: ('Iris-setosa', 'Iris-setosa')

# In [34]: clas_rlml1.clasifica(iris_entr[78]),iris_entr_clas[78]
# Out[34]: ('Iris-versicolor', 'Iris-versicolor')
# ----------------------------------------------------------------




# ------------------------------------------------
# II.1 Regresiรณn logรญstica con softmax 
# ------------------------------------------------


#  Se pide igualmente implementar un clasificador en python que implemente la
#  regresiรณn multinomial logรญstica mdiante softmax, tal y como se describe en
#  el tema 5, pero solo la versiรณn ESTOCรSTICA.

#  En concreto, se pide implementar una clase python Clasificador_RL_Softmax 
#  con la siguiente estructura, y que implemente el entrenamiento y la 
#  clasificaciรณn como seexplica en el tema 5:

# class Clasificador_RL_Softmax():

#     def __init__(self,clases):

#        .....
#     def entrena(self,entr,clas_entr,n_epochs,rate=0.1,rate_decay=False):

#        .....

#     def clasifica(self,ej):

#        .....            





# ===========================================
# PARTE III: APLICACIรN DE LOS CLASIFICADORES
# ===========================================

# En este apartado se pide aplicar alguno de los clasificadores implementados
# en el apartado anterior,para tratar de resolver tres problemas: el de los
# votos, el de los dรญgitos y un tercer problema que hay que buscar. 

# -------------------------------------
# III.1 Implementaciรณn del rendimiento
# -------------------------------------

# Una vez que hemos entrenado un clasificador, podemos medir su rendimiento
# sobre un conjunto de ejemplos de los que se conoce su clasificaciรณn,
# mediante el porcentaje de ejemplos clasificados correctamente. Se ide
# definir una funciรณn rendimiento(clf,X,Y) que calcula el rendimiento de
# clasificador concreto clf, sobre un conjunto de datos X cuya clasificaciรณn
# conocida viene dada por la lista Y. 
# NOTA: clf es un objeto de las clases definidas en
# los apartados anteriores, que ademรกs debe estar ya entrenado. 


# Por ejemplo (conectando con el ejemplo anterior):

# ---------------------------------------------------------
# In [36]: rendimiento(clas_rlml1,iris_entr,iris_entr_clas)
# Out[36]: 0.9666666666666667
# ---------------------------------------------------------




# ----------------------------------
# III.2 Aplicando los clasificadores
# ----------------------------------

#  Obtener un clasificador para cada uno de los siguientes problemas,
#  intentando que el rendimiento obtenido sobre un conjunto independiente de
#  ejemplos de prueba sea lo mejor posible. 

#  - Predecir el partido de un congresista en funciรณn de lo que ha votado en
#    las sucesivas votaciones, a partir de los datos en el archivo votos.py que
#    se suministra.  

#  - Predecir el dรญgito que se ha escrito a mano y que se dispone en forma de
#    imagen pixelada, a partir de los datos que estรกn en el archivo digidata.zip
#    que se suministra.  Cada imagen viene dada por 28x28 pรญxeles, y cada pixel
#    vendrรก representado por un caracter "espacio en blanco" (pixel blanco) o
#    los caracteres "+" (borde del dรญgito) o "#" (interior del dรญgito). En
#    nuestro caso trataremos ambos como un pixel negro (es decir, no
#    distinguiremos entre el borde y el interior). En cada conjunto las imรกgenes
#    vienen todas seguidas en un fichero de texto, y las clasificaciones de cada
#    imagen (es decir, el nรบmero que representan) vienen en un fichero aparte,
#    en el mismo orden. Serรก necesario, por tanto, definir funciones python que
#    lean esos ficheros y obtengan los datos en el mismo formato python en el
#    que los necesitan los algoritmos.

#  - Cualquier otro problema de clasificaciรณn (por ejemplo,
#    alguno de los que se pueden encontrar en UCI Machine Learning repository,
#    http://archive.ics.uci.edu/ml/). Tรฉngase en cuenta que el conjunto de
#    datos que se use ha de tener sus atrรญbutos numรฉricos. Sin embargo,
#    tambiรฉn es posible transformar atributos no numรฉricos en numรฉricos usando
#    la tรฉcnica conocida como "one hot encoding".   


#  Nรณtese que en cualquiera de los tres casos, consiste en encontrar el
#  clasificador adecuado, entrenado con los parรกmetros y opciones
#  adecuadas. El entrenamiento ha de realizarse sobre el conjunto de
#  entrenamiento, y el conjunto de validaciรณn se emplea para medir el
#  rendimiento obtenido con los distintas combinaciones de parรกmetros y
#  opciones con las que se experimente. Finalmente, una vez elegido la mejor
#  combinaciรณn de parรกmetros y opciones, se da el rendimiento final sobre el
#  conjunto de test. Es importante no usar el conjunto de test para decididir
#  sobre los parรกmetros, sino sรณlo para dar el rendimiento final.

#  En nuestro caso concreto, estas son las opciones y parรกmetros con los que
#  hay que experimentar: 

#  - En primer lugar, el tipo de clasificador usado (si es batch o
#    estaocรกstico, si es basado en error cuadrรกtico o en verosimilitud, si es
#    softmax o OvR,...)
#  - n_epochs: el nรบmero de epochs realizados influye en el tiempo de
#    entrenamiento y evidentemente tambiรฉn en la calidad del clasificador
#    obtenido. Con un nรบmero bajo de epochs, no hay suficiente entrenamiento,
#    pero tambiรฉn hay que decir que un nรบmero excesivo de epochs puede
#    provocar un sobreajuste no deseado. 
#  - El valor de "rate" usado. 
#  - Si se usa "rate_decay" o no.
#  - Si se usa normalizaciรณn o no. 

# Se pide describir brevemente el proceso de experimentaciรณn en cada uno de
# los casos, y finalmente dar el clasificador con el que se obtienen mejor
# rendimiento sobre el conjunto de test correspondiente.

# Por dar una referencia, se pueden obtener clasificadores para el problema de
# los votos con un rendimiento sobre el test mayor al 90%, y para los dรญgitos
# un rendimiento superior al 80%.  
