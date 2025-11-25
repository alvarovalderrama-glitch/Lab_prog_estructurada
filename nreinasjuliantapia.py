def mostrar_tablero(tablero):
    print()
    for i,linea in enumerate(tablero):
        print(str(i+1) + ' ' + ' '.join(linea))
    print()

def mostrar_soluciones(tablero,lista):
    n = len(tablero)
    for i,solucion in enumerate(lista):
        tablero_aux = [['◻' for i in range(n)] for j in range(n)]
        for reina in solucion:
            x,y = reina
            tablero_aux[x][y] = '◼'
        print(f'Solución {i+1}: ')
        mostrar_tablero(tablero_aux)

def validar(tablero,posible_reina,reinas_colocadas):
    px,py = posible_reina
    
    if tablero[px][py] == 0:
        for reina in reinas_colocadas:
            rx,ry = reina
            if py == ry:
                return False
            elif (px-py) == (rx-ry) or (px+py) == (rx+ry):
                return False
        return True
    else:
        return False

def solucion(tablero):
    all_soluciones = []
    
    def backtrack(fila,reinas_colocadas):
        for indice in range(len(tablero)):
            columna = indice
            reina = (fila,columna)
            
            if not validar(tablero,reina,reinas_colocadas):
                continue
            elif fila == len(tablero)-1:
                solucion = reinas_colocadas + [reina]
                all_soluciones.append(solucion)
            else:
                tablero[fila][columna] = 1
                backtrack(fila + 1,reinas_colocadas + [reina])
                tablero[fila][columna] = 0
    
    fila_inicial = 0
    reinas = []
    backtrack(fila_inicial,reinas)
    return all_soluciones
    
# ----- Main -----

n = 9

tablero = [[0 for i in range(n)] for j in range(n)]
lista_soluciones = solucion(tablero)

if lista_soluciones == []:
    print(f'No hay soluciones para un tablero de {n}x{n}.')
else:
    mostrar_soluciones(tablero,lista_soluciones)