import random

N = 3
META = N * (N*N + 1) // 2    # 15


# Crear tablero vacío

tablero = []
i = 0
while i < N:
    fila = []
    j = 0
    while j < N:
        fila.append(0)
        j += 1
    tablero.append(fila)
    i += 1


def ya_esta(tab, numero):
    i = 0
    while i < N:
        j = 0
        while j < N:
            if tab[i][j] == numero:
                return True
            j += 1
        i += 1
    return False


def es_magico(tab):
    # filas
    i = 0
    while i < N:
        s = 0
        j = 0
        while j < N:
            s += tab[i][j]
            j += 1
        if s != META:
            return False
        i += 1

    # columnas
    j = 0
    while j < N:
        s = 0
        i = 0
        while i < N:
            s += tab[i][j]
            i += 1
        if s != META:
            return False
        j += 1

    # diagonal principal
    s = 0
    k = 0
    while k < N:
        s += tab[k][k]
        k += 1
    if s != META:
        return False

    # diagonal secundaria
    s = 0
    i = 0
    j = N - 1
    while i < N and j >= 0:
        s += tab[i][j]
        i += 1
        j -= 1
    if s != META:
        return False

    return True


def siguiente_celda(x, y):
    y += 1
    if y == N:
        return x + 1, 0
    return x, y


def resolver(x, y):
    if x == N:
        return es_magico(tablero)

    num = 1
    limite = N * N
    while num <= limite:
        if not ya_esta(tablero, num):
            tablero[x][y] = num
            nx, ny = siguiente_celda(x, y)
            if resolver(nx, ny):
                return True
            tablero[x][y] = 0
        num += 1
    return False



#  Generar ecuaciones con x

def poner_ecuaciones(tab):
    cantidad = random.randint(3, 5)

    # Un solo x para todo
    xreal = random.randint(1, 9)

    usadas = []

    k = 0
    while k < cantidad:
        fila = random.randint(0, 2)
        col = random.randint(0, 2)

        if (fila, col) in usadas:
            continue

        numero = tab[fila][col]

        # crear ecuación que use el mismo x
        if numero >= xreal:
            r = numero - xreal
            expresion = "x + " + str(r)
        else:
            r = xreal - numero
            expresion = "x - " + str(r)

        tab[fila][col] = expresion
        usadas.append((fila, col))
        k += 1

    return xreal

if resolver(0, 0):

    xcorrecto = poner_ecuaciones(tablero)

    print("Cuadrado magico")
    i = 0
    while i < N:
        print(tablero[i])
        i += 1

    # 5 intentos
    intentos = 5
    exito = False

    while intentos > 0:
        print("\nTe quedan", intentos, "intentos")
        respuesta = input("¿Cuál es el valor de x? ")

        # verificar que sea número
        if respuesta.isdigit():
            if int(respuesta) == xcorrecto:
                print("\n¡Correcto!  x =", xcorrecto)
                exito = True
                break
            else:
                print("Incorrecto.")
        else:
            print("Debes escribir un número.")

        intentos -= 1

    if not exito:
        print("\nFallaste los 5 intentos.")
        print("El valor correcto de x era:", xcorrecto)

else:
    print("NO EXISTE SOLUCIÓN")
