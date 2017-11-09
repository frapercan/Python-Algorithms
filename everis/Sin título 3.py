arr = [i for i in range(2,9999999)]

def maximo_divisor(n):
    maximo = 0
    for i in range(2,n-2):
        if n % i == 0:
            maximo = n
    return maximo
def es_primo(n):
    for i in range(2,n):
        if(n % i==0):
            return False
        
    return True


p = arr[0]
for numero_iteraciones in range(5):
    print(p)
    if not es_primo(p):
        q = maximo_divisor(p)
        print(p)
        print(q)
        p = p/q
        p = arr[p-1]+q
        
    if es_primo(p):
        p = arr[p+1]
        
        
