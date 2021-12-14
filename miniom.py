def miniom_game(palabra): #creo una funcion
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