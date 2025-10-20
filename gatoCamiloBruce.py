import random

# Variables globales.
tablero=[" "," "," ",
         " "," "," ",
         " "," "," "]
JugadorActual='X'
ganador= None
JuegoFuncionando=True
turnos=0

#---------------------------------------------------------------

def MostrarTablero(tablero): # Tablero a usar en el juego.
    print(tablero[0]+' | '+tablero[1]+' | '+tablero[2])
    print("--+---+--")
    print(tablero[3]+' | '+tablero[4]+' | '+tablero[5])
    print("--+---+--")
    print(tablero[6]+' | '+tablero[7]+' | '+tablero[8])

#---------------------------------------------------------------

def JugadorJuega(tablero): # Función para que el jugador ponga la ficha donde desee.
    while True:
        Casilla=int(input('Ingresa un número del 1 al 9:')) # Le pide al jugador que elija la casilla en la que desee jugar
        if Casilla >= 1 and Casilla <= 9 and tablero[Casilla-1] == " ": # Verifica que la casilla elegida sea válida.
            tablero[Casilla-1]=JugadorActual # Si lo es, entonces pone la ficha ahí
            break
        else: # Si no lo es...
            print('Ese espacio no se puede ocupar.') #... Le notifica al usuario que el espacio no se puede ocupar
            MostrarTablero(tablero) # Ademas le vuelve a mostrar el tablero.

#---------------------------------------------------------------

def VerCasillas(tablero): # Función para verificar el ganador.
    global ganador
   # Verifica si hay 3 fichas iguales en las filas.
    if tablero[0] == tablero[1] == tablero[2] and tablero[1] != " ": 
        ganador=tablero[0]
        return True
    if tablero[3] == tablero[4] == tablero[5] and tablero[4] != " ":
        ganador=tablero[3]
        return True
    if tablero[6] == tablero[7] == tablero[8] and tablero[7] != " ":
        ganador=tablero[6]
        return True 
    # Verifica si hay 3 fichas iguales en las columnas.
    if tablero[0] == tablero[3] == tablero[6] and tablero[3] != " ":
        ganador=tablero[0]
        return True
    if tablero[1] == tablero[4] == tablero[7] and tablero[4] != " ":
        ganador=tablero[1]
        return True
    if tablero[2] == tablero[5] == tablero[8] and tablero[5] != " ":
        ganador=tablero[2]
        return True
    # Verifica si hay 3 fichas iguales en las diagonales.
    if tablero[0] == tablero[4] == tablero[8] and tablero[4] != " ":
        ganador=tablero[0]
        return True
    if tablero[2] == tablero[4] == tablero[6] and tablero[4] != " ":
        ganador=tablero[2]
        return True
    
def VerEmpate(tablero): # Función para verificar si hay empate
    global JuegoFuncionando
    if " " not in tablero and ganador==None: # Si no hay espacios en blanco y no hay ganador
        JuegoFuncionando=False # El juego deja de funcionar
        
def Turno(): # Función para el cambio de turnos.
    global JugadorActual, turnos
    if JugadorActual == 'X': #Si el jugador actual es X
        JugadorActual = 'O'  #Cambia a O
    else:
        JugadorActual = 'X' # Si no, entonces cambia a X
    turnos=turnos+1 #Además se suma un turno

#---------------------------------------------------------------    

def VerGanador(): #Funcion que detiene el juego al momento de haber un ganador.
    global JuegoFuncionando
    if VerCasillas(tablero): # Llama la funcion de las casillas, si se cumple alguna condicion de ahi
        JuegoFuncionando=False # Se para el juego

#---------------------------------------------------------------

def Maquina(tablero): # Función que hace que el bot/la maquina funcione.
    while JugadorActual=='O': # Mientras el jugador actual sea 'O'
        posicion=random.randint(0,8) # Se genera un numero aleatorio entre el 0 y el 8.
        if tablero[posicion]==' ': # Si el numero aleatorio generado está libre
            tablero[posicion]='O' # Se pone la ficha del contrincante
            Turno() # Y se cambia de turno.

#---------------------------------------------------------------

# CODIGO PRINCIPAL // PERMITE QUE EL JUEGO FUNCIONE.

while JuegoFuncionando and turnos<10 : # Mientras el juego siga funcionando y los turnos sean menores a 10, se llaman a las funciones
    MostrarTablero(tablero)
    VerGanador()
    VerEmpate(tablero)
    if not JuegoFuncionando: # Estos if se repiten despues de cada jugada, con el fin de verificar inmediatamente...
        break # ...si hay un ganador, si lo hay se para el juego de inmediato.
    JugadorJuega(tablero)
    VerGanador()
    VerEmpate(tablero)
    if not JuegoFuncionando: # Acá vuelve a estar presente
        break
    Turno()
    Maquina(tablero)
    VerGanador()
    VerEmpate(tablero)
    if not JuegoFuncionando: # Nuevamente.
        break
        

MostrarTablero(tablero) # FINAL, ANUNCIA GANADOR O EMPATE.
if ganador:
    print(f"El ganador es {ganador}.") # Si hay ganador, entonces se le muestra al jugador quien ganó.
elif not JuegoFuncionando and ganador==None: # Si el juego dejo de funcionar y no hubo ganador.
    print('Has empatado.') # Se le notifica al jugador que hay un empate.