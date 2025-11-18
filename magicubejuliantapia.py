# Esta función es recursiva y permite calcular todas las permutaciones de una lista de elementos que se le entregue.
def permutar(lista):
    n = len(lista) # Numero de elementos de la lista
    lista_permutaciones = [] # Lista vacia que guarda las permutaciones
    if n == 1: # Condición de salida de la recursión. Si solo hay una elemento en la lista, se retorna la lista dentro de otra lista.
        return [lista]
    else:
        fijado = lista[0] # Se fija el primer elemento
        lista.remove(fijado) # Se remueve el elemento fijado de la lista
        permutaciones_fijado = permutar(lista) # Se calculan las permutaciones para los elementos de la lista sin el elemento fijado
        for i in range(len(permutaciones_fijado)): # for que recorre los indices de la lista permutaciones.
            permutacion = [fijado] + permutaciones_fijado[i] # Se define "permutacion", que agrega el fijado a la i-esima permutación.
            lista_permutaciones.append(list(permutacion)) # Se agrega "permutacion" a la lista de permutaciones.
            for j in range(len(permutacion)-1): # Este for mueve el fijado por la lista y agrega cada movimiento a la lista de permutaciones.
                permutacion[j] = permutacion[j+1]
                permutacion[j+1] = fijado
                lista_permutaciones.append(list(permutacion))
        return(lista_permutaciones) # Se retorna la lista de permutaciones para que sea ocupada por el proximo elemento fijado.

# Esta función verifica si una permutación de la lista de permutaciones es un cuadrado magico o no y entrega los cuadrados magicos en una lista.
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

# Esta función muestra los cuadrados magicos en la terminal.
def mostrar_cuadrados(lista):
    for cuadrado in lista:
        print()
        for i in range(3):
            print(f'{cuadrado[i*3]} | {cuadrado[i*3+1]} | {cuadrado[i*3+2]}')
        print()

# ------ MAIN
lista_elementos = [i+1 for i in range(9)] # Los elementos del cuadrado magico, que van del 1 al 9.
combinaciones = permutar(lista_elementos) # Se calculan las permutaciones
cuadrados_magicos = comprobar_CMs(combinaciones) # Se determinan los cuadrados magicos
print('¿Cuantos cuadrados magicos resultan al combinar los numeros del 1 al 9?')
if cuadrados_magicos == []: # Si la lista de cuadrados magicos estuviera vacia, no hay cuadrados magicos con los elementos que definimos.
    print('Ninguno.')
else:
    mostrar_cuadrados(cuadrados_magicos)
    print(f'Hay {len(cuadrados_magicos)} cuadrados magicos.')
