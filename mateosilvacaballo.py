#Caballo  (1 solución)
# Recorrido del caballo (Knight's Tour) en un tablero 5x5; detiene al hallar la primera solución.

N = 5                                                             # Tamaño del tablero
movs = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]  # 8 movimientos

tab = [[-1]*N for _ in range(N)]                                  # Inicializa con -1

def dentro(i,j):                                                  # ¿Está dentro?
    return 0<=i<N and 0<=j<N                                      # Rango válido

def mostrar():                                                    # Imprime solución
    for fila in tab:                                              # Recorre filas
        print(" ".join(f"{x:2d}" for x in fila))                  # Muestra números
    print()                                                       # Línea en blanco

encontro = False                                                  # Bandera global

def back(i,j,paso):                                               # Backtracking
    global encontro                                               # Usará bandera global
    if encontro: return                                           # Si ya hay solución, corta
    tab[i][j] = paso                                              # Marca paso actual
    if paso == N*N-1:                                             # ¿Completó 25 celdas?
        mostrar()                                                 # Muestra solución
        encontro = True                                           # Señala encontrado
        return                                                    # Termina
    # Heurística simple: ordena movimientos por accesibilidad (Warnsdorff light)
    candidatos = []                                               # Lista de próximos
    for di,dj in movs:                                            # Revisa movimientos
        ni, nj = i+di, j+dj                                       # Nueva posición
        if dentro(ni,nj) and tab[ni][nj] == -1:                   # Si es válida
            # Cuenta salidas desde (ni,nj)
            deg = sum(1 for a,b in movs if dentro(ni+a,nj+b) and tab[ni+a][nj+b]==-1)
            candidatos.append((deg, ni, nj))                      # Guarda grado y pos
    candidatos.sort()                                             # Menos salidas primero
    for _,ni,nj in candidatos:                                    # Explora ordenado
        back(ni,nj,paso+1)                                        # Llama recursivo
        if encontro: return                                       # Si encontró, corta
    tab[i][j] = -1                                                # Desmarca para retroceder

# Comienza desde (0,0); puedes cambiar a cualquier celda 0..4
back(0,0,0)                                                       # Llama con paso 0
if not encontro: print("No se encontró solución desde esa posición inicial.") # Mensaje
