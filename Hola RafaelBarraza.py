#Si hacemos este programa para que solo se pueda ejecutar con numeros colocamos Spam= int (input(>>>>>))
#Pero si queremos colocar cualquier cosa y que no nos de error podemos poner en los if Spam == '1': y asi co el 2 o los números que queramos colocar
spam =input('Ingrese un número:')

print(spam)
if spam == '1':      #Al colocar '1' permite colocar uno como un numero, esto sirve para que no nos de error al no colocar solo numeros(esto pasa cuando colocamos int(input('Ingrese un numero:')))#
    print('Hola')

elif spam == '2':    #En caso de colocar 1 o 2 se mostrara en la consola hola
    print('Hola')
else:                   #Caso contrario nos mostrara en consola saludos, esto pasa si colocamos cualquier cosa.
    print('Saludos')
