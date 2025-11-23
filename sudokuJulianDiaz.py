import random

# ===========================================
#   FUNCIONES DEL SUDOKU
# ===========================================

def imprimir_sudoku(tablero):
    print("+-------+-------+-------+")
    for i in range(9):
        fila = "| "
        for j in range(9):
            if tablero[i][j] == 0:
                fila += ". "
            else:
                fila += str(tablero[i][j]) + " "
            if (j + 1) % 3 == 0:
                fila += "| "
        print(fila)
        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")

def valido(tablero, r, c, num):
    for x in range(9):
        if tablero[r][x] == num:
            return False
    for x in range(9):
        if tablero[x][c] == num:
            return False
    sr = (r // 3) * 3
    sc = (c // 3) * 3
    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if tablero[i][j] == num:
                return False
    return True

def resolver(tablero, soluciones, limite=20):
    if len(soluciones) >= limite:
        return
    for r in range(9):
        for c in range(9):
            if tablero[r][c] == 0:
                for num in range(1, 10):
                    if valido(tablero, r, c, num):
                        tablero[r][c] = num
                        resolver(tablero, soluciones, limite)
                        tablero[r][c] = 0
                return
    soluciones.append([fila[:] for fila in tablero])

# ===========================================
#      GENERAR LIMITES ENTRE 17 Y 30 TOTAL
# ===========================================

def generar_limites():
    while True:
        limites = [random.randint(0, 8) for _ in range(9)]
        total = sum(limites)
        if 17 <= total <= 30:
            return limites

# ===========================================
#      EXPORTAR SOLUCIONES
# ===========================================

def exportar_soluciones(tablero_inicial, soluciones, nombre_archivo="Soluciones"):
    with open(f"{nombre_archivo}.txt", "w") as f:
        f.write("=== TABLERO INICIAL ===\n")
        f.write("+-------+-------+-------+\n")
        for i in range(9):
            fila = "| "
            for j in range(9):
                val = tablero_inicial[i][j]
                fila += (str(val) if val != 0 else ".") + " "
                if (j + 1) % 3 == 0:
                    fila += "| "
            f.write(fila + "\n")
            if (i + 1) % 3 == 0:
                f.write("+-------+-------+-------+\n")

        f.write(f"\nSe encontraron {len(soluciones)} solución(es):\n\n")

        for idx, sol in enumerate(soluciones, 1):
            f.write(f"--- SOLUCIÓN {idx} ---\n")
            f.write("+-------+-------+-------+\n")
            for i in range(9):
                fila = "| "
                for j in range(9):
                    fila += str(sol[i][j]) + " "
                    if (j + 1) % 3 == 0:
                        fila += "| "
                f.write(fila + "\n")
                if (i + 1) % 3 == 0:
                    f.write("+-------+-------+-------+\n")
            f.write("\n")

tablero = [[0]*9 for _ in range(9)]

print("=== SUDOKU VACÍO ===")
imprimir_sudoku(tablero)

limites = generar_limites()

print("Límites por fila (0 a 8 números por fila).")
print("Límites generados por fila:", limites)
print("Total permitido de numeros a ingresar:", sum(limites), "\n")
print("Ingresar 0 para saltar espacio, -1 para terminar la entrada\n")

cantidad_total = 0
salir_anticipado = False

for r in range(9):
    if salir_anticipado:
        break
        
    print("Fila", r + 1, "— Puede ingresar hasta", limites[r], "números.")
    usados_fila = 0

    for c in range(9):
        if salir_anticipado:
            break
            
        while True:
            if usados_fila >= limites[r]:
                tablero[r][c] = 0
                break

            try:
                val = int(input("Valor en columna " + str(c+1) + " (0-9, -1 para resolver): "))
            except:
                print("Debe ser un número.")
                continue

            if val == -1:
                salir_anticipado = True
                print("Saliendo de la entrada de datos...")
                break

            if val < 0 or val > 9:
                print("Debe estar entre 0 y 9, o -1 para salir.")
                continue

            if val != 0:
                if not valido(tablero, r, c, val):
                    print("No valido. Intenta otro.")
                    continue
                usados_fila += 1
                cantidad_total += 1

            tablero[r][c] = val
            break

    if not salir_anticipado:
        imprimir_sudoku(tablero)

print("Tablero final ingresado:")
imprimir_sudoku(tablero)

if cantidad_total == 0:
    print("Sudoku vacío no puede resolverse.")
else:
    soluciones = []
    print("Primeras 20 soluciones")
    resolver(tablero, soluciones, limite=20)

    if len(soluciones) == 0:
        print("El sudoku NO TIENE solución.")
    elif len(soluciones) == 1:
        print("\n El sudoku tiene una única solución:")
        imprimir_sudoku(soluciones[0])
    else:
        print(f"\n El sudoku tiene múltiples soluciones ({len(soluciones)}).")
        print("Se exportarán a Soluciones.txt.")
        exportar_soluciones(tablero, soluciones)
