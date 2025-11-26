#Cuadrado_Magico

def cuadrado_lleno(tablero, n):
    for i in range(n):
        for j in range(n):
            if tablero[i][j]==0:
                return False
    return True #todas las celdas estan llenas
#esto revisa que el tablero no contenga cuadrados vacios, si hay celdas vacias retorna false.

def primera_celda_vacia(tablero, n):
    for i in range(n):
        for j in range(n):
            if tablero[i][j]==0:
                return i, j
    return None #no hay celdas vacias       
#encuentra la primera celda que este vacia y retorna las coordenadas de esta.

def valido(tablero, n):
    numeros=[]
    constante_magica=int(n*(n*n+1)//2)
    #verifica numeros duplicados en el tablero
    for i in range(n):
        for j in range(n):
            if tablero[i][j]!=0:
                if tablero[i][j] in numeros:
                    return False
                else:
                    numeros.append(tablero[i][j])
#verifica filas, columnas y diagonales
    for i in range(n):
        fila=tablero[i]
        if 0 not in fila and sum(fila) != constante_magica:
            return False
        
    for j in range(n):
        columna=[tablero[i][j] for i in range (n)]
        if 0 not in columna and sum(columna) != constante_magica:
            return False
        
    diagonal=[tablero[i][i] for i in range(n)]
    if 0 not in diagonal and sum(diagonal) != constante_magica:
        return False
    
    anti_diagonal=[tablero[i][n-1-i] for i in range(n)]
    if 0 not in anti_diagonal and sum(anti_diagonal) != constante_magica:
        return False 
    return True

#Funcion principal de backtracking
def backtracking(tablero, n):
    if cuadrado_lleno(tablero, n):
        return tablero
    
    i, j = primera_celda_vacia(tablero, n)
    
    for numero in range(1, n*n + 1):
        tablero[i][j]=numero
        if valido(tablero, n):
            resultado=backtracking(tablero, n)
            if cuadrado_lleno(resultado, n):
                return resultado
        tablero[i][j] =0
    return tablero
#Programa principal
n = 3
tablero=[[0 for _ in range(n)] for _ in range(n)]
solucion=backtracking(tablero, n)
print("Solucion del Cuadrado Mágico (3x3):")
for fila in solucion:
    print(fila)

#endprint "Cuadrado Mágico"