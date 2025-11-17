import random

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


numeros_usados = [False] * 10   # Para 1,9

# Suma mágica fija para la matriz 3x3
suma_magica = 15


# revisa si son validas las posiciones de la matriz (se verifican las filas y columnas)
def es_valido():

    #se verifica si la suma de las filas es distinta de la suma magica definida (15)
    for f in range(3):
        if 0 not in matriz[f]:
            if sum(matriz[f]) != suma_magica:
                return False
    
    #se verifica si la suma de la columnas es distinta de la suma magica definida (15)
    for c in range(3):
        col = [matriz[0][c], matriz[1][c], matriz[2][c]]
        if 0 not in col:
            if sum(col) != suma_magica:
                return False
    
    #se verifica si la suma de la diagonal 1 es distinta de la suma magica definida (15)
    d1 = [matriz[0][0], matriz[1][1], matriz[2][2]]
    if 0 not in d1:
        if sum(d1) != suma_magica:
            return False
    
    #se verifica si la suma de la diagonal 2 es distinta de la suma magica definida (15)
    d2 = [matriz[0][2], matriz[1][1], matriz[2][0]]
    if 0 not in d2:
        if sum(d2) != suma_magica:
            return False

    return True


#se defina la funcion de backtracking
def pistas(pos):
    if pos == 9:   # si se recorre la matriz entera se devuelve True
        return True

    fila = pos // 3
    col  = pos % 3

    #se genera una lista de rango 1,9
    numeros = list(range(1, 10))
    random.shuffle(numeros)

    for num in numeros:
        if not numeros_usados[num]:
            matriz[fila][col] = num
            numeros_usados[num] = True

            if es_valido():
                if pistas(pos + 1):
                    return True

            # deshacer si no sirve
            matriz[fila][col] = 0
            numeros_usados[num] = False

    return False

print("\nquieres generar un cuadrado magico?\n")
input("presiona Enter...\n")

#se llama a la funcion
pistas(0)


for fila in matriz:
    print(fila)

print("este es tu cuadrado magico!!!")