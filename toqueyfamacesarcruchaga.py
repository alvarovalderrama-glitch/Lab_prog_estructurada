import random #hice un modulo para generar numeros 

DIGITOS = 4 # Variable para la longitud del número secreto

def generar_secreto():
    """Genera un número secreto de 4 dígitos sin repeticiones."""
    numeros = list('0123456789') # Creamos una lista de dígitos
    random.shuffle(numeros) # Mezclamos la lista
    
    # Tomamos los primeros DIGITOS elementos, que serán nuestro secreto
    secreto = "".join(numeros[:DIGITOS])
    return secreto # Devolvemos el valor

def contar_toques_y_famas(secreto, intento):
    """Cuenta los toques y famas de un intento."""
    famas = 0
    toques = 0

    # Usamos 'for' para recorrer los dígitos del número secreto 
    for i in range(DIGITOS): 
        #revisa si el dígito y la posición son correctos
        if secreto[i] == intento[i]:
            famas += 1
        #revisa si el dígito existe en el secreto 
        # pero la posición es distinta
        elif intento[i] in secreto:
            toques += 1
            
    return toques, famas # Devuelve ambos valores

def jugar_toque_y_fama():
    """Función principal del juego."""
    secreto = generar_secreto()
    intentos = 0
    
    print("a jugar papus (4 digitos distintos)")
    
    # Bucle 'while' que se repite mientras no haya 4 Famas 
    while True: 
        intento = input(f"\nIntento #{intentos + 1}. Ingresa un número de {DIGITOS} dígitos: ")
        
        # Validación de longitud y tipo usando if/else 
        if len(intento) != DIGITOS or not intento.isdigit():
            print(f"Error: Debes ingresar exactamente {DIGITOS} dígitos.")
            continue # Vuelve al inicio del bucle 
            
        intentos += 1
        toques, famas = contar_toques_y_famas(secreto, intento)
        
        print("Resultado: " + str(toques) + " Toques, " + str(famas) + " Famas.")
        
        if famas == DIGITOS:
            print(f"\n¡GANASTE! Lo hiciste en {intentos} intentos. El número era {secreto}.")
            break # Sale del bucle infinito 'while True' 

if __name__ == "__main__":
    jugar_toque_y_fama()