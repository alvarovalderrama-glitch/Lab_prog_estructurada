###============Cubo/Cuadrado-Mágico============###

# Asignación de variables.
n = int(input("Ingresa el tamaño que quieres que sea la matriz (nxn). \n> "))
tablero = [[0 for _ in range(n)] for _ in range(n)]
num_cas = set(range(1, n*n + 1)) # Contiene los números que aún no se usan, donde el set va a permitir poder evitar repetición y eliminar rápido los que ya fueron usados.
sumatoria = (n * (n**2 + 1)) // 2 # Fórmula que permite saber la cantidad que deberian sumar las filas, columnas y diagonales.

# Función que permite ver el tablero que se creó.
def mostrar_tablero(tablero):
    for i in range(n):
        for j in range (n):
            print(f"{tablero[i][j]:3}", end = " ")
        print("")
    print("")

# Función para probar combinaciones en el tablero hasta que se encuentre una la cual cumpla las condiciones (Esto se verifica en la siguiente función) de un cubo/cuadrado mágico.
# Usando recursividad se lográ ir probando diferentes tableros hasta hallar el que cumpla con ser un cubo/cuadrado mágico.
def backtracking(tablero, num_cas, sumatoria, fila, col):
    
    if fila == n: # Ve que el tablero esté lleno y nos indica que es la solución.
        return True
    
    # Va recorriendo las columnas y después cambia de fila, hasta recorrer todo el tablero.
    sig_fila = fila 
    sig_col = col + 1
    if sig_col == n:
        sig_col = 0 
        sig_fila = fila + 1

    # Prueba con los números que quedan disponibles.
    for i in num_cas:
        tablero[fila][col] = i # Coloca el número en una casilla.
        if valido(tablero, fila, col, sumatoria) == True: # Si es válido, mantiene el número y se ejecuta lo que esta en su interior.
            num_cas_aux = num_cas - {i} # Se crea un nuevo "set" que servirá como auxiliar.

            # Llama a la siguiente casilla.
            if backtracking(tablero, num_cas_aux, sumatoria, sig_fila, sig_col) == True:
                return True
        
        # En caso de que no era válido el número se elimina modificandolo con un 0.
        tablero[fila][col] = 0 

    # No se encontró la solución, por lo que retrocede.
    return False

# Función que permite validar que el tablero generado es realmente un cubo/cuadrado mágico.
def valido(tablero, fila, col, sumatoria):
    
    #====Verifica la suma de las filas y las columnas====#
    suma_fila = sum(tablero[fila][i] for i in range(n))
    suma_col = sum(tablero[i][col] for i in range(n)) # Es una forma más compacta, pero se puede escribir también como un for y (suma_col += tablero[i][col]).

    #====Verifica la suma de las diagonales====#
    suma_diag1 = sum(tablero[i][i] for i in range(n))
    suma_diag2 = sum(tablero[i][n-1-i] for i in range(n))

    #====Verifica filas====#
    if suma_fila > sumatoria:
        return False # No cumple la condición, por lo que no nos sirve para el cubo/cuadrado mágico.
    
    # Que la fila no este vacía y que su suma sea distinto del valor de la sumatoria.
    if 0 not in tablero[fila] and suma_fila != sumatoria:
        return False
    
    #====Verifica columnas====#
    # Similar a lo anterior visto en la verificación de las filas.
    if suma_col > sumatoria:
        return False 
    col_actual = [tablero[i][col] for i in range(n)]
    if 0 not in col_actual and suma_col != sumatoria:
        return False
    
    #====Verifica diagonal principal====#
    if fila == col: # Ve si es parte de la diagonal principal.
        if all(tablero[i][i] != 0 for i in range(n)): # Ve si está completa.
        # Verifica si no cumple la sumatoria.
            if suma_diag1 != sumatoria:
                return False
        elif suma_diag1 > sumatoria:
            return False
    
    #====Verifica diagonal secundaria====#
    if (fila + col) == (n - 1): # Ve si es parte de la diagonal secundaria.
        if all(tablero[i][n-1-i] != 0 for i in range(n)): # Que se encuentré completa.
        # Verifica si no cumple la sumatoria.
            if suma_diag2 != sumatoria:
                return False
        elif suma_diag2 > sumatoria:
            return False

    return True # En caso de que si sea un cubo/cuadrado mágico, retorna True.

### Main ###

# Si es que la función "backtracking" retorna True se ejecutará lo que está en el interior del "if", en caso contrario se ejecutará lo que se encuentra dentro del "else".     
if backtracking(tablero, num_cas, sumatoria, 0, 0) == True: 
    print(f"\nSe encontró una solución para un tablero de {n}x{n}")
    print(f"La suma de cualquier fila, columna o diagonal debe dar: {sumatoria}.\n")
    mostrar_tablero(tablero)

else:
    print("No se encontró alguna solución posible.")
