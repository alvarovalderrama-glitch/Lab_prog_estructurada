import copy                                                      # Importa módulo que se utilizara más adelante, para hacer copias profundas de listas

MAX =  int(input("Ingrese el tamaño del tablero: "))             # Tamaño del tablero cuadrado (Se puede Cambiar).

#  Módulo mostrar_tablero 
def mostrar_tablero(tablero):                                    # Definimos una funcion para imprimir el tablero, la llamamos mostrar_tablero y le entregamos el parametro de tablero.
    for fila in tablero:                                         # Recorre cada fila del tablero
        print(" ".join(f"{x:2}" for x in fila))                  # Imprime fila con cada valor de ancho 2
    print("")                                                    # Línea en blanco para separar tableros

#  Módulo valida 
def valida(tablero, x, y):                                       # Función para verificar si la celda es válida
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] == 0  # True si está dentro y no visitada

#  Módulo final 
def final(x, y):                                                 # Función que indica si se llegó a la meta
    return x == MAX - 1 and y == MAX - 1                         # True si es la esquina inferior derecha

#  Backtracking principal 
def resolver(tablero, x, y, contador, soluciones):               # Función recursiva para explorar caminos

    '''if soluciones:                                            # Si ya se encontró al menos una solución, detener la recursión.
        return'''
    
    if x == MAX - 1 and y == MAX - 1:                            # Si llegamos a la meta
        tablero[x][y] = contador - 1                             # Ajusta el valor final
        soluciones.append(copy.deepcopy(tablero))                # Guarda una copia del tablero
        tablero[x][y] = 0                                        # Deshace el cambio (backtracking)
        return                                                   # Termina esta rama

    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]             # Movimientos posibles: derecha, abajo, izquierda, arriba
    

    for dx, dy in movimientos:                                   # Recorre cada movimiento
        
        '''if soluciones:                                        # Detener si ya se encontró una solución.
            return'''
        
        nx, ny = x + dx, y + dy                                  # Calcula nuevas coordenadas
        if valida(tablero, nx, ny):                              # Si la celda es válida
            tablero[nx][ny] = contador                           # Marca el paso actual
            resolver(tablero, nx, ny, contador + 1, soluciones)  # Llama recursivamente
            tablero[nx][ny] = 0                                  # Deshace el cambio (backtracking)

#   NUEVO MÓDULO: mejor_solucion 
def mejor_solucion(soluciones):                                  # Función para determinar cuál es la mejor solución (la más corta)
                                                                 # En este caso, todas las soluciones llegan a la meta, pero algunas pueden tener caminos más largos.
                                                                 # Por eso comparamos cuántos pasos se usaron en cada una.

    mejor = None                                                 # Variable para guardar la mejor solución encontrada
    menor_pasos = None                                           # Variable para guardar la cantidad de pasos de la mejor

    for sol in soluciones:                                       # Recorremos cada solución guardada
        pasos = max(max(fila) for fila in sol)                   # Buscamos el número máximo del tablero, que representa el último paso realizado
        if menor_pasos is None or pasos < menor_pasos:           # Si aún no hay mejor o esta usa menos pasos...
            menor_pasos = pasos                                  # Actualizamos la cantidad mínima de pasos
            mejor = sol                                          # Guardamos la nueva mejor solución

    return mejor, menor_pasos                                    # Devolvemos la mejor solución y su número de pasos

#  Programa principal 
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]          # Crea tablero inicial lleno de ceros
tablero[0][0] = 1                                                # Marca el punto de partida

soluciones = []                                                  # Lista para guardar soluciones
resolver(tablero, 0, 0, 2, soluciones)                           # Llama al backtracking desde (0,0) con contador 2

#  Mostrar resultados 
if soluciones:                                                   # Si se encontraron soluciones

    print(f"Se encontraron {len(soluciones)} soluciones para un tablero de {MAX}x{MAX}:\n")    # Muestra cuántas soluciones hay
    for i, sol in enumerate(soluciones, 1):                                                    # Itera sobre soluciones
        print(f"Solucion {i}:")                                                                # Imprime número de solución
        mostrar_tablero(sol)                                                                   # Muestra el tablero completo

    #  Llamamos al módulo mejor_solucion 
    mejor, pasos = mejor_solucion(soluciones)                      # Obtenemos la mejor solución y su número de pasos
    print("=== MEJOR SOLUCIÓN ENCONTRADA ===")                     # Encabezado para distinguirla
    print(f"Usa {pasos} pasos para llegar a la meta.\n")           # Muestra cuántos pasos usa
    mostrar_tablero(mejor)                                         # Muestra el tablero de la mejor solución

else:                                                                                          # Si no hay soluciones
    print(f"No hay soluciones posibles para un tablero de {MAX}x{MAX}.")                       # Mensaje

#  Guardar soluciones en archivo 
nombre_archivo = f"soluciones_MAX{MAX}.txt"                                                    # Con esta variable creamos un nombre unico para cada solucion segun su Max, osea su cantidad de filas y colummnas.

with open(nombre_archivo, "w") as f:                                                           # Abre archivo para escritura
    for n, sol in enumerate(soluciones, 1):                                                    # Itera sobre soluciones
        f.write(f"Solucion {n} (tablero {MAX}x{MAX}):\n")                                      # Escribe título
        for fila in sol:                                                                       # Recorre cada fila
            f.write(" ".join(f"{x:2}" for x in fila) + "\n")                                   # Escribe fila formateada
        f.write("\n")                                                                          # Línea en blanco entre soluciones

    #   Guarda la mejor solucion
    if soluciones:                                                                             # Solo si hay soluciones
        f.write("=== MEJOR SOLUCION ENCONTRADA ===\n")                                         # Escribe encabezado
        f.write(f"Usa {pasos} pasos para llegar a la meta.\n\n")                               # Escribe el número de pasos
        for fila in mejor:                                                                     # Recorre cada fila de la mejor solución
            f.write(" ".join(f"{x:2}" for x in fila) + "\n")                                   # Escribe la fila formateada (darle un formato visual y ordenado a los numeros en este caso)
        f.write("\n")                                                                          # Línea en blanco al final

print(f" Todas las soluciones y la mejor se han guardado en '{nombre_archivo}'.")              # Muestra donde se guardaron todas las soluciones y la mejor solucion
