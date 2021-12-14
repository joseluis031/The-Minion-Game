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
        else:              # si no ocurre ninguno de las 2, dejo correr el bucle(seria el empate)
            pass
    print("Stuart", marcador_Stuart)
    print("Kevin", marcador_Kevin)