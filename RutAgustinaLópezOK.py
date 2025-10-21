def calcular_digito_verificador(rut):
    """
    Calcula el dígito verificador de un RUT chileno
    """
    rut = str(rut).replace('.', '').replace('-', '')  # Limpiar formato
    rut = rut[:-1] if len(rut) > 1 else rut  # Remover dígito verificador si existe
    
    multiplicador = 2
    suma = 0
    
    # Recorrer el RUT de derecha a izquierda
    for digito in reversed(rut):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    
    # Calcular dígito verificador
    resto = suma % 11
    digito_verificador = 11 - resto
    
    # Casos especiales
    if digito_verificador == 11:
        return '0'
    elif digito_verificador == 10:
        return 'K'
    else:
        return str(digito_verificador)

rut=(input("Ingrese el RUT sin dígito verificador: "))
digito = calcular_digito_verificador(rut)
print(f"RUT: {rut}-{digito}")  
