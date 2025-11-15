# Algoritmo mínimo de backtracking para cuadrado mágico 3x3
# Variables en español y comentarios en cada línea.

# Función que verifica si la matriz dada es un cuadrado mágico (suma = suma_magica)
def verificar(cuadrado, suma_magica):
    # Verificar cada fila
    for f in range(3):
        # Si la suma de la fila f no es la suma mágica, devolver False
        if sum(cuadrado[f]) != suma_magica:
            return False
    # Verificar cada columna
    for c in range(3):
        # Si la suma de la columna c no es la suma mágica, devolver False
        if cuadrado[0][c] + cuadrado[1][c] + cuadrado[2][c] != suma_magica:
            return False
    # Verificar diagonal principal
    if cuadrado[0][0] + cuadrado[1][1] + cuadrado[2][2] != suma_magica:
        # Si la diagonal principal no coincide, devolver False
        return False
    # Verificar diagonal secundaria
    if cuadrado[0][2] + cuadrado[1][1] + cuadrado[2][0] != suma_magica:
        # Si la diagonal secundaria no coincide, devolver False
        return False
    # Si todas las comprobaciones pasaron, devolver True
    return True

# Función que imprime el cuadrado de forma legible
def imprimir(cuadrado):
    # Cabecera en consola
    print("\n--------- CUADRADO MÁGICO ENCONTRADO ---------")
    # Imprimir cada fila del cuadrado
    for fila in cuadrado:
        print(fila)
    # Pie en consola
    print("----------------------------------------------\n")

# Función principal que ejecuta el backtracking
def cuadrado_magico():
    # Tamaño fijo 3
    n = 3
    # Crear matriz 3x3 con ceros
    cuadrado = [[0 for _ in range(n)] for _ in range(n)]
    # Vector para marcar números usados del 1 al 9 (índice 0 no usado)
    usado = [False] * 10
    # Suma mágica conocida para 3x3
    suma_magica = 15
    # Variable para saber si encontramos al menos una solución
    encontrado = [False]  # lista para mutabilidad dentro de la función interna

    # Función recursiva que prueba números en la posición pos (0..8)
    def backtracking(pos):
        # Si ya llenamos las 9 casillas
        if pos == 9:
            # Verificamos si la solución es un cuadrado mágico
            if verificar(cuadrado, suma_magica):
                # Imprimimos el cuadrado si es válido
                imprimir(cuadrado)
                # Marcamos que encontramos una solución
                encontrado[0] = True
                # Devolver True para detener búsqueda (primera solución)
                return True
            # Si no es válido, devolver False para seguir probando
            return False

        # Convertir la posición lineal a fila y columna
        fila = pos // 3
        columna = pos % 3

        # Probar todos los números del 1 al 9
        for numero in range(1, 10):
            # Si el número ya se usó, saltarlo
            if usado[numero]:
                continue
            # Marcar número como usado
            usado[numero] = True
            # Colocar el número en el cuadrado
            cuadrado[fila][columna] = numero
            # Llamar recursivamente a la siguiente posición
            if backtracking(pos + 1):
                # Si se encontró solución, devolver True para propagar y cortar
                return True
            # Si no funcionó, deshacer cambios (backtracking)
            usado[numero] = False
            cuadrado[fila][columna] = 0
        # Si ningún número funcionó en esta casilla, devolver False
        return False

    # Iniciar backtracking desde la posición 0
    backtracking(0)

    # Si no se encontró ninguna solución, avisar en consola
    if not encontrado[0]:
        print("No se encontró ningún cuadrado mágico (esto no debería pasar para 3x3).")

# Punto de entrada: ejecutar la función principal cuando el archivo se ejecute
if __name__ == "__main__":
    # Llamar a la función principal para que se ejecute y muestre salida
    cuadrado_magico()

