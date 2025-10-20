#binario a decimal
def binario_a_decimal(binario):
    decimal=int(binario,2)
    print("El numero decimal es:",decimal)

#decimal a binario
def decimal_a_binario(decimal):
    print("su numero de decimal a binario es: "+ (bin(decimal)[2:]))



binario=binario_a_decimal(int(input("ingrese un numero binario: ")))



decimal=int(int(input("ingrese un numero decimal entero: ")))
