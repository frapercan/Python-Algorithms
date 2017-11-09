
# (>) o menor que (<).
def all_triangle_numbers(n):
    lista_triangulares = []
    for i in range(1, n + 1):   
        lista_triangulares.append((i ** 2 + i)//2)
    return lista_triangulares
numeros= all_triangle_numbers(10)

litros = 3400
deposito = 5
acc = 0
for (n,i) in zip(numeros,range(len(numeros))):
    if litros/n  < 1000:    
        litros = litros - (1000*numeros[i-1]) 
        break
    
    
    
    
    
