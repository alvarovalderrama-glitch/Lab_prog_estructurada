def all_combinaciones(lista):
    n = len(lista)
    lista_combinaciones = []
    if n == 1:
        return (lista)
    elif n!=2:
        fijado = lista[0]
        lista.remove(fijado)
        combinaciones_fijado = all_combinaciones(lista)
        for i in range(len(combinaciones_fijado)):
            combinacion = [fijado] + combinaciones_fijado[i]
            lista_combinaciones.append(list(combinacion))
            for j in range(len(combinacion)-1):
                combinacion[j] = combinacion[j+1]
                combinacion[j+1] = fijado
                lista_combinaciones.append(list(combinacion))
        return(lista_combinaciones)
    else:
        x = lista[0]; y = lista[1]
        lista_combinaciones = [[x,y],[y,x]]
        return(lista_combinaciones)

def comprobar_CMs(lista):
    cuadrados_magicos = []
    for L in lista:
        f_1 = L[0] + L[1] + L[2]
        f_2 = L[3] + L[4] + L[5]
        f_3 = L[6] + L[7] + L[8]
        c_1 = L[0] + L[3] + L[6]
        c_2 = L[1] + L[4] + L[7]
        c_3 = L[2] + L[5] + L[8]
        d_1 = L[0] + L[4] + L[8]
        d_2 = L[2] + L[4] + L[6]
        if f_1 == f_2 == f_3 == c_1 == c_2 == c_3 == d_1 == d_2:
            cuadrados_magicos.append(L)
    return cuadrados_magicos

def mostrar_cuadrados(lista):
    for cuadrado in lista:
        print()
        for i in range(3):
            print(f'{cuadrado[i*3]} | {cuadrado[i*3+1]} | {cuadrado[i*3+2]}')
        print()

# ------ MAIN
lista_elementos = [i+1 for i in range(9)]
combinaciones = all_combinaciones(lista_elementos)
cuadrados_magicos = comprobar_CMs(combinaciones)
print('¿Cuantos cuadrados magicos resultan al combinar los numeros del 1 al 9?')
if cuadrados_magicos == []:
    print('Ninguno.')
else:
    mostrar_cuadrados(cuadrados_magicos)
    print(f'Hay {len(cuadrados_magicos)} cuadrados magicos.')