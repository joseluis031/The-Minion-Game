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

