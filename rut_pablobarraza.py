rut = input("Ingresa el RUT sin dígito verificador: ")
rut = rut[::-1]  # invertimos el RUT para multiplicar desde el último dígito
factor = 2
suma = 0

for d in rut:
    suma += int(d) * factor
    factor += 1
    if factor > 7:
        factor = 2

resto = 11 - (suma % 11)

if resto == 11:
    dv = '0'
elif resto == 10:
    dv = 'K'
else:
    dv = str(resto)

print("El dígito verificador es:", dv)


