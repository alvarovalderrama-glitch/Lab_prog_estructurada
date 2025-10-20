# ----------------------------------------------
#    Recorrido del caballo (Backtracking)
# ----------------------------------------------

MAX = 4  # Tamaño del tablero (4x4)

# --- Módulo: mostrar_tablero ---
# Muestra el tablero de forma ordenada con líneas y cuadrícula
def mostrar_tablero(tablero):
    print("\n" + "-" * (MAX * 4 + 1))
    for fila in tablero:
        for celda in fila:
            print(f"| {celda:2}", end=" ")  # {celda:2} mantiene alineados los números
        print("|")
        print("-" * (MAX * 4 + 1))
    print("")

# --- Módulo: valida ---
# Comprueba si un movimiento del caballo es válido.
# Devuelve True si la nueva posición está dentro del tablero y vacía.
def valida(tablero, candidato, x, y):
    # Posibles movimientos del caballo (8 en total)
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    
    # Calcula la nueva posición desde (x, y)
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    
    # Comprueba límites del tablero y que la casilla esté vacía
    if nx < 0 or nx >= MAX or ny < 0 or ny >= MAX:
        return False
    if tablero[nx][ny] != 0:
        return False
    return True

# --- Módulo: siguiente_posicion ---
# Devuelve las coordenadas (nx, ny) que se alcanzan desde (x, y)
# con el movimiento indicado por "candidato".
def siguiente_posicion(tablero, candidato, x, y):
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx, ny

# --- Módulo: final ---
# Revisa si todas las casillas del tablero fueron visitadas (no hay ceros).
def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0:
                return False
    return True

# --- Módulo: buscar_xy ---
# Busca las coordenadas (i, j) donde se encuentra un número específico (contador).
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i, j

# --- Módulo principal: solucion ---
# Implementa el algoritmo de backtracking para encontrar
# el recorrido completo del caballo en el tablero.
def solucion(tablero):
    candidato = 1          # Movimiento actual del caballo (1 a 8 posibles)
    solucion = False        # Bandera para saber si se encontró solución
    x, y = 0, 0             # Posición inicial del caballo (esquina superior izquierda)
    contador = 1            # Contador de pasos
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]  # Guarda los movimientos probados
    tablero[x][y] = contador  # Marca la primera posición con el número 1

    # Bucle principal del backtracking
    while candidato <= 8 and not solucion:
        if valida(tablero, candidato, x, y):
            # Si el movimiento es válido, avanza
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1  # Marca el nuevo paso
            mostrar_tablero(tablero)        # Muestra el tablero en cada paso
            
            if final(tablero):
                # Si todas las casillas están llenas, se encontró una solución
                solucion = True
            else:
                # Si no, continúa explorando desde la nueva posición
                tablero_aux[x][y] = candidato
                x, y = nx, ny
                contador += 1
                candidato = 1
        else:
            # Si el movimiento no es válido, prueba el siguiente
            candidato += 1
            # Si ya probó los 8 movimientos posibles sin éxito, retrocede
            while candidato == 9 and not (x == 0 and y == 0):
                tablero[x][y] = 0          # Borra el último movimiento
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)  # Retrocede a la posición anterior
                candidato = tablero_aux[nx][ny] + 1    # Intenta el siguiente movimiento posible
                tablero_aux[nx][ny] = 0
                x, y = nx, ny
                mostrar_tablero(tablero)
    return solucion

# --- Programa principal ---
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]  # Crea tablero vacío
mostrar_tablero(tablero)  # Muestra tablero inicial

# Llama al algoritmo de solución y muestra el resultado
if solucion(tablero):
    print("✅ Hay solución:")
    mostrar_tablero(tablero)
else:
    print("❌ No hay solución.")