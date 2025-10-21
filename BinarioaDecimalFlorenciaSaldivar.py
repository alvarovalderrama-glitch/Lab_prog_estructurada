while True: #Permite que el codigo se repita hasta que se ingrese un numero valido
    binario = input("Ingresa un número binario: ")  #Pregunta por el binario que se quiere transformar a decimal

    valido= True    #Asume que el numero fue valido
    for digito in binario:  #Recorre cada digito del binario para verificar que se cumpla  
        if digito !="0" and digito !="1":   #Si el digito es distinto de uno o de cero
            valido= False   
            break
    if valido:
        decimal = int(binario,2)    #Convierte de binario a decimal
        print("El numero decimal es:", decimal)     #Muestra el resultado
        break
    else: 
        print("Solo se permiten numeros de 0 y 1")  #Si no fue valido muestra esta linea