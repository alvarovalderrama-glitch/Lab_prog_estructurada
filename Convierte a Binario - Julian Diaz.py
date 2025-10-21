n = int(input("Ingrese un número decimal: "))

binario = ""
if n == 0:
    binario = "0"

while n > 0:
    resto = n % 2
    binario = str(resto) + binario
    n //= 2

print(binario)
