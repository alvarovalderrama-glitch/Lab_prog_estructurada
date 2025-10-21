def validar_rut(rut):
    rut = rut.replace(".","").replace("-", "")

    rut_numero = rut[:-1]
    rut_dv = rut[-1].upper()

    if not rut_numero.isdigit():
        return False

    secuencia = [2,3,4,5,6,7]
    suma = 0
    for i,digito in enumerate(reversed(rut_numero)):
        suma += int(digito) * secuencia[i% len(secuencia)]

    dv_calculado = 11- (suma %11)

    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado == 10:
        dv_calculado = "K"
    else:
        dv_calculado = str(dv_calculado)

    return rut_dv == dv_calculado

rut = input("Ingresa tu rut como (ej: 12.345.678-9): ")
if validar_rut(rut):
    print("el rut es valido")
else:
    print("El rut es invalido")
