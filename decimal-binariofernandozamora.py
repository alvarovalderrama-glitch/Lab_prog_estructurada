def convertir_a_binario(numero): #define la funcion
    resultado = bin(numero)[2:] #convierte en binarioo
    return resultado #devuelve el string binario

numero_decimal_texto = input("Escribe un número decimal: ") #aca pide el numero al usuario

numero_entero = int(numero_decimal_texto) #convierte el texto a un numero entero

resultado_en_binario = convertir_a_binario(numero_entero) #llama a la funcion con el numero ingresado

print(f"El número {numero_entero} en decimal es {resultado_en_binario} en binario.") #muestra el numero final
