def digito_verificador_rut():
    aux = int(input("Ingrese su rut sin puntos y sin el digito verificador: "))
    suma = 0
    factor = 2
    while aux > 0:
        digito = aux % 10
        aux = aux // 10
        suma = suma + (digito * factor)
        factor = factor + 1

        if factor > 7:
            factor = 2
        
    

    resto = suma % 11
    valor = 11 - resto
    
    if valor == 10:
        print("el digito verificador es = K")
    elif valor == 11:
        print("el digito verificador es = 0")
    else:
        print(f"el digito verificador es = {valor}")
        
    
digito_verificador_rut()