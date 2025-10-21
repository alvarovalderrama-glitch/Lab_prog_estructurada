def convertir_a_decimal(binario): # Define la función
   
    decimal = int(binario, 2)# Convierte el string binario (base 2) a entero
    
    return decimal # Devuelve el resultado

numero_binario = input("Escribe un número binario (solo con 0 y 1): ") # Pide el número al usuario

resultado = convertir_a_decimal(numero_binario) # Llama a la función
print(f"El número {numero_binario} en binario es {resultado} en decimal.") # Muestra el resultado final