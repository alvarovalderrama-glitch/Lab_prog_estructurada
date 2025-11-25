import random

N = 3
META = 15  # Constante magica para N=3

# Inicializamos el tablero con ceros usando comprension de listas
tablero = [[0 for _ in range(N)] for _ in range(N)]

def es_magico(tab):
    # Verifica si la suma de filas, columnas y diagonales es igual a META
    # Verificar filas
    if not all(sum(fila) == META for fila in tab):
        return False
    # Verificar columnas (zip transpuesto permite iterar por columnas)
    if not all(sum(col) == META for col in zip(*tab)):
        return False
    # Verificar diagonal principal
    if sum(tab[i][i] for i in range(N)) != META:
        return False
    # Verificar diagonal secundaria
    if sum(tab[i][N - 1 - i] for i in range(N)) != META:
        return False
    return True

def resolver(fila, col, usados):
    # Caso base: si hemos pasado la ultima fila, verificamos si es magico
    if fila == N:
        return es_magico(tablero)
    # Calculamos la siguiente posicion
    siguiente_fila, siguiente_col = (fila, col + 1) if col + 1 < N else (fila + 1, 0)
    # Probamos numeros del 1 al 9
    for num in range(1, N * N + 1):
        if num not in usados:
            tablero[fila][col] = num
            usados.add(num) # Marcamos como usado
            # Llamada recursiva
            if resolver(siguiente_fila, siguiente_col, usados):
                return True

            # Backtracking: desmarcamos si no llego a la solucion
            usados.remove(num)
            tablero[fila][col] = 0
    return False

def generar_ecuaciones(tab):
    # Selecciona celdas aleatorias para convertirlas en ecuaciones
    cantidad = random.randint(3, 5)
    x_real = random.randint(1, 9)
    
    # Obtenemos todas las coordenadas posibles y elegimos al azar
    coordenadas = [(r, c) for r in range(N) for c in range(N)]
    elegidas = random.sample(coordenadas, cantidad)

    for f, c in elegidas:
        valor_celda = tab[f][c]
        diferencia = valor_celda - x_real
        
        # Formato de la ecuacion basado en la diferencia
        if diferencia >= 0:
            tab[f][c] = f"x + {diferencia}"
        else:
            tab[f][c] = f"x - {abs(diferencia)}"
            
    return x_real

#Funcion para agregár bordes y lineas entre los numeros
def imprimir_tablero_elegante(tab):
    # 1. Determinar el ancho maximo de cada celda
    N = len(tab)
    # Convertir todos los elementos a string y encontrar la longitud maxima
    max_len = 0
    for fila in tab:
        for celda in fila:
            max_len = max(max_len, len(str(celda)))

    # Ancho de la celda: max_len + 2 (espacio a cada lado para padding)
    ancho_celda = max_len + 2
    # Separador horizontal: '+' + (celda de guiones + '+') * N
    separador_horizontal = "+" + ("-" * ancho_celda + "+") * N

    print(separador_horizontal)

    # 2. Imprimir cada fila
    for fila in tab:
        linea = "|"
        for celda in fila:
            # Centrar el contenido de la celda
            contenido = str(celda).center(ancho_celda)
            linea += contenido + "|"
        print(linea)
        print(separador_horizontal)

numeros_usados = set()

if resolver(0, 0, numeros_usados):
    valor_x = generar_ecuaciones(tablero)

    print("Cuadrado Magico Algebraico:")
    # LLAMADA A LA NUEVA FUNCION
    imprimir_tablero_elegante(tablero) 

    # Logica del juego (el 'input' debe ser reemplazado por la funcion original)
    intentos = 5
    exito = False

    for i in range(intentos, 0, -1):
        print(f"\nTe quedan {i} intentos")
        
        # En tu script original, aquí está el 'input'
        # respuesta = input("Cual es el valor de x? ")
        
        # Para tu uso normal, simplemente usa la línea de 'input'
        respuesta = input("Cual es el valor de x? ") # Reemplaza con la línea original
        
        # Si usas este código en un entorno no interactivo como este,
        # necesitarías simular la respuesta o eliminar esta parte.

        if respuesta.isdigit():
            if int(respuesta) == valor_x:
                print(f"\nCorrecto. x = {valor_x}")
                exito = True
                break
            else:
                print("Incorrecto.")
        else:
            print("Por favor ingresa un numero valido.")

    if not exito:
        print("\nSe han acabado los intentos.")
        print(f"El valor correcto de x era: {valor_x}")

else:
    print("No se encontro solucion.")