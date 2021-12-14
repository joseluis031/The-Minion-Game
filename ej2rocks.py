import math
import os
import random
import re
import sys
import pprint

#
# Complete the 'verticalRooks' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY r1
#  2. INTEGER_ARRAY r2
#

def verticalRooks(r1, r2):
    # Write your code here
    winner=''
    chess=[]
    # Construir la matriz a partir de las listas r1 y r2
    for i in range(len(r1)):
        fila = []
        for j in range(len(r1)):
            if r1[j]==i+1:
                fila.append('T1')
            elif r2[j]==i+1:
                fila.append('T2')
            else:
                fila.append(' ')
        chess.append(fila)
    pprint.pprint(chess)

    # Inicia el movimiento el jugador 2
    jugador_1 = 'T1'
    jugador_2 = 'T2'
    jugador=jugador_2
    while True:
        movimiento=False
        #pprint.pprint(chess)
        # Recorremos la matriz buscando una casilla que contenga el jugador
        for i in range(len(r1)):
            for j in range(len(r1)):
                if chess[i][j]==jugador:
                    # intentamos mover arriba o abajo (dentro del rango) a una casilla vacía
                   # print('Jugador '+jugador+' posicion('+str(i)+','+str(j)+')='+str(chess[i][j]))
                    if i-1 > 0 and chess[i-1][j]==' ':
                        #mover a la fila de arriba
                        print('el jugador '+jugador+' mueve a posicion ('+str(i-1)+','+str(j)+')')
                        chess[i-1][j]=jugador
                        chess[i][j]= ' '  #libera la casilla de la posición actual
                        movimiento = True
                        #setear el jugador al que le toca el siguiente movimiento
                        if (jugador == jugador_2):
                            jugador=jugador_1
                        else:
                            jugador=jugador_2
                        break
                    elif i+1 < len(r1) and chess[i+1][j]==' ':
                        #mover a la fila de abajo
                        print('el jugador '+jugador+' mueve a posicion ('+str(i+1)+','+str(j)+')')
                        chess[i+1][j]=jugador
                        chess[i][j]= ' ' 
                        movimiento = True
                        #setear el jugador al que le toca el siguiente movimiento
                        if (jugador == jugador_2):
                            jugador=jugador_1
                        else:
                            jugador=jugador_2
                        break
            if movimiento==True:
                break
        if movimiento==True:
            continue
        elif movimiento==False: # finaliza el recorrido
            print('No es posible realizar más movimientos al jugador '+jugador)
            if (jugador == jugador_1):
                winner = 'player-2'
            else:
                winner = 'player-1'
            break

    print('ganador '+winner)
    return winner

if __name__ == '__main__':
    fptr = open('prueba', 'w')

    t = int(input("Introduce 6 numeros separados por un enter>>").strip())
    for t_itr in range(t):
        n = int(input().strip())

        r1 = []

        for _ in range(n):
            r1_item = int(input().strip())
            r1.append(r1_item)

        r2 = []

        for _ in range(n):
            r2_item = int(input().strip())
            r2.append(r2_item)

        result = verticalRooks(r1, r2)

        fptr.write(result + '\n')

    fptr.close()
