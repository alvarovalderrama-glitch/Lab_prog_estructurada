# Gato

a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = " " # Inicializacion de las posiciones del gato vacias
turno = "X" # El primer turno sera para la X

def mostrar(): # Esto es para formar la tabla del gato e imprimirla
        print(f"{a1}|{a2}|{a3}") # Fila A
        print("-+-+-")
        print(f"{b1}|{b2}|{b3}") # Fila B
        print("-+-+-")
        print(f"{c1}|{c2}|{c3}") # Fila C

for _ in range(9):
        mostrar()
        pos = input(f"Turno de {turno}, elige (a1..c3): ").lower() # Aqui se vera a quien le toca el turno y quien debe jugar colocando una coordenada

        if pos == "a1" and a1 == " ": a1 = turno
        elif pos == "a2" and a2 == " ": a2 = turno
        elif pos == "a3" and a3 == " ": a3 = turno
        elif pos == "b1" and b1 == " ": b1 = turno
        elif pos == "b2" and b2 == " ": b2 = turno
        elif pos == "b3" and b3 == " ": b3 = turno
        elif pos == "c1" and c1 == " ": c1 = turno
        elif pos == "c2" and c2 == " ": c2 = turno
        elif pos == "c3" and c3 == " ": c3 = turno
        else:
            print("Posición inválida.") # Si usa una posicion ya usada o un termino que no sean (a1...c3) sera invalidado el turno y tendra que repetir
            continue

        # Revisar Ganador
        lineas = [
            (a1,a2,a3), (b1,b2,b3), (c1,c2,c3), # Filas
            (a1,b1,c1), (a2,b2,c2), (a3,b3,c3), # Columnas
            (a1,b2,c3), (a3,b2,c1)              # Diagonales
        ]
        for l in lineas:
            if l[0] == l[1] == l[2] != " ":
                mostrar() # Mostrara el tablero final
                print("Gana", turno) # imprimira el ganador y terminara el juego
                exit() #Final del juego

        turno = "O" if turno == "X" else "X" # Cambiar de jugadores despues de cada turno

mostrar()
print("Empate") # En caso de empate se imprimira un mensaje que diga empate y terminara el juego
