import random
def crear_tablero(tamaño):
    
    return [[0 for _ in range(tamaño)] for _ in range(tamaño)]


def obstaculo(tablero):
    num=0
    tamaño = len(tablero)
    num_obstaculos =(tamaño * tamaño) // 5  # 20% del tablero como obstáculos
    for i in range(num_obstaculos):
            x = random.randint(0, tamaño - 1)
            y = random.randint(0, tamaño - 1)
            if (x, y) not in [(0, 0), (tamaño - 1, tamaño - 1)]:# Evita la posición inicial y final
                tablero[x][y] = -1  
            else:
                 i-= 1  # Reintenta si el obstáculo cae en la posición inicial o final
     
def mostrar_tablero(tablero):
    for i in range(tamaño):
        for j in range(tamaño):
            print(tablero[i][j], end = " ") 
        print(" ")
    print(" ")

def final(tablero, tamaño):
            if tablero[tamaño-1][tamaño-1] == 0:# Verifica si la posición final ha sido alcanzada
                return False
            return True

def mover(tablero, x, y, tamaño):
    
    if final(tablero, tamaño):
       print("Camino encontrado:")
       mostrar_tablero(tablero)
       return True
    movimientos_x = [1, 0, -1, 0]
    movimientos_y = [0, 1, 0, -1]

    for i in range(4):
        nx = x + movimientos_x[i]
        ny = y + movimientos_y[i]
        if 0 <= nx < tamaño and 0 <= ny < tamaño and tablero[nx][ny] == 0:
            tablero[nx][ny] = tablero[x][y] + 1

            if mover(tablero, nx, ny, tamaño):
                return True
            tablero[nx][ny] = 0  # Retroceso
    return False

def recorrido(tamaño, x_inicial=0, y_inicial=0):
    tablero = crear_tablero(tamaño)
    obstaculo(tablero)
    tablero[x_inicial][y_inicial] = 1
    mover(tablero, x_inicial, y_inicial, tamaño)

# Ejecución principa

tamaño = int(input("Ingrese el tamaño del tablero: "))
recorrido(tamaño)