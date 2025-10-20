# Inicialización del tablero
maps = [1,2,3,
        4,5,6,
        7,8,9]
 
# Inicialización de las líneas ganadoras
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
# Mostrar el tablero en pantalla
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])
     
# Hacer un movimiento en una casilla
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
# Obtener el resultado actual del juego
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win
 
# Inteligencia artificial: buscar línea con la cantidad necesaria de X y O en las líneas ganadoras
def check_line(sum_O, sum_X):
 
    step = ""
    for line in victories:
        o = 0
        x = 0
 
        for j in range(0, 3):
            if maps[line[j]] == "O":
                o += 1
            if maps[line[j]] == "X":
                x += 1
 
        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]
                 
    return step
 
# Inteligencia artificial: elegir el movimiento
def AI():        
 
    step = ""
 
    # 1) si en alguna de las líneas ganadoras hay 2 de sus figuras y 0 del oponente, colocar en esa línea
    step = check_line(2, 0)
 
    # 2) si en alguna de las líneas ganadoras hay 2 figuras del oponente y 0 suyas, bloquear esa línea
    if step == "":
        step = check_line(0, 2)        
 
    # 3) si hay 1 figura suya y 0 del oponente en una línea, colocar en esa línea
    if step == "":
        step = check_line(1, 0)           
 
    # 4) si el centro está libre, ocupar el centro
    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5           
 
    # 5) si el centro está ocupado, ocupar la primera casilla
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1           
   
    return step
 
# Programa principal
game_over = False
human = True
 
while not game_over:
 
    # 1. Mostrar el tablero
    print_maps()
 
    # 2. Preguntar al jugador dónde hacer el movimiento
    if human:
        symbol = "X"
        step = int(input("Humano, tu turno: "))
    else:
        print("La computadora hace su movimiento: ")
        symbol = "O"
        step = AI()
 
    # 3. Si la computadora encontró dónde hacer el movimiento, jugar. Si no, es un empate.
    if step != "":
        step_maps(step, symbol) # hacer el movimiento en la casilla indicada
        win = get_result() # determinar el ganador
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print("¡Empate!")
        game_over = True
        win = "la amistad"
 
    human = not human        
 
# El juego ha terminado. Mostrar el tablero. Anunciar el ganador.
print_maps()
print("Ganó", win)
