"""
ordenar de manera acendente una lista de numeros y
encontrar el segundo valor impar en la lista 
"""

contador = 0
numeros = input()
numeros = sorted([int(x) for x in numeros.split()])

for i in numeros:
    if i % 2 != 0:
        contador += 1
    if contador == 2:
        segundo_numero_impar = i
        break

print(segundo_numero_impar)