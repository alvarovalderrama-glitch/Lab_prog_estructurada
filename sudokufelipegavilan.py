#Sudoku resolviendo desde backtraking desde una plantilla en archivo .txt

# Esta función lee un archivo .txt que contiene un sudoku
# de 9 filas y 9 columnas con números entre 0 y 9.
def leer_sudoku_desde_archivo(nombre_archivo):
   #Guarda el tablero
    tablero = []
    #El archivo es abierto en modo "r"
    archivo = open(nombre_archivo, "r")

    #Lee linea por linea
    for linea in archivo:

        #Se quitan saltos de linea y espacios extras
        linea_limpia = linea.strip()

        #Se separan los numeros por espacio
        numeros_como_texto = linea_limpia.split()

        #Converte cada numero a entero
        fila = []
        for numero in numeros_como_texto:
            fila.append(int(numero))

        tablero.append(fila)

    archivo.close()

    return tablero


# Esta función imprime el sudoku de manera ordenada
def imprimir_sudoku(tablero):
    for fila in range(9):

        #Separa de manera horizontal cada 3 filas
        if fila % 3 == 0 and fila != 0:
            print("------+-------+------")

        for col in range(9):

            #Separa de manera vertical cada 3 columnas
            if col % 3 == 0 and col != 0:
                print("|", end=" ")

            print(tablero[fila][col], end=" ")

        print("")  #Salto de línea
    print("")      #Linea extra


#Verifica si es valido poner un numero en tablero por filas
def posicion_es_valida(tablero, fila, col, numero):

    #Revisar la fila completa
    for c in range(9):
        if tablero[fila][c] == numero:
            return False

    #Revisa la columna completa
    for f in range(9):
        if tablero[f][col] == numero:
            return False

    #Calcula el inicio del caudrande de 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (col // 3) * 3

    #Revisa el cuadrante 3x3
    for f in range(inicio_fila, inicio_fila + 3):
        for c in range(inicio_columna, inicio_columna + 3):
            if tablero[f][c] == numero:
                return False

    return True


#Funcion para resolver el sudoku
def resolver_sudoku(tablero, fila, col):

    #Si fila llega a 9 significa que el sudoku esta completo
    if fila == 9:
        return True

    #Calcula la siguiente posicion
    if col == 8:
        siguiente_fila = fila + 1
        siguiente_col = 0
    else:
        siguiente_fila = fila
        siguiente_col = col + 1

    #Si la casilla actual esta ocupada
    if tablero[fila][col] != 0:
        return resolver_sudoku(tablero, siguiente_fila, siguiente_col)

    #Si está vacia intentar numeros del 1 al 9
    for numero in range(1, 10):

        if posicion_es_valida(tablero, fila, col, numero):

            tablero[fila][col] = numero  #Coloca numero

            if resolver_sudoku(tablero, siguiente_fila, siguiente_col):
                return True

            tablero[fila][col] = 0  
    return False


#Funcion para guardar el sudoku resuelto en un archivo nuevo .txt
def guardar_sudoku_en_archivo(tablero, nombre_archivo):
    archivo = open(nombre_archivo, "w")

    for fila in range(9):
        linea = ""

        for col in range(9):
            linea += str(tablero[fila][col]) + " "

        archivo.write(linea.strip() + "\n")

    archivo.close()


#Programa principal
#La plantilla tiene que estar con el nombre
nombre_archivo = "sudoku.txt"

print("Buscando la Plantilla")
tablero_sudoku = leer_sudoku_desde_archivo(nombre_archivo)
#Imprieme la plantilla 
print("\nSudoku inicial:")
imprimir_sudoku(tablero_sudoku)

#Se resuelve el tablero imprimiento el resultado
if resolver_sudoku(tablero_sudoku, 0, 0):
    print("Sudoku resuelto:\n")
    imprimir_sudoku(tablero_sudoku)
#Guarda en nuevo archivo el sudoku resuelto
    print("Guardando solución en sudoku_resuelto.txt")
    guardar_sudoku_en_archivo(tablero_sudoku, "sudoku resuelto.txt")
    print("Archivo guardado\n")

else:
    print("El sudoku no tiene solución")
