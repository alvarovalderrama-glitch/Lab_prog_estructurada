
import random

DIGITOS = 3

numero_secreto = "" 

for _ in range(DIGITOS):
    # genera un dígito aleatorio (un número entre 0 y 9)
    digito_aleatorio = random.randint(0, 9)
    # agrega ese dígito (como texto) a nuestro número secreto
    numero_secreto = numero_secreto + str(digito_aleatorio)

print('adivivina el numero de ' + str(DIGITOS) + " dígitos.")
print("Tienes 10 intentos para adivinarlo.")

intentos = 0
famas = 0 #la fama es el digito correcto en la posicion correcta


while famas != DIGITOS and intentos < 10: #el juego se repite mientras NO tengas 3 famas Y tengas menos de 10 intento
    
    print("Intento " + str(intentos + 1))
    
    # pedimos el numero al Jugador
    intento_str = input("cual es tu numero: ")
    
    # intento, se valida el numero
    while len(intento_str) != DIGITOS or not intento_str.isdigit():
        print("debe ser un numero de " + str(DIGITOS) + " digitos.")
        intento_str = input(" cual es tu numero ")
    
    # se resetean los contadores para este intento
    famas = 0
    toques = 0 # el 'toque' es el digito correcto en la posicion INCORRECTA
    
    # listas para guardar los digitos que NO son fama
    lista_secreto_sobrantes = []
    lista_intento_sobrantes = []

 #buscar famas
    for i in range(DIGITOS):
        # si el digito en la posicion i es igual en ambos
        if numero_secreto[i] == intento_str[i]:
            famas = famas + 1
        else:
            #  si no es fama se guarda
            lista_secreto_sobrantes.append(numero_secreto[i])
            lista_intento_sobrantes.append(intento_str[i])

    #buscar toques
    # recorremos los digitos que sobraron del intento
    for digito_intento in lista_intento_sobrantes:
        
        # si ese digito esta en la lista de sobrantes del secreto
        if digito_intento in lista_secreto_sobrantes:
            toques = toques + 1
            # lo borramos de la lista de sobrantes
            lista_secreto_sobrantes.remove(digito_intento)
            
    # imprime el resultado del intento
    print("famas: " + str(famas))
    print("toques: " + str(toques))
    
    # sumamos un intento
    intentos = intentos + 1

if famas == DIGITOS:
    print("ganaste")
    print('adivinaste el numero' + numero_secreto)
else:
    print('perdiste')
    print('se te acabaron los intentos')
    print("el nuermo de la maquina era: " + numero_secreto)