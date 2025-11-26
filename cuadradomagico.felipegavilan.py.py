#Cuadrado mágico para tableros ingresados

MAX = int(input("Ingrese tamaño del cuadrado mágico: "))

#Suma que debe tener cada linea o diagonal para que sea cuadro magico
suma_linea = MAX * (MAX*MAX + 1) // 2

#Comprueba si es valido colocar ese numero en (x,y)
def valida(tablero, valor, x, y):

    #No deja que repite numeros
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == valor:
                return False

    #Valida que la fila sea menor que la suma magica
    if sum(tablero[x]) + valor > suma_linea:
        return False

    #Valida que la columna sea menor que la suma magica
    if sum(tablero[f][y] for f in range(MAX)) + valor > suma_linea:
        return False

    #Valida la diagonal (izquierda a drerecha) para que sea menor que la suma magica
    if x == y:
        suma_diagonal = sum(tablero[i][i] for i in range(MAX)) + valor
        if suma_diagonal > suma_linea:
            return False

    #Valida la diagonal (derecha a izquierda) para que sea menor que la suma magica
    if x + y == MAX - 1:
        suma_diagonal = sum(tablero[i][MAX-1-i] for i in range(MAX)) + valor
        if suma_diagonal > suma_linea:
            return False

    return True


#Funcion que pasa a la siguiente posicion
def siguiente_posicion(x, y):
    if y < MAX - 1:
        return x, y + 1
    return x + 1, 0


#Funcion para ver si se lleno el tablero
def final(x, y):
    return x == MAX - 1 and y == MAX - 1


#Muestra el tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:2}", end=" ")
        print("")
    print("")


def resolver(tablero, x, y):
    # Si estoy en la última celda prueba todos los números
    if x == MAX:
        return True

    nx, ny = siguiente_posicion(x, y)

    for num in range(1, MAX*MAX + 1):

        if valida(tablero, num, x, y):
            tablero[x][y] = num

            #Si era la última celda → verificar completamente
            if final(x, y):
                # validar completamente filas/columnas/diagonales
                ok = True

                for i in range(MAX):
                    if sum(tablero[i]) != suma_linea:
                        ok = False
                    if sum(tablero[f][i] for f in range(MAX)) != suma_linea:
                        ok = False

                if sum(tablero[i][i] for i in range(MAX)) != suma_linea:
                    ok = False

                if sum(tablero[i][MAX-1-i] for i in range(MAX)) != suma_linea:
                    ok = False

                if ok:
                    return True

                tablero[x][y] = 0
                continue

            if resolver(tablero, nx, ny):
                return True

            # retroceder
            tablero[x][y] = 0

    return False


tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]

print(f"Suma magica debido al tablero es : {suma_linea}\n")

if resolver(tablero, 0, 0):
    print("Cuadrado magico hecho:\n")
    mostrar_tablero(tablero)
else:
    print("No existe cuadrado magico para este tamaño de tablero.")