MAX = 5
posx = [-2,-1,1,2,2,1,-1,-2] #definición de los movimientos del caballo
posy = [1,2,2,1,-1,-2,-2,-1] 
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] #crea tablero
soluciones = [] # Lista para guardar todas las soluciones

#modulo valida
def valida(nx, ny, tablero):
    #verifica que la posicion alcanzada desde x,y con el candidato está dentro del tablero y vacía
    if(nx <0 or nx>=MAX):
        return False
    if(ny <0 or ny>=MAX):
        return False
    if(tablero[nx][ny]!=0):
        return False
    return True

#modulo mostrar tablero
def mostrar_tablero(tablero):
    for fila in tablero: # Imprime cada fila del tablero
        print(" ".join(f"{c:2}" for c in fila))
    print()

# Crea una copia del tablero
def copiar_tablero(tablero): 
    return [fila[:] for fila in tablero] # Copia cada fila del tablero

# Función recursiva para encontrar todas las soluciones
def buscar_soluciones(x, y, candidato, tablero):
    global soluciones
    if candidato == MAX * MAX + 1: # Si se han hecho todos los movimientos
        soluciones.append(copiar_tablero(tablero))  # Agrega una copia del tablero a la lista
        return #sigue buscando otras soluciones

    for i in range(8): # Probar todos los movimientos posibles
        nx = x + posx[i] # Nueva posición x
        ny = y + posy[i] # Nueva posición y
        if valida(nx, ny, tablero): # Verifica si la nueva posición es válida
            tablero[nx][ny] = candidato # Marca movimiento
            buscar_soluciones(nx, ny, candidato + 1, tablero) # Llamada recursiva
            tablero[nx][ny] = 0  

# Función principal
def principal():
    cx, cy = 0, 0   # Coordenadas iniciales
    tablero[cx][cy] = 1 # Empezamos desde (0,0)
    buscar_soluciones(cx, cy, 2, tablero) # comienza la búsqueda de soluciones
    print(f"El total de soluciones encontradas fueron {len(soluciones)} soluciones.") #número de soluciones encontradas
    for i, tableros_resueltos in enumerate(soluciones[:10]):  # solo muestra las primeras 10 soluciones
        print(f"Solución {i+1}:") # le da numero a cada solución
        mostrar_tablero(tableros_resueltos) # Imprime la solución

principal()
  