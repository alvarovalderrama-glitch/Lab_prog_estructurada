import random
#Genera un número secreto de 4 digitos
secreto=''.join(random.sample("0123456789", 4))
print("Adivina el número que contiene 4 dígitos")

while True:
    #Solicita intento al jugador
    intento=input("ingrese números: ")
    #Valida que el número tenga 4 dígitos
    if len(intento) != 4:
        print("Deben ser 4 dígitos")
        continue

    # Valida que el intento contenga solo dígitos
    if not intento.isdigit():
        print("Solo se permiten números")
        continue
        
    # Valida que no haya dígitos repetidos
    if len(set(intento)) != 4:
        print("Los dígitos no deben repetirse")
        continue

    #Calcula números correctos en posiciones correctas(famas)
    famas=sum(1 for i in range(4) if intento[i]==secreto[i])

    #Calcula números correctos en posiciones incorrectas(toques)
    toques=sum(1 for d in intento if d in secreto)-famas
    #Mostrar resultado del intento
    print(f"famas: {famas} toques: {toques}")
    
    #Si todas son famas, el jugador gana
    if famas==4:
        print(f"¡Correcto! era {secreto}, ¡Ganaste!")
        break