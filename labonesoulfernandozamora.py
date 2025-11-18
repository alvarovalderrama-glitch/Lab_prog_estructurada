### Laberinto una solucion ###
import random

# Asignar variables
soluciones = [] # Lista para almacenar posibles soluciones 
candidato = 1 # Representa la dirección del movimiento: 1: derecha, 2: abajo, 3: izquierda, 4: arriba
contador = 1 # Contador de pasos en la ruta de la solución
x = y = xsiguiente = ysiguiente = 0 # Coordenadas actuales (x, y) y siguientes (xsiguiente, ysiguiente). Se inicializan en (0, 0)

#prepa el tablero
def crear_tablero(MAX):
    # Crea una matriz (lista de listas) de tamaño MAX x MAX inicializada con 0
    return [[0 for _ in range(MAX)] for _ in range(MAX)]


def colocar_obstaculos(tablero, MAX):
    # Coloca obstáculos ('x') aleatoriamente en el tablero.
    # El número de obstáculos es igual a MAX.
    for _ in range(MAX):
        # Genera coordenadas aleatorias
        x, y = random.randint(0, MAX - 1), random.randint(0, MAX - 1)
        # Asegura que el punto de inicio (0, 0) y el final (MAX-1, MAX-1) no sean obstáculos
        if (x, y) not in [(0, 0), (MAX - 1, MAX - 1)]:
            tablero[x][y] = "X" # 'X' representa un obstáculo


def mostrar_tablero(tablero, MAX):
    # Imprime el tablero en la consola
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ") # Imprime el contenido de la celda seguido de un espacio
        print("") # Salto de línea al final de cada fila
    print("") # Salto de línea adicional para separar tableros


# seleccionar el tamaño del tablero
def elegir_dimensiones():
    # Solicita al usuario la dimensión del tablero (MAX) y valida la entrada
    while True:
        try:
            MAX = int(input("Introduzca la dimension para la matriz cuadrada (mayor que 1):\n>"))
        except ValueError:
            print("Error. Introduzca un número entero mayor que 1\n")
            continue # Vuelve a pedir la entrada
        if MAX <= 1:
            print("Error. Introduzca un número entero mayor que 1\n")
        else:
            return MAX # Devuelve la dimensión válida



# consulta si la direccion a la que se quiere ir está dentro del tablero y está vacía (0)
def valida(tablero, candidato, x, y, MAX):
    # Arreglos que definen los cambios en x e y para las 4 direcciones:
    # [Derecha, Abajo, Izquierda, Arriba]
    xdireccion = [0,1,0,-1]
    ydireccion = [1,0,-1,0]
    
    # Calcula las coordenadas de la siguiente posición
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    
    # 1. Verifica si la siguiente posición está fuera de los límites del tablero
    if xsiguiente < 0 or xsiguiente == MAX: # Verifica límite superior/inferior de x
        return False
    if ysiguiente < 0 or ysiguiente == MAX: # Verifica límite izquierdo/derecho de y
        return False
    
    # 2. Verifica si la siguiente posición está vacía (cero)
    if tablero[xsiguiente][ysiguiente] == 0:
        return True # Es una posición válida
    else:
        return False # Es un obstáculo ('X') o ya se visitó (número > 0)


# devuelve las x e y del siguiente movimiento
def siguiente_posicion(candidato, x, y):
    # Calcula la siguiente posición basada en la dirección (candidato)
    xdireccion = [0,1,0,-1]
    ydireccion = [1,0,-1,0]
    
    # Calcula las coordenadas
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    
    return xsiguiente, ysiguiente


def final(x, y, MAX):
    # Comprueba si la posición actual (x, y) es la posición final
    if x == MAX - 1 and y == MAX - 1:
        return True
    return False


# ---------------- FUNCIONES SOLUCION ---------------- #

# buscar la primera solucion (implementa el algoritmo de Backtracking)
def solucion_unica(candidato, tablero, contador, x, y, MAX):
    # Condición de éxito: Si la posición actual es el final, hemos encontrado una solución
    if final(x, y, MAX):
        return True
    
    # Bucle para probar las 4 direcciones (candidatos)
    while candidato <= 4:
        # 1. Verificar si el movimiento en la dirección 'candidato' es válido
        if valida(tablero, candidato, x, y, MAX):
            # Obtener las coordenadas del siguiente paso
            xsiguiente, ysiguiente = siguiente_posicion(candidato, x, y)
            
            # Marcar el movimiento:
            contador += 1 # Incrementar el contador de pasos
            tablero[xsiguiente][ysiguiente] = contador # Marcar la celda con el número de paso
            
            # Llamada recursiva: va a proseguir con la siguiente posición hasta llegar al final
            if solucion_unica(1, tablero, contador, xsiguiente, ysiguiente, MAX):
                return True # Si la llamada recursiva retorna True (solución encontrada), propagar el éxito
            
            # Backtracking: si la llamada recursiva devuelve False (no hay solución desde ahí):
            # si no encuentra el final, se devuelve (deshace el último movimiento)
            tablero[xsiguiente][ysiguiente] = 0 # Borra el ultimo movimiento (restablece a 0)
            contador -= 1 # Decrementar el contador de pasos
            
        candidato += 1 # Probar con la siguiente dirección
    
    # Si se han probado las 4 direcciones y ninguna lleva a la solución
    return False


# ---------------- PROGRAMA PRINCIPAL ---------------- #
def main():
    # 1. Configuración del tablero
    MAX = elegir_dimensiones() # Pide al usuario la dimensión
    tablero = crear_tablero(MAX) # Crea el tablero inicializado a 0
    colocar_obstaculos(tablero, MAX) # Añade obstáculos aleatorios
    
    print("Tablero creado:\n")
    mostrar_tablero(tablero, MAX) # Muestra el tablero inicial
    
    # 2. Establecer el punto de partida
    # Las coordenadas de inicio son (x, y) = (0, 0).
    tablero[x][y] = 1 # Marcar la posición inicial como el primer paso
    
    # 3. Buscar la solución
    # Se llama a la función de backtracking desde el inicio (0, 0) y con el primer candidato (1)
    if solucion_unica(candidato, tablero, contador, x, y, MAX):
        print("Solución encontrada:\n")
        mostrar_tablero(tablero, MAX) # Muestra el tablero con la ruta marcada
    else:
        print("No hay solución.")


if __name__ == "__main__":
    main()