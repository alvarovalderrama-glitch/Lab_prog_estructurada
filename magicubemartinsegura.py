cuadrado = [0 for i in range(9)] # Se crea un cuadrado de tamaño 3
#numero magico
NMAGICO=int(input("Ingrese cualquier numero multiplo de 3 mayor o igual a 15: "))
#numeros para la diagonal 
diagonal = [((NMAGICO//3)-1)+i for i in range(3)][::-1]
for i in range(2,7,2):
    cuadrado[i] = diagonal[(i//2)-1] # Se completa la diagonal con una suma de 3 numeros consecutivos

def mostrartabla(tabla):
    for i in range(3):
        print(f"|{tabla[3*i]} |{tabla[(3*i)+1]} |{tabla[(3*i)+2]} ")

def backtracking(posActual,copia):
    valorValido = False 
    for pos in [abs(posActual-1),abs(posActual -3)]: # Se recorren las esquinas de la matriz
        num,valorValido = comprobacion(pos,copia) # Se comprueba si existe algun valor valido 
        if valorValido:
            copia[pos] = num 
        else:
            break # Si no existe nigun valor valido se sale del bucle
    if valorValido and posActual == 8: #Si el bucle termina con un valor valido y empezo en la posicion 8, significa que el cuadrado se completo
        mostrartabla(copia)
        exit()
    elif posActual ==0: backtracking(8,copia)

def comprobacion(pos,copia): 
    if pos <4:#Primero se revisa la esquina izquierda
        if pos == 1:#posicion 1
            resta =NMAGICO-sumaFilas(0) 
        else:#posiicon 3
            resta = NMAGICO -sumaColumnas(0) #En la posicion 1 y 3 solo se consideran la suma horizontal de la posicion 1 y la suma vertical de la posicion 3
        return (resta,True) if 0<resta< NMAGICO and resta not in copia else (0,False) # Se comprueba si el valor sea menor al numero magico y mayor a 0, tambien se comprueba que no haya sido puesto en la tabla
    else:#Esquina derecha
        if pos == 7:
            resta = NMAGICO - sumaFilas(2)
            return (resta,True) if resta == NMAGICO -sumaColumnas(1) and resta not in copia else (0,False)
        else:

            resta = NMAGICO -sumaFilas(1)
            return (resta,True) if resta == NMAGICO -sumaColumnas(2) and resta not in copia else (0,False)

def sumaFilas(filaN):
    inicio = 3*filaN
    return sum(copia[inicio:inicio+3])

def sumaColumnas(ColumnasN):
    inicio = ColumnasN
    return sum(copia[inicio:7+inicio:3])

for valorEsquina in range(1,NMAGICO-4):
    copia=cuadrado.copy()
    copia[0] = valorEsquina
    resta = NMAGICO -sum(copia[0:9:4])

    if 0<resta< NMAGICO and resta not in copia:
        copia[8] = resta #Se completa la otra diagonal
        backtracking(0,copia)
