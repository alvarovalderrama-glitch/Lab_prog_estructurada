# Toque y Fama (con historial de intentos)

import random

secreto = "".join(random.sample("0123456789", 4)) # Genera un número secreto de 4 dígitos distintos

intentos = []  # Guardará tu historial: [(intento, toque, fama), ...]

print("=== JUEGO: TOQUE Y FAMA ===") # Titulo del juego
print("Adivina el número secreto de 4 cifras (todas diferentes)") 

while True:
    intento = input("\nTu número: ") # Solicita al jugador que ingrese un número

    # Validar el formato del número
    if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4: # Valida que el número tenga 4 dígitos únicos
        print("Número inválido. Debe tener 4 cifras distintas.") # Si no cumple con las condiciones se le indicara que el numero es invalido
        continue

    # Calcular Fama y Toque
    fama = sum(1 for i in range(4) if intento[i] == secreto[i]) #  Cuenta cuántos dígitos están en la posición correcta
    toque = sum(1 for c in intento if c in secreto) - fama # Cuenta cuántos dígitos correctos que están mal posicionados

    # Guardar en historial
    intentos.append((intento, toque, fama))

    # Mostrar historial
    print("\n--- Historial ---")
    for i, (num, t, f) in enumerate(intentos, start=1):
        print(f"{i:02d}) {num} → Toque: {t}, Fama: {f}")

    # Verificar si ganó
    if fama == 4: # Si el jugador tiene 4 famas correcta, adivinó el número
        print("\n🎉 ¡Felicidades! Adivinaste el número:", secreto)
        break #Fin del juego
