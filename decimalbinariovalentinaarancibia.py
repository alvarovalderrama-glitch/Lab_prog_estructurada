número = int(input("ingrese un número: "))
binario = ""
while número > 0:
    binario = str(número % 2) + binario
    número = número // 2
print('el número binario es', binario)