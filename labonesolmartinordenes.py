import random

def hacer_Lab(n, prob_obs=0.25): # crea un laberinto con una probabilidad de generar obstaculos (muros)
    lab = []
    for i in range(n):
        fila = []
        for j in range(n):
            if random.random() < prob_obs:
                fila.append('|')
            else: 
                fila.append('-')
        lab.append(fila) 
    lab[0][0] = 'i'
    lab[n-1][n-1] = 'F' # hace que las entrada y las salida esten despejadas
    return lab
def imprim_Lab(lab): # hace que se imprima el laberinto
    for fila in lab:
        print(''.join(fila))
    print()


def valido(lab, x, y): # define la funcion para validar si la casilla está disponible para moverse
    n = len(lab)
    return 0<= x <= n and 0<= y < n and lab[x][y] in ('-','F')

def resolver(lab, x=0, y=0): # se hace uso de backtracking para llegar al final
    if lab[x][y] == 'F':
        return True
    if lab[x][y] == '-': # marca el camino que hay que seguir
        lab[x][y] = '*'


    mov = [(0,1),(1,0),(0,-1),(-1,0)] # define los movimientos que se pueden hacer

    for dx, dy in mov:
        nx, ny = x + dx, y + dy
        if valido(lab, nx, ny) and resolver(lab, nx, ny):
            return True

    if hacer_Lab[x][y] not in ('|','F'): # retrocede en caso de que no se llegue al final
        hacer_Lab[x][y] = '-'
    return False

n = int(input("cual será el tamaño del laberinto (número):")) # se pide que se ingrese el tamaño del tablero
lab = hacer_Lab(n)

print("\nSe ha creado el laberinto:\n")
imprim_Lab(lab)

if resolver(lab):
    print('se encontró un camino:\n')
else:
    print('no se encontró un camino\n')

imprim_Lab(lab)