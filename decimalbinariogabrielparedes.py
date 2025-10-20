def decimal_a_binario():
    aux = int(input("Ingrese un número decimal: "))
    contador = 1
    suma = 0
    
    while(aux > 1):
        resto = aux % 2
        aux = aux // 2
        digito = contador * resto
        suma= suma + digito
        contador = contador * 10
    resto = aux
    resto = resto * contador
    suma = suma + resto
    print(f"el numero binario es: {suma}")
    
decimal_a_binario()