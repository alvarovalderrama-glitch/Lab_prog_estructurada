import random  # Importa el módulo random

def mostrar_tablero(tablero):  # Devuelve el tablero como texto
    return "\n".join(" ".join(str(c) for c in fila) for fila in tablero) + "\n"  # Une filas y columnas

def es_valida(tablero, x, y):  # Verifica si una posición es válida
    n = len(tablero)  # Tamaño del tablero
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == 0  # Revisa límites y si está libre

def resolver_todas(tablero, x, y, soluciones, paso):  # Busca todas las rutas posibles
    n = len(tablero)  # Tamaño del laberinto
    if x == n - 1 and y == n - 1:  # Caso base: llegó a la meta
        tablero[x][y] = paso  # Marca último paso
        soluciones.append([fila.copy() for fila in tablero])  # Guarda copia
        tablero[x][y] = 0  # Desmarca para seguir buscando
        return

    if es_valida(tablero, x, y):  # Si la celda se puede usar
        tablero[x][y] = paso  # Marca paso actual
        resolver_todas(tablero, x + 1, y, soluciones, paso + 1)  # Movimiento derecha
        resolver_todas(tablero, x, y + 1, soluciones, paso + 1)  # Movimiento abajo
        resolver_todas(tablero, x - 1, y, soluciones, paso + 1)  # Movimiento izquierda
        resolver_todas(tablero, x, y - 1, soluciones, paso + 1)  # Movimiento arriba
        tablero[x][y] = 0  # Desmarca la celda

n = int(input("Ingrese tamaño del laberinto (n x n): "))  # Pide tamaño al usuario
tablero = [[0 for _ in range(n)] for _ in range(n)]  # Crea matriz n×n
soluciones = []  # Lista de soluciones
resolver_todas(tablero, 0, 0, soluciones, 1)  # Inicia búsqueda desde (0,0)

with open("soluciones_numeradas.txt", "w") as f:  # Abre archivo para guardar soluciones
    for i, sol in enumerate(soluciones, start=1):  # Recorre todas las soluciones
        f.write(f"Solución #{i}\n")  # Escribe número de solución
        f.write(mostrar_tablero(sol))  # Escribe el tablero
        f.write("\n" + "-" * 30 + "\n")  # Separador

print(f"Se encontraron {len(soluciones)} soluciones y se guardaron en 'soluciones_numeradas.txt'")  # Mensaje final
