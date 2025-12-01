n = 3 # establece el tamaño del cuadrado (matriz)
ecuacion = (n * (n**2 + 1)) // 2 # el resultado de cada linea del cuadrado

cuadrado = [[0 for _ in range(n)] for _ in range(n)] # crea el cuadrado magico


def valido(cuadrado): # establece la funcion para saber si las filas y columnas cumplen con el cuadrado
    for i in range(n):
        fila = cuadrado[i]
        if 0 not in fila and sum(fila) != ecuacion: # revisa si los numeros en la fila cumplen con la ecuacion
            return False
        col = [cuadrado[j][i] for j in range(n)]
        if 0 not in col and sum(col) != ecuacion: # revisa si los numeros de las columnas cumplen con la ecuacion
            return False

    return True

def eliminar(list, num): #establece la funcion que elimina un numero del cuadrado en caso de no ser valido
    if not list:
        return []
    primero = list[0]
    resto = eliminar(list[1:], num) # resto es el resultado de aplicar la funcion
    return resto if primero == num else [primero] + resto

def resolver(cuadrado, disponible, fila, col): # define la funcion para solucionar el cuadrado (backtracking) 
    if fila == n:
        return True 
    if col + 1 < n:
        nfila, ncol = fila, col + 1
    else:
        nfila, ncol = fila + 1, 0
    for num in disponible: # prueba cada numero disponible para el cuadrado

        cuadrado[fila][col] = num

        if valido(cuadrado): # revisa si el cuadrado actual es valido
            nuevo = eliminar(disponible, num)
            if resolver(cuadrado, nuevo, nfila, ncol):
                return True
        cuadrado[fila][col] = 0

    return False

disponibles = list(range(1, n*n + 1)) # crea una lista de los numero disponibles

if resolver(cuadrado, disponibles, 0, 0): # en caso de que el cuadrado final se muestra la solucion al cuadrado
    print("se creo el cuadrado:")
    for fila in cuadrado:
        print(fila)
else:
    print("no hay una solucion para el cuadrado.")