import random

def mostrar_tablero(n):
    print()
    print(f" {n[1]} | {n[2]} | {n[3]}")
    print("---+---+---")
    print(f" {n[4]} | {n[5]} | {n[6]}")
    print("---+---+---")
    print(f" {n[7]} | {n[8]} | {n[9]}")
    print()

def casilla_libre(n, pos):
    return n[pos] not in ("X", "O")

def hay_tres_en_linea(n, s):
    # Filas
    if n[1] == s and n[2] == s and n[3] == s: return True
    if n[4] == s and n[5] == s and n[6] == s: return True
    if n[7] == s and n[8] == s and n[9] == s: return True
    # Columnas
    if n[1] == s and n[4] == s and n[7] == s: return True
    if n[2] == s and n[5] == s and n[8] == s: return True
    if n[3] == s and n[6] == s and n[9] == s: return True
    # Diagonales
    if n[1] == s and n[5] == s and n[9] == s: return True
    if n[3] == s and n[5] == s and n[7] == s: return True
    return False

def turno_de(mov):
    if mov % 2 == 1:
        return "X"
    else:
        return "O"


print("=== Gato ===")
ganador = "empate"  
print("¿Quieres que la MÁQUINA juegue con 'X' (y empiece)?")
print("Escribe 1 para 'Sí' (máquina = X) o 0 para 'No' (tú = X).")
while True:
    eleccion_txt = input("eleccion (0/1): ").strip()
    if eleccion_txt in ("0", "1"):
        eleccion = int(eleccion_txt)
        break
    else:
        print("Entrada no válida. Escribe 0 o 1.")
if eleccion == 1:
    maquina = "X"
    jugador = "O"
else:
    maquina = "O"
    jugador = "X"


n = ["?"] + [str(i) for i in range(1, 10)]


mov = 1


mostrar_tablero(n)
while mov < 10:
    simbolo_turno = turno_de(mov) 

    if simbolo_turno == maquina:
     
        libres = [i for i in range(1, 10) if casilla_libre(n, i)]
        mov_maquina = random.choice(libres)
        n[mov_maquina] = maquina

        # Mostrar tablero y chequear ganador
        mostrar_tablero(n)
        if hay_tres_en_linea(n, maquina):
            ganador = "perdiste"
            break

    else:
        #Turno JUGADOR
        while True:
            cas = input(f"Tu turno ({jugador}). Escoge una casilla [1-9]: ").strip()
            if cas in "123456789" and casilla_libre(n, int(cas)):
                pos = int(cas)
                n[pos] = jugador
                break
            print("Entrada inválida o casilla ocupada. Intenta de nuevo.")

       
        mostrar_tablero(n)
        if hay_tres_en_linea(n, jugador):
            ganador = "ganaste"
            break

    mov = mov + 1  

print("Resultado:", ganador)