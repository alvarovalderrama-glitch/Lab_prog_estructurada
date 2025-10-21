# Canridad de números a adivinar entre 1 y 9 
import random
MAX = int(input("ingrese la cantidad de números que desee adivinar (máximo 9): "))
while MAX > 9 or MAX < 1:
    print("INGRESE UN NÚMERO ENTRE 1 Y 9")
    MAX = int(input("ingrese la cantidad de números que desee adivinar (máximo 9): "))

# Generar lista de números aleatorios únicos entre 1 y 9
adivina = random.sample(range(1, 10), MAX)
print("Debes adivinar",MAX,"números ¡A JUGAR!")
tablero = ["*" for _ in range(MAX)]

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    print("\n" + "-" * (MAX * 5 + 1))
    for celda in tablero:
        print(f"| {celda:2}", end=" ")
    print("|")
    print("-" * (MAX * 5 + 1))
    print("")
    
aciertos = 0
contador = 0

# Función principal del juego
def jugar():
    global aciertos, contador
    while aciertos < MAX and contador < 5:
            mostrar_tablero(tablero)
            intentos = int(input("ingrese un número (1 al 9): "))
            while intentos < 1 or intentos > 9:
                print("ingrse un número valido (1 al 9)")
                intentos = int(input("ingrese un número (1 al 9)"))
                
            posición = int(input(f"ingrese la posición del número (1 a {MAX}): ")) - 1
            while posición < 0 or posición >= MAX:
                print(f"ingrese una posición valida entre 1 y {MAX}")
                posición = int(input(f"ingrese la posición del número (1 a {MAX}): ")) - 1
                
            contador += 1
            
            if adivina[posición] == intentos and tablero[posición] == "*":
                tablero[posición] = str(intentos)
                aciertos += 1
                print("OBTUVISTE UNA FAMA")
            elif intentos in adivina:
                print("OBTUVISTE UN TOQUE")
            else:
                print("ESE NÚMERO NO ESTÁ")
                
            if aciertos == MAX:
                print("GANASTE, el número era",adivina)
            elif contador == 5:
                print("PERDISTE, el número era", adivina)

 # Función para preguntar si se desea jugar nuevamente               
def jugar_nuevamente():
    while True:
        respuesta = input("¿Deseas jugar nuevamente? (si/no): ").strip().lower()
        if respuesta in ["si", "s", "sí"]:
            return True
        elif respuesta in ["no", "n"]:
            print("¡HASTA LUEGO, BUEN JUEGO!")
            return False
        else:
            print("Ingrese una respuesta válida (si/no).")

# Iniciar el juego
jugar()
jugar_otra_vez = jugar_nuevamente()
while jugar_otra_vez:
    # Reiniciar variables para un nuevo juego
    adivina = random.sample(range(1, 10), MAX)
    tablero = ["*" for _ in range(MAX)]
    aciertos = 0
    contador = 0
    jugar()
    jugar_otra_vez = jugar_nuevamente()