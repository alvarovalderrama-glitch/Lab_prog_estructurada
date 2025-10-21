while True:
    try:
        numero_decimal = int(input('Ingrese un numero entero no negativo:'))
        if numero_decimal>=0:
            break
        else:
            print('Fuera de intervalo')
    except ValueError:
        print('Dato no valido.')
        
lista_cifras = []

if numero_decimal == 0:
    print('El numero 0 en binario es 0')
else:
    aux_decimal = numero_decimal
    while aux_decimal > 0:
        resto = aux_decimal%2
        aux_decimal = aux_decimal//2
        lista_cifras.append(str(resto))
    lista_cifras.reverse()
    numero_binario = int(''.join(lista_cifras))
    print(f'El numero {numero_decimal} en binario es {numero_binario}')