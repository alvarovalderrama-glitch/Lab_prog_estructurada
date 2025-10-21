rut = int(input('Rut: '))
suma = 0
m = 2
while rut > 0:
    digito = rut % 10
    suma += digito * m
    m += 1
    if m > 7:
        m = 2
    rut //= 10

resto = 11 - (suma % 11)

if resto == 11:
    dv = "0"
elif resto == 10:
    dv = "K"
else:
    dv = str(resto)

print(dv)
