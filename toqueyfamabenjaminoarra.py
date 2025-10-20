# Toque y Fama (con historial de intentos)

import random

# Genera un número secreto de 4 dígitos distintos
secreto = "".join(random.sample("0123456789", 4))

intentos = []  # Guardará tu historial: [(intento, toque, fama), ...]

print("=== JUEGO: TOQUE Y FAMA ===")
print("Adivina el número secreto de 4 cifras (todas diferentes)")

while True:
    intento = input("\nTu número: ")

    # Validar el formato del número
    if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
        print("Número inválido. Debe tener 4 cifras distintas.")
        continue

    # Calcular Fama y Toque
    fama = sum(1 for i in range(4) if intento[i] == secreto[i])
    toque = sum(1 for c in intento if c in secreto) - fama

    # Guardar en historial
    intentos.append((intento, toque, fama))

    # Mostrar historial
    print("\n--- Historial ---")
    for i, (num, t, f) in enumerate(intentos, start=1):
        print(f"{i:02d}) {num} → Toque: {t}, Fama: {f}")

    # Verificar si ganó
    if fama == 4:
        print("\n🎉 ¡Felicidades! Adivinaste el número:", secreto)
        break