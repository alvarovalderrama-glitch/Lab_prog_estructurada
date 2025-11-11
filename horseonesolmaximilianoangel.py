# Pide el tamaño del tablero cuadrado (número de filas y columnas)
MAX = int(input("Ingrese el número de fila y columnas que desea (Será un tablero cuadrado, tendrá la misma cantida de filas y de columnas):  \n> "))

todas_soluciones = [] # Lista para almacenar las soluciones.

# Función validación.
def valida(tablero, candidato, x, y):
    #Verifica si la posición alcanzada desde x, y con el candidato este dentro del tablero y se encuentre vacía.
    posx = [-2,-1,1,2,2,1,-1,-2]  # Lista con los desplazamientos en fila para cada movimiento del caballo
    posy = [1,2,2,1,-1,-2,-2,-1]   # Lista con los desplazamientos en columna para cada movimiento del caballo
    nx = x + posx[candidato - 1]  # Calcula la nueva fila sumando el desplazamiento correspondiente
    ny = y + posy[candidato - 1]  # Calcula la nueva columna sumando el desplazamiento correspondiente
    if(nx<0 or nx>=MAX):  # Si la nueva fila está fuera del rango del tablero
        return False  # Movimiento inválido
    if(ny<0 or ny>=MAX):  # Si la nueva columna está fuera del rango del tablero
        return False  # Movimiento inválido
    if(tablero[nx][ny]!=0):  # Si la casilla de destino no está vacía (ya fue ocupada)
        return False  # Movimiento inválido
    return True  # Si ninguna condición anterior se cumplió, el movimiento es válido

# Función para la siguiente posición
def siguiente_posicion(tablero, candidato, x,y):
    # Devuelve la posicion nx, ny alcanzada desde x, y con el candidato.
    posx = [-2,-1,1,2,2,1,-1,-2]  # Desplazamientos en fila iguales a los usados en valida()
    posy = [1,2,2,1,-1,-2,-2,-1]   # Desplazamientos en columna iguales a los usados en valida()
    nx = x + posx[candidato - 1]  # Calcula la nueva fila
    ny = y + posy[candidato - 1]  # Calcula la nueva columna
    return nx, ny  # Retorna las coordenadas de la siguiente posición

# Función final
def final(tablero):
    for i in range(MAX):  # Recorre todas las filas del tablero
        for j in range(MAX):  # Recorre todas las columnas del tablero
            if(tablero[i][j]==0):  # Si encuentra alguna casilla igual a 0 (vacía)
                return False  # El tablero no está completo, retorna False
    return True  # Si no encontró casillas vacías, el tablero está completo

# Función para buscar x, y.
def buscar_xy(tablero, contador):
    for i in range(MAX):  # Recorre filas
        for j in range(MAX):  # Recorre columnas
            if(tablero[i][j]==contador):  # Si la casilla tiene el número buscado
                return i, j  # Devuelve fila y columna donde está ese número

# Función para la solución.
def solucion(tablero):

    candidato = 1 ; solucion = False ; x = 0; y = 0; contador = 1  # Inicializa variables: candidato, flag de solución, coordenadas y contador
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]  # Crea un tablero auxiliar lleno de ceros del mismo tamaño
    tablero[x][y] = contador  # Marca la primera casilla (0,0) con el contador inicial (1)

    while candidato <= 8:  # Bucle principal: intenta candidatos 1..8 hasta encontrar solución
        if(valida(tablero, candidato, x, y)):  # Si el candidato actual es válido desde la posición x,y
            nx, ny = siguiente_posicion(tablero, candidato, x, y)  # Calcula la siguiente posición según el candidato
            tablero[nx][ny] = contador + 1  # Marca la nueva posición con el siguiente número del recorrido
            if seleccion == "1":  # Si el usuario pidió ver la traza
                mostrar_tablero(tablero)  # Muestra el tablero actual con la traza parcial
            if final(tablero):  # Si el tablero quedó completo (no hay ceros) 
                todas_soluciones.append([fila[:] for fila in tablero]) # A la lista "todas_soluciones" se le agregan las soluciones encontradas.
                if seleccion == "3":
                    mostrar_tablero(tablero)
                    tablero[nx][ny] = 0 
                else:
                    return True
            else:
                tablero_aux[x][y] = candidato; x = nx; y = ny; contador += 1  # Guarda el candidato usado, avanza a nx,ny y aumenta contador
                candidato = 1  # Resetea candidato al inicio (1)
                continue
        
        candidato += 1  # Si el candidato no es válido, pasa al siguiente candidato

        while candidato == 9 and not (x==0 and y==0):  # Si ya probó todos los candidatos (1..8) y no está en la casilla inicial, retrocede
            tablero[x][y] = 0  # Desmarca la casilla actual (la vacía)
            contador -= 1  # Decrementa el contador porque retrocede
            nx, ny = buscar_xy(tablero, contador)  # Busca la posición donde quedó el último contador válido
            candidato = tablero_aux[nx][ny] + 1  # Recupera el siguiente candidato a probar desde el tablero auxiliar
            tablero_aux[nx][ny] = 0  # Limpia la marca en el tablero auxiliar
            x = nx; y = ny  # Retrocede la posición actual a nx,ny
            if seleccion == "1":  # Si se pidió ver la traza
                mostrar_tablero(tablero)  # Muestra el tablero durante el retroceso

    return solucion  # Devuelve True si encontró solución, False si no

#Función que muestra el tablero
def mostrar_tablero(tablero):
    for i in range(MAX):  # Recorre filas
        for j in range(MAX):  # Recorre columnas
            print(f"{tablero[i][j]:3}", end = " ")  # Imprime cada valor, un mínimo de 3 espacios por cada casilla, para que queden todas alineadas
        print("")  # Salto de línea al terminar cada fila
    print("")  # Línea en blanco adicional para separar tableros

def una_solucion():
    if(solucion(tablero) == True):  # Llama a la función solucion(tablero) y verifica si retornó True
        print("\nHay al menos 1 solución posible. \n")  # Mensaje de éxito si existe solución
        mostrar_tablero(tablero)  # Muestra el tablero solución
    else:
        print("\nNo hay una solución posible. \n")  # Mensaje si no se encontró ninguna solución    

### Main ###

# Muestra el menú de opciones hasta que se ingrese 1, 2 o 3
while True:
    print("""
|==============Opciones del caballo==============|
    1.- Quiero ver la traza (Solo 1 solución).
    2.- Quiero solo la solución.
    3.- Salir.
|================================================|
 """)  # Imprime el menú de opciones
    
    seleccion = input("Ingrese la opción que desea usar:  \n> ")  # Lee la opción elegida por el usuario
    if seleccion in ("1", "2", "3"):  # Si la opción es 1, 2 o 3
        break  # Sale del bucle y continúa
    else:
        print("Error, opción invalida.")  # Mensaje cuando la opción no es válida


tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] # Crea el tablero (matriz) inicial lleno de ceros

if seleccion == "1": # Si "seleccion" es igual a 1 ejecuta lo que tiene en su interior.
    if solucion == 1:  # (Esta línea no tiene efecto útil: compara la función con 1) Se deja tal cual.
        mostrar_tablero(tablero)  # Mostraría el tablero si la condición fuera verdadera (no lo será)    
    una_solucion() # Llama la función "una_solucion"

elif seleccion == "2": # Si "seleccion" es igual a 2 ejecuta lo que tiene en su interior.
    una_solucion() # Llama la función "una_solucion".

elif seleccion == "3":
    print("Saliendo del programa...") # Imprime el mensaje cuando "seleccion" es igual a 3




