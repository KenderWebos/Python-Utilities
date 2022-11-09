import random

#CONSTANTES
CANT_MIN_JUGADORES = 4
CANT_MAX_JUGADORES = 16

#VARIABLES
cantJugadores = 0
cantRondas = 0

bestPlayPerRound = []

#FUNCIONES
def getRandom():
    numeros = [1,2,3,4,5,6]
    return random.choice(numeros)

#CAPTURA DE DATOS INICIALES
while(cantJugadores < CANT_MIN_JUGADORES or cantJugadores > CANT_MAX_JUGADORES):
    cantJugadores = int(input("Ingrese la cantidad de jugadores: "))
    if(cantJugadores < CANT_MIN_JUGADORES or cantJugadores > CANT_MAX_JUGADORES):
        print("La cantidad de jugadores debe ser entre 4 y 16")

while(cantRondas < 1):
    cantRondas = int(input("Ingrese la cantidad de rondas: "))
    if(cantRondas < 1):
        print("La cantidad de rondas debe ser mayor a 0")

#INICIO DE LA APLICACION
print("\n-----INICIANDO EL JUEGO-----\n")

for i in range(cantRondas):
    print(f">> -------- Ronda: {i+1} ----- <<")
    for j in range(cantJugadores):
        listPerPlayer = []
        print("Jugador: ", j+1)
        for k in range(5):
            listPerPlayer.append(getRandom())
        print(listPerPlayer)
    print("-----------------------------")