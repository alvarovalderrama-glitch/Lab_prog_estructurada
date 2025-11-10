LINEAS = [(0,1,2),(3,4,5),(6,7,8),
          (0,3,6),(1,4,7),(2,5,8),
          (0,4,8),(2,4,6)]

def crear_tablero():
    return [' ']*9

def mostrar(t):
    print(f" {t[0]} | {t[1]} | {t[2]} ")
    print("---+---+---")
    print(f" {t[3]} | {t[4]} | {t[5]} ")
    print("---+---+---")
    print(f" {t[6]} | {t[7]} | {t[8]} ")

def ganador(t, f):
    for a,b,c in LINEAS:
        if t[a]==t[b]==t[c]==f:
            return True
    return False

def lleno(t):
    return not any(c==' ' for c in t)

def jugar():
    t = crear_tablero()
    turno = 'X'
    mostrar(t)
    while True:
        try:
            i = int(input(f"Turno {turno}. Elija 1-9: ")) - 1
        except:
            print("Entrada invalida"); continue
        if i < 0 or i > 8 or t[i] != ' ':
            print("Movimiento invalido"); continue
        t[i] = turno
        mostrar(t)
        if ganador(t, turno):
            print("Gana", turno); break
        if lleno(t):
            print("Empate"); break
        turno = 'O' if turno == 'X' else 'X'

if __name__ == "__main__":
    jugar()
