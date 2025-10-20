import random #hace que la maquina genere un numero aleatorio
Intento = 1
Intmax = 5
Acertado = False

print('Bienvenido a toque y fama')
Opcion = input('¿Prefieres elegir el número o que la maquina lo elija? (si/no): ') #

if Opcion.lower() in ['s','si']:
    N_Secreto = ".join(random.sample('0123456789', 5))" 
    print('La maquina ha creado el número secreto')
else:
    N_Secreto = input('escriba su número secreto(son 5 digitos): ') #deja escribir el numero personalizado

    
while Intento <= Intmax and not Acertado: #dice el numero de intentos del juego
    print(f'\nIntento {Intento} de {Intmax}')
    Jugador = input('intente adivinar el número: ')

    for i in range(5): #evalua el numero ingresado para saber si se acertó
        if Jugador[i] == N_Secreto[i]:
            print(Jugador[i],'está en esa posicion')
        elif Jugador[i] in N_Secreto:
            print(Jugador[i], 'está en el número pero en otra posición')
        else:
            print(Jugador[i], 'no está en el número')

    if Jugador == N_Secreto: #da la condicion de si se adivina el número o no se adivina
        print('¡Has adivinado el número!')
        Acertado = True
        break
    else:
        print('El número es incorrecto, intentalo de nuevo')
        Intento += 1

if not Acertado: #muestra el caso de si se agotan los intentos
  print('\nYa no te quedan más intentos')