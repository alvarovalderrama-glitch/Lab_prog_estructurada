# El Gato con variables (sin arreglos)
# Tablero 3x3 usando 9 variables separadas; IA elige casillas aleatorias.

import random                                       # Para jugadas aleatorias

# 9 variables que representan cada casilla (vacío = " ")
a1=a2=a3=b1=b2=b3=c1=c2=c3=" "                      # Inicializa tablero

def mostrar():                                      # Dibuja el tablero
    print(f"\n {a1} | {a2} | {a3}\n---+---+---\n {b1} | {b2} | {b3}\n---+---+---\n {c1} | {c2} | {c3}\n")

def libre(c):                                       # ¿Casilla libre?
    return globals()[c] == " "                      # Consulta variable por nombre

def jugar(c, ficha):                                # Coloca ficha en variable
    globals()[c] = ficha                            # Asigna a la variable global

def ganador(f):                                     # Comprueba líneas ganadoras
    g = lambda x: globals()[x]                      # Atajo para leer variable
    lineas = [("a1","a2","a3"),("b1","b2","b3"),("c1","c2","c3"),
              ("a1","b1","c1"),("a2","b2","c2"),("a3","b3","c3"),
              ("a1","b2","c3"),("a3","b2","c1")]
    return any(g(x)==g(y)==g(z)==f for x,y,z in lineas)  # True si hay 3 en línea

def tablero_lleno():                                # ¿Sin espacios?
    return all(globals()[v]!=" " for v in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"])

# ---- Juego ----
jugador = input("Elige tu ficha (X/O): ").strip().upper() or "X"  # Ficha jugador
jugador = "X" if jugador not in ("X","O") else jugador             # Normaliza
ia = "O" if jugador=="X" else "X"                                 # Ficha IA
turno = "jugador"                                                 # Comienza el jugador
mostrar()                                                        # Muestra vacío

while True:                                                      # Bucle principal
    if turno == "jugador":                                        # Turno jugador
        cas = input("Tu jugada (a1..c3): ").strip().lower()      # Lee casilla
        if cas in ("a1","a2","a3","b1","b2","b3","c1","c2","c3") and libre(cas):
            jugar(cas, jugador)                                   # Coloca ficha
            mostrar()                                            # Dibuja
            if ganador(jugador):                                  # ¿Ganaste?
                print("¡Ganaste!"); break
            turno = "ia"                                         # Cambia turno
        else:
            print("Casilla inválida u ocupada.")
    else:                                                        # Turno IA
        posibles = [v for v in ("a1","a2","a3","b1","b2","b3","c1","c2","c3") if libre(v)]
        cas = random.choice(posibles)                            # Toma aleatoria
        jugar(cas, ia)                                           # Coloca IA
        print(f"La IA juega en {cas.upper()}")                   # Informa jugada
        mostrar()                                                # Dibuja
        if ganador(ia):                                          # ¿Gana IA?
            print("Gana la IA."); break
        turno = "jugador"                                         # Vuelve el jugador
    if tablero_lleno():                                          # ¿Empate?
        print("Empate."); break
