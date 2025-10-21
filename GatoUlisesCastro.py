import random

#Inicialización del Tablero y Variables
C1, C2, C3 = " ", " ", " "
C4, C5, C6 = " ", " ", " "
C7, C8, C9 = " ", " ", " "

INVALID, VALID = 0, 1
LAPLAY = INVALID 
WIN, WINCOMP, WINPLA = 0, 0, 0
TURNO = 0
# Función para dibujar el tablero
def dibujar_tablero():
    tablero = (
        f"este es el tablero\n"
        f"                                _{C1}_I_{C2}_I_{C3}_ \n"
        f"                                _{C4}_I_{C5}_I_{C6}_ \n"
        f"                                {C7}  I  {C8}I  {C9}"
    )
    print(tablero)

# Función para verificar si hay un ganador
def revision(f):
    
    if (C1 == f and C2 == f and C3 == f) or \
       (C4 == f and C5 == f and C6 == f) or \
       (C7 == f and C8 == f and C9 == f) or \
       (C1 == f and C4 == f and C7 == f) or \
       (C2 == f and C5 == f and C8 == f) or \
       (C3 == f and C6 == f and C9 == f) or \
       (C1 == f and C5 == f and C9 == f) or \
       (C3 == f and C5 == f and C7 == f):
        return 1
    return 0

#inicio

print("bienvenido al gato :D")
dibujar_tablero()
while True:
    print("Con que ficha jugaras: 1 para ficha X 0 para ficha O")
    try:
        FICHA_J = int(input())
        if FICHA_J == 1 or FICHA_J == 0:
            break
        else:
            print("Digito invalido. por favor intentelo de nuevo")
    except ValueError:
        print("Digito invalido. por favor intentelo de nuevo")

# Asignar fichas
if FICHA_J == 1:
    FICHAW = "X"
    FICHAM = "O"
else:
    FICHAW = "O"
    FICHAM = "X"
while True:
    print("¿Quién empieza primero? 1 para que empieces tu primero 0 para que empiece la maquina primero")
    try:
        turn = int(input())
        if turn == 1 or turn == 0:
            break
        else:
            print("Digito invalido. por favor intentelo de nuevo")
    except ValueError:
        print("Digito invalido. por favor intentelo de nuevo")
if turn == 1:
    TURNO = 1
else:
    TURNO = 0
#BUCLE PRINCIPAL DEL JUEGO
while TURNO < 9 and WIN == 0:
    if TURNO % 2 == 0: # Turno de la Máquina
        print("Turno de la máquina")
        LAPLAY = INVALID
        while LAPLAY == INVALID:
            JUGADAM = random.randint(1, 9) 
            if JUGADAM == 1 and C1 == " ":
                C1 = FICHAM
                LAPLAY = VALID
            elif JUGADAM == 2 and C2 == " ":
                C2 = FICHAM
                LAPLAY = VALID
            elif JUGADAM == 3 and C3 == " ":
                C3 = FICHAM
                LAPLAY = VALID
            elif JUGADAM == 4 and C4 == " ":
                C4 = FICHAM
                LAPLAY = VALID
            elif JUGADAM == 5 and C5 == " ":
                C5 = FICHAM
                LAPLAY = VALID
            elif JUGADAM == 6 and C6 == " ":
                C6 = FICHAM
                LAPLAY = VALID
            elif JUGADAM == 7 and C7 == " ":
                C7 = FICHAM
                LAPLAY = VALID
            elif JUGADAM == 8 and C8 == " ":
                C8 = FICHAM
                LAPLAY = VALID
            elif JUGADAM == 9 and C9 == " ":
                C9 = FICHAM
                LAPLAY = VALID
            # Si LAPLAY sigue siendo INVALID, el bucle repite la jugada
        WINCOMP = revision
        (FICHAM)
        if WINCOMP == 1:
            WIN = 1
    else: # Turno del Jugador
        print("Tu turno")
        LAPLAY = INVALID
        
        # Lógica del jugador (JUGADAW)
        while LAPLAY == INVALID:
            try:
                # El DFD tenía un bloque de selección para 1, 2... 9. Lo simplificamos pidiendo la jugada
                JUGADAW = int(input("Ingrese el número de la casilla (1-9): "))
                
                # Comprobar si la casilla está vacía y asignarla (simplificando la estructura repetitiva del DFD)
                if JUGADAW == 1 and C1 == " ":
                    C1 = FICHAW
                    LAPLAY = VALID
                elif JUGADAW == 2 and C2 == " ":
                    C2 = FICHAW
                    LAPLAY = VALID
                elif JUGADAW == 3 and C3 == " ":
                    C3 = FICHAW
                    LAPLAY = VALID
                elif JUGADAW == 4 and C4 == " ":
                    C4 = FICHAW
                    LAPLAY = VALID
                elif JUGADAW == 5 and C5 == " ":
                    C5 = FICHAW
                    LAPLAY = VALID
                elif JUGADAW == 6 and C6 == " ":
                    C6 = FICHAW
                    LAPLAY = VALID
                elif JUGADAW == 7 and C7 == " ":
                    C7 = FICHAW
                    LAPLAY = VALID
                elif JUGADAW == 8 and C8 == " ":
                    C8 = FICHAW
                    LAPLAY = VALID
                elif JUGADAW == 9 and C9 == " ":
                    C9 = FICHAW
                    LAPLAY = VALID
                else:
                    print("Este lugar ya esta ocupado, o el número no es válido (1-9)")
            except ValueError:
                print("Entrada inválida. Debe ser un número del 1 al 9.")
        WINPLA = revision(FICHAW)
        if WINPLA == 1:
            WIN = 1

    # Incrementar el turno y dibujar el tablero después de cada movimiento
    TURNO += 1
    dibujar_tablero()
    
#final del juego

if WIN == 0 and TURNO == 9: # Si WIN es 0 y se llenaron las 9 casillas
    print("FUE UN EMPATE :/")
elif WINCOMP == 1:
    print("PERDISTE D:")
elif WINPLA == 1:
    print("GANASTE :D")