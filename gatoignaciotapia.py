
#funcion que permite crear el tablero

def print_tablero(tablero):
   for row in tablero:
       print("  | ".join(row))
       print("-" * 9)

#checkea si la fila es la que fue la que gano
def check_winner(tablero,jugador):
   for row in tablero:
       if all(s == jugador for s in row):
           return True
   #checkea si la columna fue la que gano
   for col in range(3):
       if all(tablero[row][col]==jugador for row in range(3)):
           return True
    #checkea si la diagonal fue la que gano
   if all(tablero[i][i]== jugador for i in range(3)) or all(tablero[i][2-i]==jugador for i in range(3)):
       return True
   
   return False

#definicion de las variables

tablero = [[""for _ in range(3)] for _ in range(3)]
jugador='X'
#
for _ in range(9):
   print_tablero(tablero)
   row, col = map(int, input(f"jugador{jugador},introduzca una columna y fila(0-2):").split())  #
    #en caso de que alguna de las condiciones de victoria sean verdad, se imprime el mensaje al jugador quien haya ganado
   if tablero[row][col] == "":
       tablero[row][col] = jugador
       if check_winner(tablero,jugador):
           print_tablero(tablero)
           print(f"jugador {jugador}wins!")
           break
       jugador = 'O' if jugador == 'X' else 'X'
   else:
       print("Movimiento invalido!, porfavor introduzca una columna y fila valida!")
#caso en que haya un empate
else:
   print("It's a tie!")