def binario_a_decimal():
    aux = int(input("Ingrese un número binario: "))
    digito = 0
    factor = 0
    contador = 0
    suma = 0
    
    while aux > 0:
        digito = aux % 10
        aux = (aux - digito) // 10
        factor = 2 ** contador
        suma = suma + (digito * contador)
        contador = contador + 1
        
    factor = 2 ** contador
    aux = aux * factor
    suma = suma + aux
    

    print(f"El número decimal es: {suma}")

binario_a_decimal()