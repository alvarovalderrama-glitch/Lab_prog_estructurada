#Rut (dígito verificador)
# Cálculo del DV chileno con módulo 11 y validador opcional.

def limpiar_rut(texto):                           # Función para limpiar formato
    texto = texto.replace(".", "").replace("-", "")# Quita puntos y guión
    return texto.strip()                           # Elimina espacios

def calcular_dv(numero_str):                       # Calcula DV para un RUT sin DV
    suma = 0                                       # Acumulador para la suma ponderada
    factor = 2                                     # Factor inicial (2 a 7 y se repite)
    for dig in reversed(numero_str):               # Recorre de derecha a izquierda
        suma += int(dig) * factor                  # Multiplica dígito por factor
        factor = 2 if factor == 7 else factor + 1  # Cicla 2..7
    resto = 11 - (suma % 11)                       # Resto según regla
    if resto == 11:                                # Caso resto 11 → DV 0
        return "0"
    if resto == 10:                                # Caso resto 10 → DV K
        return "K"
    return str(resto)                              # Otro caso → número

def formatear_rut(numero_str, dv):                 # Pone guion y puntos básicos
    cuerpo = numero_str                             # (simple: sin puntos de miles)
    return f"{cuerpo}-{dv}"                         # Devuelve con guion

def validar_rut(rut_completo):                     # Valida un RUT con DV
    limpio = limpiar_rut(rut_completo)             # Limpia entrada
    if not limpio[:-1].isdigit():                  # Verifica que cuerpo sea numérico
        return False                               
    numero, dv = limpio[:-1], limpio[-1].upper()   # Separa cuerpo y DV
    return calcular_dv(numero) == dv               # Compara DV calculado

# --------- Ejecución interactiva ----------
op = input("1) Calcular DV  2) Validar RUT  -> ").strip()  # Menú simple
if op == "1":                                      # Opción calcular
    cuerpo = input("Ingresa el RUT sin DV (solo números): ").strip()
    if cuerpo.isdigit():                           # Verifica numérico
        dv = calcular_dv(cuerpo)                   # Calcula DV
        print("RUT:", formatear_rut(cuerpo, dv))   # Muestra resultado
    else:
        print("Entrada inválida.")
elif op == "2":                                    # Opción validar
    rut_in = input("Ingresa el RUT con DV (ej: 12345678-5): ").strip()
    print("VÁLIDO" if validar_rut(rut_in) else "INVÁLIDO") # Informa
else:
    print("Opción no válida.")
