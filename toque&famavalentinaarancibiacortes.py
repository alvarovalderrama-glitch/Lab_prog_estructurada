# =======================
#  JUEGO DE TOQUE & FAMA
# =======================
# Objetivo:
# El jugador debe adivinar una secuencia de números aleatorios (sin repetirse).
# - "FAMA": número y posición correctos.
# - "TOQUE": número correcto, pero en otra posición.
# - Tiene máximo 5 intentos para adivinar todos los números.
# ===============================
import random

def jugar(): #función principal del juego toque & fama
    
    #EL JUGADOR DECIDE QUÉ CANTIDAD DE NÚMEROS DESEA ADIVINAR
    MAX = int(input("ingrese la cantidad de números que desee adivinar (máximo 9): "))
    while MAX > 9 or MAX < 1: #valida el rango
        print("INGRESE UN NÚMERO ENTRE 1 Y 9")
        MAX = int(input("ingrese la cantidad de números que desee adivinar (máximo 9): "))

    adivina = random.sample(range(1, 10), MAX) #elige varios elementos aleatorios de la lista sin que se repitan
    print("Debes adivinar",MAX,"números ¡A JUGAR!")
    tablero = ["*" for _ in range(MAX)] #las casillas son incógnitas


    def mostrar_tablero(tablero): #función que crea el tablero
        print("\n" + "-" * (MAX * 5 + 1))
        for celda in tablero:
            print(f"| {celda:2}", end=" ")
        print("|")
        print("-" * (MAX * 5 + 1))
        print("")
    
    aciertos = 0 #cantidad de famas
    contador = 0 #número de intentos

    while aciertos < MAX and contador < 5:
            mostrar_tablero(tablero)
            #número candidato
            intentos = int(input("ingrese un número (1 al 9): "))
            while intentos < 1 or intentos > 9:
                print("ingrese un número valido (1 al 9)")
                intentos = int(input("ingrese un número (1 al 9)"))
            #posición del número candidato
            posición = int(input(f"ingrese la posición del número (1 a {MAX}): ")) - 1
            while posición < 0 or posición >= MAX:
                print(f"ingrese una posición valida entre 1 y {MAX}")
                posición = int(input(f"ingrese la posición del número (1 a {MAX}): ")) - 1
                
            contador += 1 #número de intentos despúes de un intento
            
            if adivina[posición] == intentos and tablero[posición] == "*": #esto define si obtuvimos una fama
                tablero[posición] = str(intentos)
                aciertos += 1
                print("OBTUVISTE UNA FAMA") #número candidato & posición correcta
            elif intentos in adivina:
                print("OBTUVISTE UN TOQUE") #número candidato correcto & posición incorrecta
            else:
                print("ESE NÚMERO NO ESTÁ")
            #verifica si hay victoria
            if aciertos == MAX:
                print("GANASTE, el número era",adivina)
            elif contador == 5:
                print("PERDISTE, el número era", adivina)

def jugar_nuevamente(): #función que nos permite jugar nuevamente
    while True:
        respuesta = input("¿Deseas jugar nuevamente? (si/no): ").strip().lower()
        if respuesta in ["si", "s", "sí"]:
            return True
        elif respuesta in ["no", "n"]:
            print("¡HASTA LUEGO, BUEN JUEGO!")
            return False
        else:
            print("Ingrese una respuesta válida (si/no).")

#bucle principal del programa
while True: #mientras sea verdadero, jugaremos
    jugar()
    if not jugar_nuevamente(): #si jugar nuevamente es falso, el juego termina
        break
