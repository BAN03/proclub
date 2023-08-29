"""
longitud de array = N**2
ejemplo: 
N = 2
array = [
    [0,0]
    [0,0]
]

M = cantidad de movimientos maximos en la partida

input = valores de M y N,
        dos enteros para el trazo de linea del jugador

salida = puntuajes de la partida
"""

# tablero de la partida
N = [0 for x in range(int(input())**2)]

# Movimientos de la partida
M = int(input())

player1 = i%2 # 0
player2 = i%2 # 1
player1.score = player1.score + 1 # player 1 gets an extra turn, so 'i' needs to get extracted by 1
