import random

def jugar_toque_y_fama_simple():
    """Versión simplificada del juego Toque y Fama (4 dígitos, ilimitados intentos)."""
    
    # 1. Generar número secreto de 4 dígitos únicos (como cadena)
    digitos = list("0123456789")
    random.shuffle(digitos)
    secreto = "".join(digitos[:4])
    
    intentos = 0
    print("--- Toque y Fama ---")
    print("Adivina el número de 4 dígitos únicos.")
    # print(f"DEBUG: {secreto}") # Descomenta para ver la respuesta
    
    while True:
        intentos += 1
        
        # 2. Pedir y validar la entrada
        while True:
            intento = input(f"\nIntento #{intentos}. Tu número (4 dígitos únicos): ")
            if len(intento) == 4 and intento.isdigit() and len(set(intento)) == 4:
                break
            print("Entrada inválida. Debe ser un número de 4 dígitos únicos.")
        
        toques = 0
        famas = 0
        
        # 3. Contar Famas y Toques
        
        # Famas (dígito y posición correctos)
        for i in range(4):
            if intento[i] == secreto[i]:
                famas += 1
        
        # Toques (dígito correcto, posición incorrecta)
        # Se cuentan los dígitos y se restan las Famas para no contarlas 
        comunes = len(set(intento) & set(secreto))
        toques = comunes - famas
        
        # 4. Mostrar resultado
        if famas == 4:
            print(f"\n¡¡¡GANASTE!!! El número era {secreto}.")
            print(f"Lo adivinaste en {intentos} intentos.")
            break
        else:
            print(f"Resultado: {toques} Toques, {famas} Famas")

# Iniciar el juego
if __name__ == "__main__":
    jugar_toque_y_fama_simple()