# Inicialización del mapa
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
 
# Mostrar el mapa en la pantalla
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
     
# Hacer una jugada en la casilla
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
 
# Programa principal
game_over = False
player1 = True
 
while not game_over:
 
    # 1. Mostrar el mapa
    print_maps()
 
    # 2. Preguntar al jugador dónde hacer la jugada
    if player1:
        symbol = "X"
        step = int(input("Jugador 1, tu jugada: "))
    else:
        symbol = "O"
        step = int(input("Jugador 2, tu jugada: "))
 
    step_maps(step, symbol)  # hacer la jugada en la casilla indicada
    win = get_result()  # determinar el ganador
    if win:
        game_over = True
    else:
        game_over = False
 
    player1 = not player1        
 
# El juego ha terminado. Mostrar el mapa. Anunciar al ganador.        
print_maps()
print("Ganó", win)
