def decimal_a_binario(decimal):
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario
decimal = int (input('Ingrese su decimal: '))
binario = decimal_a_binario(decimal)
print(binario)