import random

# --- 1. UTILIDADES Y LÓGICA BASE ---

def crear_tablero():
    return [' '] * 10

def dibujar_tablero(tablero):
    print('-------------')
    print(f'| {tablero[1]} | {tablero[2]} | {tablero[3]} |')
    print('-------------')
    print(f'| {tablero[4]} | {tablero[5]} | {tablero[6]} |')
    print('-------------')
    print(f'| {tablero[7]} | {tablero[8]} | {tablero[9]} |')
    print('-------------')

def verificar_ganador(tablero, marca):
    # Lista concisa de todas las líneas ganadoras
    lineas = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), 
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    
    # Comprueba si la marca ocupa alguna línea
    return any(tablero[a] == marca and tablero[b] == marca and tablero[c] == marca 
               for a, b, c in lineas)

def verificar_empate(tablero):
    return ' ' not in tablero[1:]

# --- 2. MANEJO DE MOVIMIENTOS ---

def obtener_movimiento_humano(tablero, jugador):
    """Pide al jugador una posición válida."""
    while True:
        try:
            mov = int(input(f'Turno de {jugador}. Elige casilla (1-9): '))
            if 1 <= mov <= 9 and tablero[mov] == ' ':
                return mov
            print('Casilla no válida o ya ocupada. Intenta de nuevo.')
        except ValueError:
            print('Entrada inválida. Debe ser un número.')

def obtener_movimiento_pc(tablero, pc_marca):
    """IA simple: 1. Ganar, 2. Bloquear, 3. Esquina, 4. Centro, 5. Lado."""
    jugador_marca = 'X' if pc_marca == 'O' else 'O'
    
    # 1. Chequear si la PC puede ganar o si el jugador puede ganar (y bloquear)
    for marca in [pc_marca, jugador_marca]:
        for i in range(1, 10):
            if tablero[i] == ' ':
                tablero_copia = list(tablero)
                tablero_copia[i] = marca
                if verificar_ganador(tablero_copia, marca):
                    return i
    
    # 3-5. Estrategia: Esquina > Centro > Lado
    movs = [i for i in [1, 3, 7, 9, 5, 2, 4, 6, 8] if tablero[i] == ' ']
    return movs[0] if movs else 0

# --- 3. BUCLE PRINCIPAL CON SELECCIÓN DE MODO ---

def jugar_gato():
    print('¡Bienvenido al Gato! 🐱')
    
    # Selección de modo simplificada
    while True:
        modo = input('Jugar: (1) vs PC o (2) vs Humano: ')
        if modo in ('1', '2'): break
        print('Opción no válida.')
        
    tablero = crear_tablero()
    jugador_actual = 'X'

    while True:
        dibujar_tablero(tablero)
        
        # Determinar y ejecutar movimiento
        if modo == '2' or jugador_actual == 'X':
            # Modo Humano (ambos turnos) o Turno Humano de 'X' (modo PC)
            movimiento = obtener_movimiento_humano(tablero, jugador_actual)
        else: # modo == '1' y jugador_actual == 'O' (Turno PC)
            print("Turno de la PC...")
            movimiento = obtener_movimiento_pc(tablero, 'O')
        
        tablero[movimiento] = jugador_actual
        
        # Verificar fin de juego
        if verificar_ganador(tablero, jugador_actual):
            dibujar_tablero(tablero)
            ganador = 'PC 🤖' if modo == '1' and jugador_actual == 'O' else f'Jugador {jugador_actual} 🎉'
            print(f'¡{ganador} ha ganado!')
            break
        
        if verificar_empate(tablero):
            dibujar_tablero(tablero)
            print('¡Empate! 🤝')
            break
            
        # Cambiar de turno
        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

# --- INICIO ---
if __name__ == '__main__':
    while True:
        jugar_gato()
        if input('¿Jugar de nuevo? (s/n): ').lower().startswith('n'):
            break