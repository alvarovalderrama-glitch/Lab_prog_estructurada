numero=int(input("Ingresa un número entero positivo: "))
binario=""
while numero>0:
    binario=str(numero%2)+binario
    numero=numero//2
print(f"El número en binario es: {binario}")