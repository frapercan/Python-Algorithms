def descomponer_en_potencias_de_digitos(n):
    sn = str(n)
    suma = 0
    for s in sn:
        suma += int(s)**2
        return suma



class problema_ciclos_89():
    def __init__(self):
        self.memoria = dict()
        
    def detecta_ciclos_89_o_1(self,n):
        if(n == 89):
            return 1
        if(n==1):
            return 0
        if(n in self.memoria):
            return self.memoria[n]
        return self.detecta_ciclos_89_o_1(descomponer_en_potencias_de_digitos(n))
    
    
    def cuenta_numeros_ciclos_89(self,numero_maximo):
        
        contador = 0
        for n in range(2,numero_maximo+1):
            ciclo = self.detecta_ciclos_89_o_1(n)
            self.memoria[n] = ciclo
            contador += ciclo
            
pc = problema_ciclos_89()
print(pc.cuenta_numeros_ciclos_89(50))