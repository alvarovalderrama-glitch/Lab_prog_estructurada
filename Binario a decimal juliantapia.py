while True:
    try:
        numero_binario = int(input('Ingrese un numero en modulo 2 (binario):'))
        if numero_binario>=0 and set(list(str(numero_binario))) in [{'0','1'},{'0'},{'1'}]:
            break
        else:
            print('El numero no es binario o es negativo.')
    except ValueError:
        print('Dato no valido.')

lista_cifras = list(str(numero_binario))
lista_cifras.reverse()
numero_decimal = 0
for i in range(0,len(lista_cifras)):
    suma = int(lista_cifras[i])*2**i
    numero_decimal = suma + numero_decimal
print(f'El numero {numero_binario} es {numero_decimal} en decimal.')