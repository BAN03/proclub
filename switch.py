"""
El foco se prendera o apagara cuando pase por su switch

M debe ser menor a N, y al hacer los switch deben iniciar desde 2 hasta M:

Digamos por ejemplo, que el numero M introducido es 3
Primero comienza en 2, donde cada foco multiplo de 2 debera hacer switch
Despues avanza a 3, y cada foco multiplo de 3 debera hacer switch

if 0:
    switch a 1
if 1:
    switch a 0

6 focos = N
3 switch = M

instancia 1 de numero 2:
    0 1 0 1 0 1
instancia 2 de numero 3:
    0 1 1 1 0 0
"""

def switch(N, M):
    salida = [0 for i in range(N)]
    

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    if N <= 0 or M <= 0:
        print("El numero debe ser mayor a 0")
        exit()
    if N > 1000:
        print("El primer numero debe ser menor a 1000")
        exit()
    if M > N:
        print("El segundo numero debe ser menor al primero")
        exit()
        
    switch(N, M)