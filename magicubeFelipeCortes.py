def imprimir_tablero(tablero):
    for i in range(0, 9, 3):
        print(tablero[i], tablero[i+1], tablero[i+2]) #Imprime cada fila

def backtracking(tablero, posicion, soluciones):
    if posicion == 9:
        soluciones.append(tablero[:]) #Se hace una copia de la solución actual y se guarda
        return
    
    for i in range(posicion, 9):
        tablero[posicion], tablero[i] = tablero[i], tablero[posicion] #Se cambia el número de la posición con 'i' para probar numeros
        backtracking(tablero, posicion + 1, soluciones) #Avanza a la siguiente casilla
        tablero[posicion], tablero[i] = tablero[i], tablero[posicion]  #Retrocede de casilla

numeros = list(range(1, 10)) #Crea la lista con números del 1 al 9
soluciones = [] # Almacena las soluciones encontradas
backtracking(numeros, 0, soluciones) #Comienza desde la posición 0 con la lista inicial

print(f"Se encontraron {len(soluciones)} soluciones") #Muestra la cantidad de soluciones totales
print("=" * 50)

for solucion, sol in enumerate(soluciones): #Imprimir todas las soluciones
    print(f"Solución {solucion + 1}:")
    imprimir_tablero(sol)
    print('=' * 12)