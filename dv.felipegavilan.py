#Digito verificador
def calcular_dv(rut):
    rut = rut.strip().replace(".", "")
    suma, multiplo = 0, 2

    for digito in reversed(rut):
        suma += int(digito) * multiplo
        multiplo = 2 if multiplo == 7 else multiplo + 1

    resto = 11 - (suma % 11)
    if resto == 11:
        return "0"
    elif resto == 10:
        return "K"
    else:
        return str(resto)


rut = input("Ingrese su RUT sin dígito verificador: ")
dv = calcular_dv(rut)
print(f"El dígito verificador es: {dv}")
print(f"RUT completo: {rut}-{dv}")