'''script descripcion: number race
Dev: Juan Erazo
Date: 13-09-2024
'''

import random

def solicitar_numero_jugadores():
    while True:
        try:
            jugadores = int(input("Ingrese la cantidad de jugadores (2-4): "))
            if 2 <= jugadores <= 4:
                return jugadores
            else:
                print("Por favor, ingrese un número entre 2 y 4.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def seleccionar_nivel_tablero():
    while True:
        print("\nSeleccione el nivel de tablero:")
        print("1. Nivel básico (20 posiciones)")
        print("2. Nivel intermedio (30 posiciones)")
        print("3. Nivel avanzado (50 posiciones)")
        print("4. Nivel experto (100 posiciones)")
        
        try:
            nivel = int(input("Ingrese el número del nivel: "))
            if nivel == 1:
                return 20
            elif nivel == 2:
                return 30
            elif nivel == 3:
                return 50
            elif nivel == 4:
                return 100
            else:
                print("Opción no válida. Por favor, elija un nivel entre 1 y 4.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def main():
    jugadores = solicitar_numero_jugadores()
    meta = seleccionar_nivel_tablero()
    posiciones = [0] * jugadores
    pares_consecutivos = [0] * jugadores

    while True:
        for i in range(jugadores):
            input(f"\nTurno del jugador {i + 1}. Presiona Enter para lanzar los dados...")
            dado1, dado2 = lanzar_dados()
            print(f"Jugador {i + 1} lanzó: {dado1} y {dado2}")

            if dado1 == dado2:
                pares_consecutivos[i] += 1
                print(f"¡Par! ({dado1} y {dado2}) - Pares consecutivos: {pares_consecutivos[i]}")
            else:
                pares_consecutivos[i] = 0  # Reinicia si no es par

            posiciones[i] += dado1 + dado2

            print(f"Jugador {i + 1} avanza a la posición {posiciones[i]}")

            # Verifica condiciones de victoria
            if pares_consecutivos[i] == 3:
                print(f"¡Jugador {i + 1} gana directamente por 3 pares consecutivos!")
                return
            elif posiciones[i] >= meta:
                print(f"¡Jugador {i + 1} ha llegado a la meta y gana!")
                return

if __name__ == "__main__":
    main()