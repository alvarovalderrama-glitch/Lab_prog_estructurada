def resolver_cuadrado_magico_3x3():
    N = 3
    SUMA_MAGICA = 15
    soluciones = [] # Aquí se guardarán todos los cuadrados mágicos encontrados
    
    # Inicialización del estado
    cuadrado = [[0] * N for _ in range(N)]
    usados = [False] * (N * N + 1) # Control de números 1 a 9
    
    # Lista con las 9 posiciones a llenar, en orden de (0,0) a (2,2)
    camino = [(f, c) for f in range(N) for c in range(N)] 
    
    # Puntero para la simulación iterativa (sustituye al índice de la pila)
    puntero_pila = 0 

    while puntero_pila >= 0:
        
        # 1. Condición de Éxito: Se llenaron las 9 celdas
        if puntero_pila == N * N:
            # Verificar la última condición (Diagonal Secundaria)
            if (cuadrado[0][2] + cuadrado[1][1] + cuadrado[2][0]) == SUMA_MAGICA:
                #guarda una copia de la solucion encontrada
                soluciones.append([row[:] for row in cuadrado]) 
            puntero_pila -= 1
            continue

        # Obtener las coordenadas de la celda actual (basada en el puntero)
        f, c = camino[puntero_pila] 
        
        # 2. Deshacer Estado Anterior (si retrocedimos aquí)
        # Esto prepara la celda para probar el siguiente número.
        valor_anterior = cuadrado[f][c]
        if valor_anterior != 0:
            usados[valor_anterior] = False
            cuadrado[f][c] = 0
            
        valor_inicial = valor_anterior + 1 # Empezar a buscar desde el número siguiente
        
        encontrado_valor = False
        
        # 3. Probar Opciones (números del 1 al 9)
        for num in range(valor_inicial, N * N + 1):
            if not usados[num]:
                
                # Asignar y Marcar
                cuadrado[f][c] = num
                usados[num] = True
                
                # --- PODA (Verificación temprana) ---
                poda_exitosa = True
                
                # Poda de Filas (solo si la fila está completa)
                if c == N - 1 and sum(cuadrado[f]) != SUMA_MAGICA:
                    poda_exitosa = False
                
                # Poda de Columnas (solo si la columna está completa)
                if f == N - 1 and sum(cuadrado[i][c] for i in range(N)) != SUMA_MAGICA:
                    poda_exitosa = False
                
                # Poda de Diagonal Principal (solo si está completa)
                if f == c == N - 1 and sum(cuadrado[i][i] for i in range(N)) != SUMA_MAGICA:
                    poda_exitosa = False
                if poda_exitosa:
                    encontrado_valor = True
                    puntero_pila += 1 
                    break # Detenemos la búsqueda de números y avanzamos de celda

                # Backtrack Inmediato (el número falló la poda)
                usados[num] = False
                cuadrado[f][c] = 0
                
        # 4. Retroceso: Si no se encontró ningún número válido en la celda
        if not encontrado_valor:
            puntero_pila -= 1 # Mover el puntero hacia atrás
            # La limpieza (un-do) ya se realizó al inicio del loop
            # antes de la búsqueda de 'num'.

    return soluciones

# --- Ejemplo de Uso ---
print("Buscando TODAS las soluciones del cuadrado mágico de 3x3...")
soluciones = resolver_cuadrado_magico_3x3()

if soluciones:
    print(f"¡Se encontraron {len(soluciones)} soluciones")
    print("--------------------------------")
    for i, solucion in enumerate(soluciones, 1):
        print(f"Solución #{i}:")
        for fila in solucion:
            print(fila)
        print("--------------------------------")
else:
    print("No se encontró solución.")