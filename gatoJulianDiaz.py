import random

# Celdas vacías del tablero
c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = " "

# Función para mostrar el tablero actual
def mostrar():
    print(" " + c1 + " | " + c2 + " | " + c3)
    print("---+---+---")
    print(" " + c4 + " | " + c5 + " | " + c6)
    print("---+---+---")
    print(" " + c7 + " | " + c8 + " | " + c9)

# Verifica si un símbolo ha ganado
def ganador(sim):
    if (c1 == sim and c2 == sim and c3 == sim) or        (c4 == sim and c5 == sim and c6 == sim) or        (c7 == sim and c8 == sim and c9 == sim) or        (c1 == sim and c4 == sim and c7 == sim) or        (c2 == sim and c5 == sim and c8 == sim) or        (c3 == sim and c6 == sim and c9 == sim) or        (c1 == sim and c5 == sim and c9 == sim) or        (c3 == sim and c5 == sim and c7 == sim):
        return True
    return False

# Comprueba si una posición está libre
def libre(n):
    if n == 1 and c1 == " ": return True
    if n == 2 and c2 == " ": return True
    if n == 3 and c3 == " ": return True
    if n == 4 and c4 == " ": return True
    if n == 5 and c5 == " ": return True
    if n == 6 and c6 == " ": return True
    if n == 7 and c7 == " ": return True
    if n == 8 and c8 == " ": return True
    if n == 9 and c9 == " ": return True
    return False

# Marca una posición con X u O
def marcar(n, sim):
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
    if n == 1: c1 = sim
    elif n == 2: c2 = sim
    elif n == 3: c3 = sim
    elif n == 4: c4 = sim
    elif n == 5: c5 = sim
    elif n == 6: c6 = sim
    elif n == 7: c7 = sim
    elif n == 8: c8 = sim
    elif n == 9: c9 = sim

# Asigna símbolos y primer turno aleatorio
if random.randint(0,1) == 0:
    humano = "X"
    maquina = "O"
else:
    humano = "O"
    maquina = "X"

turno = "humano" if random.randint(0,1) == 0 else "maquina"

# Indica quien empieza y con que simbolo

print("Tú eres:", humano)
print("La máquina es:", maquina)
print("Empieza:", turno)
print("Guía:\n 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9")

# Ciclo del juego
jugadas = 0
fin = False
while not fin:
    mostrar()
    if turno == "humano":
        valido = False
        while not valido:
            pos = input("Elige posición (1-9): ")
            if pos.isdigit():
                n = int(pos)
                if n >= 1 and n <= 9 and libre(n):
                    valido = True
        marcar(n, humano)
        jugadas += 1
        if ganador(humano):
            mostrar()
            print("¡Ganaste!")
            fin = True
        elif jugadas == 9:
            mostrar()
            print("Empate.")
            fin = True
        else:
            turno = "maquina"
    else:
        elegido = False
        while not elegido:
            n = random.randint(1,9)
            if libre(n):
                elegido = True
        print("La máquina juega en", n)
        marcar(n, maquina)
        jugadas += 1
        if ganador(maquina):
            mostrar()
            print("La máquina gana.")
            fin = True
        elif jugadas == 9:
            mostrar()
            print("Empate.")
            fin = True
        else:
            turno = "humano"
