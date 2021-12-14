# The-Minion-Game
La dirección de este repositorio es la siguiente: [GitHub](https://github.com/joseluis031/The-Minion-Game.git)

El código  del juego de los miniom es el siguiente:
```def miniom_game(palabra): #creo una funcion
    marcador_Stuart = 0   #creo los marcadores de los 2 jugadores
    marcador_Kevin = 0
    vocales = 'AEIOUaeiou' # defino la variable vocales
    p = len(palabra)      # defino una variable que lo que va a hacer es leerme la palabra que introduzca
    for i in range(p):    # creo un bucle con for y range que me va a permitir contar cuantas palabras se pueden
        if palabra[i] in vocales:  #formar empezando por vocal, en esete caso se sumaria 1 punto al marcador de Kevin
            marcador_Kevin += p - i
        elif palabra[i] not in vocales: #formar empezando por consonante, en este caso se sumaria 1 punto al marcador de Stuart
            marcador_Stuart += p- i  #con esto, cada punto que se cuenta, a la vez resta una posibilidad, eso lo he realizado restandole el índice
    
    print("Stuart", marcador_Stuart)
    print("Kevin", marcador_Kevin)
    
    if marcador_Stuart > marcador_Kevin:  #utilizo condicionales para printear las posibles soluciones
        print("Stuart ha ganado por", marcador_Stuart - marcador_Kevin, "de diferencia")
    elif marcador_Kevin > marcador_Stuart:
        print("Kevin ha ganado por", marcador_Kevin - marcador_Stuart, "de diferencia")
    else:
        print("Draw")
        
if __name__ == '__main__':
    comenzar = input()
    miniom_game(comenzar)



el codigo del segundo ej es:
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
    
    
    
 ej 2 con otro codigo no me ha dado tiempo a acabarlo:
 from random import randint

def encerrada(fila,columna):
    if fila == 0 and tablero[fila + 1][columna] != '':
        fallo = True
    elif fila == 1:
        if tablero[fila + 1][columna] != '' and tablero[fila- 1][columna] != '':
            fallo = True
        else:
            fallo = False
        return fallo
    
def movimiento(fila, columna):
    if fila == 0:
        tablero[fila+1][columna] = tablero[fila][columna]
        tablero[fila][columna] = ''
    elif fila == 1:
        if tablero[fila+1][columna] != ''
            tablero[fila-1][columna] = tablero[fila][columna]
            tablero[fila][columna] = ''
        else:
           tablero[fila+1][columna] = tablero[fila][columna]
           tablero[fila][columna] = ''
    elif fila == 2:
        tablero[fila-1][columna] = tablero[fila][columna]
        tablero[fila][columna] = ''
    
def printlab(tablero):

    contador_indice = 0
    for tablero[contador_indice] in tablero:
        print(tablero[contador_indice])
        contador_indice += 1
        print("2\n")

def cambio(fila,columna):
    if fila == 0:
        fila = fila + 1
    elif fila == 1:
        if tablero[fila + 1][columna] != '':
            fila = fila - 1
        else:
            fila = fila + 1
    elif fila == 2:
        fila = fila - 1
    return fila


while True:
    tablero = [
[' ',' ',' ']
[' ',' ',' ']
[' ',' ',' ']
]

     x = randint(0,2)
     y = randint(0,2)
     z = randint(0,2)
     a = randint(0,2)
     b = randint(0,2)
     c = randint(0,2)
     d = randint(0,2)

     while x == a:
       a = randint(0,2)
     while y == b:
       b = randint(0,2)
     while z == c:
        c = randint(0,2)
#posicion de las piezas
     (tablero[x])[0] = chr(0x2656)
     (tablero[y])[1] = chr(0x2656)
     (tablero[z])[2] = chr(0x2656)
     (tablero[a])[0] = chr(0x265C)
     (tablero[b])[1] = chr(0x265C)
     (tablero[c])[2] = chr(0x265C)
     
     printlab(tablero)
     
     errorx = encerrada(x, 0)
     errory = encerrada(y, 1)
     errorz = encerrada(z, 2)
     errora = encerrada(a, 0)
     errorb = encerrada(b, 1)
     errorc = encerrada(c, 2)
     
      if errorx == True and errory == True and errorz == True:
            print("El jugador blanco no se puede mover, volvemos a crear el tablero")
        pass
    elif errora == True and errorb == True and errorc == True:
        print("El jugador negro no se puede mover, volvemos a crear el tablero")
        pass
    else:
        break

turno = randint(0, 1)
while True:
    if turno == 1:
        if errorx == False and errora == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = encerrada(a, 0)
        elif errory == False and errorb == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False and errorc == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = encerrada(c, 2)
        elif errorx == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = encerrada(a, 0)
        elif errory == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = encerrada(c, 2)
        else:
            break
        turno = 0
    elif turno == 0:
        if errora == False and errorx == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False and errory == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False and errorz == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            errorz = encerrada(z, 2)
        elif errora == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            errorc = encerrada(z, 2)
        else:
            break
        turno = 1
    printeartablero(tableroajedrez)
if errorx == True and errory == True and errorz == True:
    print("El jugador blanco no se puede mover, ha ganado el jugador negro")
elif errora == True and errorb == True and errorc == True:
    print("El jugador negro no se puede mover, ha ganado el jugador blanco")

