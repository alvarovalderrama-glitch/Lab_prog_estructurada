# Variables globales
tablero = [0, 0, 0,
           0, 0, 0,
           0, 0, 0]
n=0

def valida(candidato, pos): # Verifica que el candidato no este duplicado
    for i in range(pos): # Revisa todas las posiciones ya visitadas 
        if tablero[i] == candidato: # Si se encuentra un duplicado
            return False # No es valido
    return True # Si el numero no se ha usado, entonces es valido

def verificar(): # Verificar si hay cuadrado magico
        suma = 15 # El resultado de las sumas
        # Verificar filas // Si la suma de cada una es distinta a la establecida, entonces es invalida
        if tablero[0] + tablero[1] + tablero[2] != suma: 
            return False
        if tablero[3] + tablero[4] + tablero[5] != suma: 
            return False
        if tablero[6] + tablero[7] + tablero[8] != suma: 
            return False
        # Verificar columnas // Si la suma de cada una es distinta a la establecida, entonces es invalida
        if tablero[0] + tablero[3] + tablero[6] != suma:
            return False
        if tablero[1] + tablero[4] + tablero[7] != suma:
            return False
        if tablero[2] + tablero[5] + tablero[8] != suma: 
            return False
        # Verificar diagonales // Si la suma de cada una es distinta a la establecida, entonces es invalida
        if tablero[0] + tablero[4] + tablero[8] != suma:
            return False
        if tablero[2] + tablero[4] + tablero[6] != suma:
            return False
        return True
        
def mostrar_tablero():
        global n
        n = n+1 # Se suma una al contador de cuadrados.
        print(f'Cuadrado magico numero {n}: ') # Muestra el numero del cuadrado, seguido a eso, muestra el tablero.
        print(tablero[0], tablero[1], tablero[2]) 
        print(tablero[3], tablero[4], tablero[5])
        print(tablero[6], tablero[7], tablero[8])
        print()

def backtracking():
    pos = 0 # Pos actual en el tablero.
    candidato = 1 # Numero a probar
    
    while pos >= 0: # Mientras no se haya retrocediddo completamente 
        if candidato <= 9 and valida(candidato, pos): # Si el candidato es menor a 9 y es valido
            tablero[pos] = candidato # Coloca el numero del candidato en la pos. actual del tablero
            if pos == 8: # Si se llego a la ultima pos.
                if verificar(): # Verifica que el cuadrado sea magico
                    mostrar_tablero() # Se muestra el cuadrado magico.
                candidato += 1 # Prueba el sig. numero en la misma posicion
            else:
                pos += 1 # Avanza a la sig. posicion del tablero
                candidato = 1 # Reinicia el candidato para probar desde 1 en la nueva pos.
        else:
            if candidato > 9: # Si ya se probaron todos los candidatos
                tablero[pos] = 0 # Se limpia la pos actual.
                pos -= 1 # Retrocede una pos.
                if pos >= 0: # Si todavia se esta dentro del tablero
                    candidato = tablero[pos] + 1 # Toma el sig. numero de la pos. anterior.
            else:
                candidato += 1 # Prueba con el sig. numero en la misma posicion.


print("Cuadrados mágicos encontrados:\n")
backtracking() # Inicia la búsqueda de todos los cuadrados mágicos
