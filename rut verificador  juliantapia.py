while True:
    try:
        rut = int(input('Ingrese un rut sin puntos ni el digito verificador:'))
        if rut in range(10**6,10**8):break
        else:
            print('El rut tiene un numero de digitos no valido.')
    except ValueError:
        print('Dato no valido')

rut_lista = list(str(rut))
rut_lista.reverse()
suma = 0

for i in range(2,len(rut_lista)+2):
    digito_rut = int(rut_lista[i-2])
    if i >= 8:
        i += -6
    producto = i*digito_rut
    suma += producto

resto = suma%11
verificar = 11-resto

if verificar == 11:
    verificar = 0
if verificar == 10:
    verificar = 'k'
    
print(f'El numero verificador de el rut {rut} es {verificar}')