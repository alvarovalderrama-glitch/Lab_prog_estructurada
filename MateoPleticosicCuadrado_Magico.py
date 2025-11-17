# tamaño del tablero
MAX = 3

# ESTE MODULO REVISA SI EL CANDIDATO ESTA EN EL TABLERO
def esta_en_tablero(tablero, candidato):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == candidato:
                return True
    return False

# revisa si el tablero esta lleno
def tablero_lleno(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0:
                return False
    return True

def es_magico(tablero, constante):
    # 1) revisar filas
    for i in range(MAX):
        suma_fila = 0
        for j in range(MAX):
            suma_fila = suma_fila + tablero[i][j]
        if suma_fila != constante:
            return False

    # 2) revisar columnas
    for j in range(MAX):
        suma_columna = 0
        for i in range(MAX):
            suma_columna = suma_columna + tablero[i][j]
        if suma_columna != constante:
            return False

    # 3) revisar diagonal principal
    suma_diag_p = 0
    for i in range(MAX):
        suma_diag_p = suma_diag_p + tablero[i][i]
    if suma_diag_p != constante:
        return False

    # 4) revisar diagonal secundaria
    suma_diag_s = 0
    for i in range(MAX):
        j = MAX - 1 - i
        suma_diag_s = suma_diag_s + tablero[i][j]
    if suma_diag_s != constante:
        return False

    # si todo bien:
    return True

# Modulo valido: solo revisa que el número no se repita en el tablero
def valido(tablero, candidato):
    if esta_en_tablero(tablero, candidato):
        return False
    else:
        return True

# modulo mostrar_tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end=" ")
        print("")
    print("")

# ----------------- MODULO SOLUCION (BACKTRACKING ITERATIVO) -----------------

def solucion(tablero):
    constante = 15

    # lista de posiciones (0,0) (0,1) ... (2,2)
    posiciones = []
    for i in range(MAX):
        for j in range(MAX):
            posiciones.append((i, j))

    n_pos = MAX * MAX          # 9 casillas
    valores = [0] * n_pos      # valor actual probado en cada casilla
    pos = 0                    # índice de casilla actual (0..8)

    while 0 <= pos < n_pos:
        x, y = posiciones[pos]
        encontrado = False

        # probar el siguiente candidato para esta casilla
        while valores[pos] < 9 and not encontrado:
            valores[pos] += 1
            candidato = valores[pos]

            # usamos el módulo valido (revisa que no se repita)
            if valido(tablero, candidato):
                tablero[x][y] = candidato
                encontrado = True

        if not encontrado:
            # no hay número posible en esta casilla → retrocedemos
            valores[pos] = 0
            tablero[x][y] = 0
            pos -= 1
            continue

        # si estamos en la última casilla, comprobamos si es mágico
        if pos == n_pos - 1:
            if es_magico(tablero, constante):
                return True      # ya tenemos el cuadrado mágico
            # si no es mágico, seguimos probando otros valores en esta casilla
            continue
        else:
            # avanzar a la siguiente casilla
            pos += 1

    # si salimos del while sin éxito
    return False

# -----------------------------------Main------------------------------------

tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]

print("Tablero Inicial")
mostrar_tablero(tablero)

if solucion(tablero):
    print("Hay solución:")
    mostrar_tablero(tablero)
else:
    print("No existe solución")
