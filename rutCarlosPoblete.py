rut = int(input("Ingresa Rut, sin digito verificador: "))
aux = rut
suma = 0
factor = 2
while(aux > 0):
    digito = aux % 10
    aux = int((aux-digito)/10)
    suma = suma+(digito*factor)
    factor = factor+1
    if factor == 8:
        factor = 2
suma = suma+(aux*factor)
resto = 11-(suma % 11)
if resto == 10:
    print("Su rut es: ",rut,"- K")
else:
    if resto == 11:
        print("Su rut es: ",rut,"- 0")
    else:
        print("Su rut es: ",rut,"-",resto)