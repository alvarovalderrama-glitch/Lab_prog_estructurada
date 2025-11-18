import random

# Asignar variables
# Se utilizará para almacenar copias del tablero cada vez que se encuentre una solución
soluciones = [] 
candidato = 1 # Dirección del movimiento
contador = 1 # Contador de pasos en la ruta de la solución
x = y = xsiguiente = ysiguiente = 0 # Coordenadas iniciales

# --- (Las funciones crear_tablero, colocar_obstaculos, mostrar_tablero,
#      elegir_dimensiones, valida, siguiente_posicion y final permanecen IGUALES) ---

#prepara el tablero
def crear_tablero(MAX):
    return [[0 for _ in range(MAX)] for _ in range(MAX)]

def colocar_obstaculos(tablero, MAX):
    for _ in range(MAX):
        x, y = random.randint(0, MAX - 1), random.randint(0, MAX - 1)
        if (x, y) not in [(0, 0), (MAX - 1, MAX - 1)]:
            tablero[x][y] = "X"

def mostrar_tablero(tablero, MAX):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")

#elige los parametros
def elegir_dimensiones():
    while True:
        try:
            MAX = int(input("Introduzca la dimension para la matriz cuadrada (mayor que 1):\n>"))
        except ValueError:
            print("Error. Introduzca un número entero mayor que 1\n")
            continue
        if MAX <= 1:
            print("Error. Introduzca un número entero mayor que 1\n")
        else:
            return MAX

#funcion posicion
def valida(tablero, candidato, x, y, MAX):
    xdireccion = [0,1,0,-1]
    ydireccion = [1,0,-1,0]
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    if xsiguiente < 0 or xsiguiente == MAX:
        return False
    if ysiguiente < 0 or ysiguiente == MAX:
        return False
    if tablero[xsiguiente][ysiguiente] == 0:
        return True
    else:
        return False

def siguiente_posicion(candidato, x, y):
    xdireccion = [0,1,0,-1]
    ydireccion = [1,0,-1,0]
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    return xsiguiente, ysiguiente

def final(x, y, MAX):
    if x == MAX - 1 and y == MAX - 1:
        return True
    return False


# Buscar TODAS las soluciones usando Backtracking
def buscar_todas_soluciones(candidato, tablero, contador, x, y, MAX):
    global soluciones # Permite modificar la lista global de soluciones

    #En lugar de devolver True y detenerse  almacena la solución encontrada y hace backtracking para buscar más.
    if final(x, y, MAX):
        # Almacenar una COPIA profunda del tablero con la solución
        soluciones.append([fila[:] for fila in tablero])
        return 
    
    while candidato <= 4:
        if valida(tablero, candidato, x, y, MAX):
            xsiguiente, ysiguiente = siguiente_posicion(candidato, x, y)
            contador += 1
            tablero[xsiguiente][ysiguiente] = contador
            
            # Llamada recursiva: NO comprueba el valor de retorno; solo sigue explorando
            buscar_todas_soluciones(1, tablero, contador, xsiguiente, ysiguiente, MAX)
            
            # Backtracking: Deshace el movimiento (esto es crucial para seguir explorando)
            tablero[xsiguiente][ysiguiente] = 0 
            contador -= 1
            
        candidato += 1


#programa principal modificado
def main():
    global soluciones
    
    MAX = elegir_dimensiones()
    tablero = crear_tablero(MAX)
    colocar_obstaculos(tablero, MAX)
    
    print("Tablero creado:\n")
    mostrar_tablero(tablero, MAX)
    
    # Establecer el punto de partida
    global x, y, contador, candidato
    tablero[x][y] = 1

    # Iniciar la búsqueda de todas las soluciones
    buscar_todas_soluciones(candidato, tablero, contador, x, y, MAX)
    
    # Mostrar resultados
    if soluciones:
        print(f"🥳 ¡Se encontraron {len(soluciones)} soluciones! 🥳\n")
        
        # Muestra solo las primeras N soluciones (para tableros grandes)
        num_a_mostrar = min(len(soluciones), 3) 
        for i in range(num_a_mostrar):
            print(f"--- Solución {i + 1} ---")
            mostrar_tablero(soluciones[i], MAX)
            
        if len(soluciones) > num_a_mostrar:
            print(f"... y {len(soluciones) - num_a_mostrar} soluciones más.")
    else:
        print(" No hay solución.")

if __name__ == "__main__":
    main()