def binario_y_decimal(binario):
    decimal = 0
    for bit in binario:
        decimal=decimal * 2 + int(bit)
    return decimal
binario = input('ingrese su consulta binaria: ')
decimal = binario_y_decimal(binario)
print(decimal)