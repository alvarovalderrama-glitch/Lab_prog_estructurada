# Gato con arreglos (listas)
# Tablero 3x3 representado como lista de listas. IA aleatoria.

import random                                                     # Para jugadas de IA

tab = [[" " for _ in range(3)] for _ in range(3)]                 # Crea 3x3 vacío

def mostrar():                                                    # Dibuja tablero
    for i in range(3):                                            # Recorre filas
        print(" " + " | ".join(tab[i]))                           # Junta celdas
        if i<2: print("---+---+---")                              # Separador

def libre(f,c):                                                   # ¿Libre?
    return tab[f][c] == " "                                       # Comprueba

def ganador(f):                                                   # ¿Hay 3 en línea?
    lineas = []                                                   # Lista de líneas
    lineas += [tab[i] for i in range(3)]                          # Filas
    lineas += [[tab[0][j],tab[1][j],tab[2][j]] for j in range(3)] # Columnas
    lineas += [[tab[0][0],tab[1][1],tab[2][2]], [tab[0][2],tab[1][1],tab[2][0]]] # Diagonales
    return any(all(c==f for c in L) for L in lineas)              # Verifica

def lleno():                                                      # ¿Empate?
    return all(tab[i][j]!=" " for i in range(3) for j in range(3))# Sin espacios

jugador = input("Elige tu ficha (X/O): ").strip().upper() or "X"      # Ficha jugador
jugador = jugador if jugador in ("X","O") else "X"                            # Normaliza
cpu = "O" if jugador=="X" else "X"                                    # Ficha IA
turno = "jugador"                                                  # Comienza jugador
mostrar()                                                         # Dibuja

while True:                                                       # Bucle principal
    if turno=="jugador":                                           # Turno jugador
        try:                                                      # Manejo de error
            f,c = map(int, input("Tu jugada fila,columna (1-3,1-3): ").split(",")) # Lee
            f,c = f-1, c-1                                        # A índice 0
            if 0<=f<3 and 0<=c<3 and libre(f,c):                  # Valida
                tab[f][c]=jugador                                    # Coloca ficha
                mostrar()                                         # Dibuja
                if ganador(jugador): print("¡Ganaste!"); break        # Gana jugador
                turno="ia"                                        # Cambia turno
            else:
                print("Movimiento inválido.")
        except:
            print("Formato: 2,3 por ejemplo.")
    else:                                                         # Turno IA
        libres=[(i,j) for i in range(3) for j in range(3) if libre(i,j)]# Opciones
        f,c = random.choice(libres)                               # Elige al azar
        tab[f][c]=cpu                                             # Coloca
        print(f"IA juega en ({f+1},{c+1})")                       # Info
        mostrar()                                                 # Dibuja
        if ganador(cpu): print("Gana la IA."); break              # Gana IA
        turno="jugador"                                            # Vuelve
    if lleno(): print("Empate."); break                           # Empate
