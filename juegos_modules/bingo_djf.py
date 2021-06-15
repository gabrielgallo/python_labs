import random
from random import randrange

def GenerarCartones(jugadores):
    listaCartones = list()
    for x in range(int(jugadores)):
        carton = list()
        for n in range(5):            
            while True:
                num = int(randrange(1,99))
                if num not in carton:
                    carton.append(num)
                    break
                else:                    
                    continue
        carton.sort()
        listaCartones.append(carton)
    return listaCartones
    
def SacarBolilla(listaBolillas):
    num = 0
    while True:
        bolilla = int(randrange(1,99))
        if bolilla not in listaBolillas:            
            listaBolillas.append(bolilla)
            break
        if num == 100:
            break
        num +=1
    return listaBolillas

def ExisteGanador(small, big):
    coincidencias = True
    for x in small:
        if x in big:
            continue
        else:
            return False
    return coincidencias


def Ganador(listaBolillas, listaCartones):
    jugador = 1
    for carton in listaCartones:
        if ExisteGanador(carton, listaBolillas):
            return jugador
        jugador += 1
    return 0

def PrintCartones(listaCartones):
    print("Lista de cartones")
    jugador = 1
    for carton in listaCartones:
        print(f"Carton del jugador {jugador}: {carton}")
        jugador += 1

def BingoStart():
    print("Bienvenido al Bingo")
    jugadores = input("Ingrese la cantidad de jugadores ")
    listaCartones = GenerarCartones(jugadores)
    listaBolillas = list()
    PrintCartones(listaCartones)    
    while True:
        opcion = input("Desea sacar una bolilla o terminar el juego(x)?")
        if opcion == 'x':
            break
        PrintCartones(listaCartones)
        listaBolillas = SacarBolilla(listaBolillas)
        print(f"Bolilla {listaBolillas[-1]}")
        listaBolillas.sort()
        print(f"Lista de bolillas {listaBolillas}")
        ganador = Ganador(listaBolillas, listaCartones)
        if ganador == 0:
            print("Aún no hay ganadores")
            continue
        print(f"Ganador del bingo jugador {ganador}")
        break
    print("Gracias por jugar al bingo")

if __name__ == "__main__":
    BingoStart()


