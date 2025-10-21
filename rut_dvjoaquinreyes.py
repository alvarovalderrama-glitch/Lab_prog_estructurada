def calcular_dv(rut):
    rut = str(rut)
    secuencia = [2, 3, 4, 5, 6, 7]
    suma = 0
    for i, digito in enumerate(reversed(rut)):
        suma += int(digito) * secuencia[i % len(secuencia)]
    dv_calculado = 11 - (suma % 11)
    if dv_calculado == 11:
        return "0"
    elif dv_calculado == 10:
        return "K"
    else:
        return str(dv_calculado)
rut=int(input("Ingrese su RUT sin puntos ni guion y sin el ultimo digito: "))
dv = calcular_dv(rut)
print("El digito verificador es: " + dv)
