while True:
    decimal = input("Ingresa un numero decimal: ")  #pregunta por el numero decimal    
    if decimal.isdigit():   #verifica que sea un numero
        decimal = int(decimal)  #lo toma como entero
        print("el numero decimal es:", bin(decimal)[2:])    #Da el decimal si es que si se ingreso un numero valido
        break      
    else:
        print("solo debes ingresar numeros (sin espacios ni puntos)")    #Le dice al usuario que solo puede ingresar numeros 