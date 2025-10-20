rut_string = input("escribe un rut sin puntos ni digito verificador: ")

# Convertimos el string (texto) a un numero entero
rut_numero = int(rut_string)

suma_total = 0
multiplicador = 2 

while rut_numero > 0:
    
    #sacamos el ultimo digito del numero
    ultimo_digito = rut_numero % 10
    
   
    suma_total = suma_total + (ultimo_digito * multiplicador)  # multiplicamos ese digito por el multiplicador y lo sumamos
    
    
    rut_numero = rut_numero // 10 #quitamos el ultimo digito del numero
    
    
    multiplicador = multiplicador + 1 #avanzamos el multiplicador para el siguiente digito
    
    
    if multiplicador == 8:  #si el multiplicador llega a 8, lo reiniciamos a 2
        multiplicador = 2

resto = suma_total % 11 #dividimos la suma total por 11 y nos quedamos con el RESTO

resultado = 11 - resto #a 11 le restamos el resto

#mostrar resultado, si es 11, 0 si es 10, K

digito_verificador = "" #creamos una variable vacia para almacenar el digito 
if resultado == 11:
    digito_verificador = '0'
elif resultado == 10:
    digito_verificador = 'K'
else:
    #si es un numero normal, lo convertimos a string
    digito_verificador = str(resultado)
print("el digito verificador es: " + digito_verificador)
print("el RUT completo es: " + rut_string + "-" + digito_verificador)