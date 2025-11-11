
def valida(tablero, candidato, x, y):
    """ Verifica si un movimiento del caballo (candidato)
    desde la posición (x, y) es válido.
    Retorna True si el movimiento está dentro del tablero
    y la casilla destino está vacía (valor 0). """
    nx = x + pos_x[candidato - 1]
    ny = y + pos_y[candidato - 1]

    # Comprobar que las nuevas coordenadas no salgan del tablero
    if nx < 0 or nx >= tamaño_tablero:

        return False
    if ny < 0 or ny >= tamaño_tablero:
        return False
    
    # Comprobar que la casilla no haya sido visitada
    if tablero[nx][ny] != 0:
        return False
    
    return True # movimiento válido


def siguiente_posicion(candidato, x, y):
    """ Calcula y devuelve las nuevas coordenadas (nx, ny)
    que el caballo alcanzaría al realizar el movimiento indicado. """
    nx = x + pos_x[candidato - 1]
    ny = y + pos_y[candidato - 1]
    return nx, ny


def final(tablero):
    """" Determina si el tablero está completo.
    Retorna True cuando todas las casillas tienen un valor distinto de 0 """
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            if tablero[i][j] == 0:
                return False
    return True


def copiar_tablero(tablero):
    """Devuelve una copia independiente del tablero actual.
    Esto permite guardar una solución sin que sea modificada
    por futuros retrocesos"""
    copia = []
    for fila in tablero:
        copia.append(fila[:])
    return copia     # Copia cada fila de la matriz


def mostrar_tablero(tablero):
    # Imprime el tablero en formato cuadrado
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            print(f"{tablero[i][j]:2}", end=" ") # Imprime cada casilla con 2 espacios
        print("")
    print("")


def solucion(tablero, x = 0, y = 0, contador = 1, primera_solucion = None):
    """ Parámetros:
        tablero: matriz NxN que representa el recorrido del caballo.
        x, y: posición actual del caballo.
        contador: número del movimiento actual.
        primera_solucion: almacena la primera solución encontrada (opcional).

    Retorna:
        (total, primera_solucion)
        - total: número total de soluciones encontradas.
        - primera_solucion: copia del tablero con la primera solución. """
    
    # Si el tablero está completo, se encontró una solución
    if final(tablero):
        # Si aún no hay una solución guardada, guardar la primera
        if primera_solucion is None:
            primera_solucion = copiar_tablero(tablero)
        return 1, primera_solucion  # una solución encontrada

    total = 0 # contador local de soluciones

    # Probar los 8 posibles movimientos del caballo
    for candidato in range(1, 9):
        if valida(tablero, candidato, x, y):
            # Calcular la nueva posición válida
            nx, ny = siguiente_posicion(candidato, x, y)
            
            # Marcar el movimiento en el tablero
            tablero[nx][ny] = contador + 1

            # Llamada recursiva: acumular resultados
            sub_total, primera_solucion = solucion(tablero, nx, ny, contador + 1, primera_solucion)
            
            # Acumular el total de soluciones
            total += sub_total

            # Retroceso: deshacer el movimiento
            tablero[nx][ny] = 0 

    return total, primera_solucion


# Programa principal

tamaño_tablero = 5  # tamaño del tablero
pos_x = [-2, -1, 1, 2, 2, 1, -1, -2] # desplazamientos horizontales del caballo
pos_y = [1, 2, 2, 1, -1, -2, -2, -1] # desplazamientos verticales del caballo

# Crear tablero vacío
tablero = [[0 for i in range(tamaño_tablero)] for j in range(tamaño_tablero)]

# Posición inicial del caballo
tablero[0][0] = 1  # posición inicial

print(f"Buscando soluciones para un tablero de {tamaño_tablero}x{tamaño_tablero}...\n")

# Llamar a la función principal
cantidad, una_solucion = solucion(tablero)

if una_solucion:
    print("Ejemplo de una solución encontrada:\n")
    mostrar_tablero(una_solucion)

    print(f"Cantidad total de soluciones: {cantidad}")

else:

    print("No se encontró una solución")

