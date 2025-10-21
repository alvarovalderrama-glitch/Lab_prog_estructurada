
#Juego del Gato (Tic Tac Toe)
class TicTacToe:
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador_actual = 'X'
        self.movimientos = 0
    
    #Función para imprimir el tablero
    def imprimir_tablero(self):
        """Imprime el tablero actual"""
        print("\n   |   |   ")
        for i in range(3):
            print(f" {self.tablero[i][0]} | {self.tablero[i][1]} | {self.tablero[i][2]} ")
            if i < 2:
                print("___|___|___")
            else:
                print("   |   |   ")
        print()
    
    #Función para hacer un movimiento en el Juego
    def hacer_movimiento(self, fila, columna):
        """Realiza un movimiento en el tablero"""
        if 0 <= fila < 3 and 0 <= columna < 3 and self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = self.jugador_actual
            self.movimientos += 1
            return True
        return False
    
    #Función para cambiar de jugador
    def cambiar_jugador(self):
        """Cambia al siguiente jugador"""
        self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
    
    #Función para verificar el ganador
    def verificar_ganador(self):
        """Verifica si hay un ganador"""
        # Verificar filas
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != ' ':
                return self.tablero[fila][0]
        
        # Verificar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != ' ':
                return self.tablero[0][columna]
        
        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            return self.tablero[0][2]
        
        return None
    
    # Función para verificar si el tablero está lleno
    def tablero_lleno(self):
        """Verifica si el tablero está lleno"""
        return self.movimientos == 9
    
    # Función principal del juego
    def jugar(self):
        """Función principal del juego"""
        print("¡Bienvenido al juego del Gato!")
        print("Instrucciones:")
        print("- Las posiciones van de 0 a 2 para filas y columnas")
        print("- Ejemplo: 0,0 es la esquina superior izquierda")
        print("- 1,1 es el centro")
        print("- 2,2 es la esquina inferior derecha\n")

    # Bucle principal del juego    
        while True:
            self.imprimir_tablero()
            print(f"Turno del jugador: {self.jugador_actual}")
            
            try:
                fila = int(input("Ingresa la fila (0-2): "))
                columna = int(input("Ingresa la columna (0-2): "))
                
                if self.hacer_movimiento(fila, columna):
                    ganador = self.verificar_ganador()
                    
                    if ganador:
                        self.imprimir_tablero()
                        print(f"¡Felicidades! El jugador {ganador} ha ganado!")
                        break
                    
                    if self.tablero_lleno():
                        self.imprimir_tablero()
                        print("¡Empate! El juego ha terminado.")
                        break
                    
                    self.cambiar_jugador()
                else:
                    print("Movimiento inválido. Esa casilla ya está ocupada o está fuera del rango.")
            
            except ValueError:
                print("Por favor, ingresa números válidos (0, 1, 2).")

# Ejecutar el juego
if __name__ == "__main__":
    juego = TicTacToe()
    juego.jugar()

# Fin del código del juego del Gato
#El self se utiliza para referirse a la instancia actual de la clase y acceder a sus atributos y métodos.
#__init__ es un método especial en Python que se llama automáticamente cuando se crea una nueva instancia de una clase. 
            #Se utiliza para inicializar los atributos del objeto.   