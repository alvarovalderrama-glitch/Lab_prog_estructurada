def validar_rut(rut):
    # Eliminar puntos y guiones
    rut= rut.replace(".", "").replace("-","")

    # Separar el número y el dígito verificador
    rut_numero = rut[:-1]
    rut_dv = rut[-1].upper()
    # Validar que el número sea solo dígitos
    if not rut_numero.isdigit():
        return False

# Multiplicación de los dígitos por la secuencia [2, 3, 4, 5, 6, 7]
    secuencia =[2, 3, 4, 5, 6, 7]
    suma = 0
    for i, digito in enumerate(reversed(rut_numero)):
        suma += int(digito) * secuencia [i % len(secuencia)]
    # Cálculo del dígito verificador
    dv_calculado = 11 - (suma % 11)
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(dv_calculado)
    
    # Comparar el DV calculado con el proporcionado
    return rut_dv == dv_calculado

# Ejemplo de uso
rut = "21.842.128-8"
if validar_rut(rut):
    print(f"El RUT {rut} es válido.")
else:
    print(f"El RUT {rut} es inválido.")