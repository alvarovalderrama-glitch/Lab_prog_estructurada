class NReinas:
    def __init__(self, n):
        self.n = n
        self.soluciones = []
        # El tablero se representa como una lista: indice=fila, valor=columna
        self.tablero = [-1] * n

    def _es_seguro(self, fila, col):
        """Verifica si (fila, col) es un lugar seguro."""
        for f_ant in range(fila):
            c_ant = self.tablero[f_ant]
            # Mismo columna (c) o misma diagonal
            if c_ant == col or abs(fila - f_ant) == abs(col - c_ant):
                return False
        return True

    def _buscar_soluciones(self, fila):
        """Método recursivo de Vuelta Atrás."""
        if fila == self.n:
            # Caso base: ¡Solución encontrada!
            self.soluciones.append(list(self.tablero))
            return

        for col in range(self.n):
            if self._es_seguro(fila, col):
                self.tablero[fila] = col  # Colocar reina
                self._buscar_soluciones(fila + 1)  # Ir a la siguiente fila
                # El 'backtracking' es implícito: la siguiente iteración de 'for' probará otra columna.

    def resolver(self):
        """Función pública para iniciar la resolución."""
        self._buscar_soluciones(0)
        return self.soluciones

def imprimir_solucion(sol, n):
    """Muestra una solución de forma visual."""
    for col in sol:
        linea = ["♕" if i == col else "." for i in range(n)]
        print(" ".join(linea))

# --- Ejecución ---
try:
    N = int(input("Tablero N x N: "))
    
    if N <= 3 and N != 1:
        print(f"N={N}: 0 soluciones.")
    else:
        # Crea una instancia y resuelve
        juego = NReinas(N)
        sols = juego.resolver()
        
        print(f"\nTotal: {len(sols)} soluciones para N={N}.")
        
        if sols:
            print("\nPrimera Solución (♕ = Reina):")
            imprimir_solucion(sols[0], N)
            
except ValueError:
    print("Error: Ingresa un número entero.")