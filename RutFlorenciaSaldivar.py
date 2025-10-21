def validar_rut(rut): #definimos la funcion
    rut = rut.replace(".", "").replace("-", "") #quitamos puntos y guines
    rut_numero = rut[:-1] # tomamos todos los caracteres numericos excepto el ultimo
    rut_dv = rut[-1].upper() # tomamos el ultimo caracter y lo pasamos a mayuscula

    if not rut_numero.isdigit(): # solo digitos
        return False # retorna falso

    secuencia = [2, 3, 4, 5, 6, 7] 
    suma = 0 # acumula la suma
    for i, digito in enumerate(reversed(rut_numero)): # Recorremos desde derecha a izquierda
           suma += int(digito) * secuencia[i % len(secuencia)] #aplica los factores en orden repetido
    dv_calculado = 11 - (suma % 11) # Formula para calcular el DV
    if dv_calculado == 11: 
        dv_calculado = '0' 
    elif dv_calculado == 10: 
        dv_calculado = 'K' #
    else: 
        dv_calculado = str(dv_calculado)

    return rut_dv == dv_calculado   #compara el dv entregado con el calculado

rut= input("Ingrese su rut:")
if validar_rut(rut):
    print(f"el rut {rut} es valido")
else:
    print(f"el rut {rut} es invalido")