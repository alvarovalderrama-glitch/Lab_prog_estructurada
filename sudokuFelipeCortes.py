sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def imprimir_sudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0: #Agrega una separación cada 3 Filas
            print("- - - - - - - - - - -")
        fila = ""
        for j in range(9):
            if j % 3 == 0 and j != 0: #Agrega una separación cada 3 columnas
                fila += "| "
            fila += str(sudoku[i][j]) + " "
        print(fila)


def encontrar_coordenada_grid(val):
    if val <= 2: #Encuentra el grid superior / izquierdo
        return 0
    elif val <= 5: #Encuentra el grid del medio / centro
        return 1
    else: #Encuentra el grid inferior / derecho
        return 2

def obtener_grid_celda(x, y, sudoku):
    subgrid_col = encontrar_coordenada_grid(x) #Busca por los grids de fila
    subgrid_fila = encontrar_coordenada_grid(y) #Busca por los grids de columna
    
    grid = []
    for fila in sudoku[subgrid_fila *3: subgrid_fila *3 + 3]: #Obtiene las filas del grid
        for col in fila[subgrid_col *3: subgrid_col * 3 + 3]: #Obtiene las columnas del grid
            grid.append(col)
            
    return grid
    
def es_posible(x, y, valor, sudoku):
    if valor in sudoku[y]: #Detecta si está el mismo numero en la fila
        return False 

    col = [fila[x] for fila in sudoku] #Detecta si está el mismo numero en la columna
    if valor in col:
        return False
    
    grid3x3 = obtener_grid_celda(x, y, sudoku)
    if valor in grid3x3: #Detecta si está el mismo numero en el grid
        return  False
    
    return True

def resolver_sudoku(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for valor in range(1,10):
                    if es_posible(x, y, valor,sudoku):
                        sudoku[y][x] = valor #Le asigna un valor
                        if resolver_sudoku(sudoku):
                            return True
                        sudoku[y][x] = 0
                        
                return False
    imprimir_sudoku(sudoku)
    return True

print("Imprimiendo Sudoku...\n")

if not resolver_sudoku(sudoku):
    print("No se encontraron soluciones")