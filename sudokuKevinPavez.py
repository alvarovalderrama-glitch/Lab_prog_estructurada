MAX = 9
"""Comenzamos creando un tablero 9x9 llenos de 0's 
"""
def crear_tablero():
    tablero = []
    for i in range (MAX):
        fila = []
        for j in range (MAX):
            fila.append(0)
        tablero.append(fila)
    return tablero
        
"""Seguimos con la funcion para imprimir el tablero en
la terminal y utilizamos un ciclo for para su impresion"""
def imprimir_tablero(tablero):
    print("\n" + "="*25)
    print("        SUDOKU 9x9")
    print("="*25)
    
    for i in range(MAX):
        if i % 3 == 0 and i != 0:
            print("  " + "-"*6 + "+" + "-"*7 + "+" + "-"*7)
        
        print("  ", end="")  
        for j in range(MAX):
            if j % 3 == 0 and j != 0:
                print("| ", end="")  
            
            if tablero[i][j] == 0:
                print("_ ", end="")  
            else:
                print(str(tablero[i][j]) + " ", end="") 
        
        print()  
    """"Comenzamos con las validaciones en fila,
    columna y cada bloque del 3x3
    """

def validar_fila(tablero, fila, num):
    """Validacion de fila"""
    for j in range (MAX):
        if tablero[fila][j] == num:
            return False
    return True

def validar_columna(tablero, columna, num):
    """Validacion de columnas"""
    for i in range (MAX):
        if tablero[i][columna] == num:
            return False
    return True
def validar_bloque(tablero, fila, columna, num):
    """Calcular en que bloque estamos"""
    fila_inicio = (fila // 3) * 3
    columna_inicio = (columna // 3) * 3
    
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(columna_inicio, columna_inicio + 3):
            if tablero[i][j] == num:
                """Retornamos false ya que el numero ya existia en el bloque
                """
                return False 
    
    return True

"""Combinamos las 3 validaciones"""
def es_valido(tablero, fila, columna, num):
    return (validar_fila(tablero, fila, num) and
            validar_columna(tablero, columna, num) and
            validar_bloque(tablero, fila, columna, num))

def encontrar_casilla_vacia(tablero):
    """Funcion para buscar la primera casilla vacia"""
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0:
                return (i, j)
    return None


def resolver_sudoku(tablero):
    """Utilizamos backtracking para resolver el sudoku"""
    "Caso base:"
    casilla = encontrar_casilla_vacia(tablero)
    
    """El puzle esta resuelto si no hay casillas vacias"""
    if casilla is None:
        return True
    
    fila, columna = casilla
    
    """Recursividad:"""
    for num in range(1, 10):
        if es_valido(tablero, fila, columna, num):
            """Intentamos numero"""
            tablero[fila][columna] = num
            
            """Llamada a la recursividad"""
            if resolver_sudoku(tablero):
                return True
            """Backtracking"""
            tablero[fila][columna] = 0
    
    """Si ningun intento funciono, retornamos false"""
    return False

"""Programa main"""
if __name__ == "__main__":
    """Este sera nuestro tablero, podemos poner tantas pistas como queramos"""
    tablero = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("TABLERO INICIAL:")
    imprimir_tablero(tablero)
    
    print("Resolviendo :3")
    
    if resolver_sudoku(tablero):
        print("\n SOLUCIÓN ENCONTRADA:")
        imprimir_tablero(tablero)
    else:
        print("\n No se encontró solución")