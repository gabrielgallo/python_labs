import random
import os
import msvcrt

class Bingo:
    _carton = []

    def __init__(self, cant):
        self._cant = int(cant)
        self._carton = list(random.sample(range(0, 100), int(cant)))

    def VerCarton(self):
        print(self._carton)

    def marcarNumero(self, numeroMarcar):
        if numeroMarcar in self._carton:
            self._carton[self._carton.index(numeroMarcar)] = "*"

    def IsBingo(self):
        aciertos = self._carton.count("*")
        if int(aciertos) == int(self._cant):
            return True

class Bombo:
    _CantBolas = 0
    _Bombo = []
    _nroSorteado = []

    def __init__(self, cant):
        self._CantBolas = int(cant)
        self._Bombo = [i for i in range(1, 100)]

    def getNumero(self):
        #devuelve un numero del bombo

        numeroPos = random.randint(0, len(self._Bombo) - 1)
        numero = self._Bombo[numeroPos]
        del self._Bombo[numeroPos]

        self._nroSorteado.append(numero)
        self._CantBolas = self._CantBolas -1
        return numero

    def getNroSorteado(self):

        return self._nroSorteado

    def getNumerosRestantes(self):
        return self._CantBolas

CantPlayers=0
while int(CantPlayers) == 0:
    CantPlayers = input("Ingrese la cantidad de Jugadores = ")


cantNrosCarton = input("ingrese la cantidad de nros por carton = ")

list_obj = []

for x in range(int(CantPlayers)):
    obj = Bingo(int(cantNrosCarton))
    list_obj.append(obj)

i = 1
for x in list_obj:
    print("Jugador " + i.__str__())
    print(x.VerCarton())
    i=i+1

sorteo = Bombo(100) #100 numeros 0..99
print("*********************Comienza Sorteo****************************")
print("Restan " + str(sorteo.getNumerosRestantes()) + " Bolas")
input("Presione una tecla para continuar o Ñ para salir")


while int(sorteo.getNumerosRestantes()) > 1:
    numero = sorteo.getNumero()
    print("Numeros sorteados " + str(sorteo.getNroSorteado()))
    print("Salio el: " + str(numero))
    print("Restan " + str(sorteo.getNumerosRestantes()) + " Bolas")
    #Recorro lista de objetos y elimino numero sorteado
    i=1
    for x in list_obj:
        x.marcarNumero(numero)
        print("Jugador " + str(i))
        print(x.VerCarton())
        if x.IsBingo():
            print("*******************************************************")
            print("**********GANADOR Jugador " + str(i) + "*****************************")
            print("*******************************************************")
            exit()
        i=i+1


    input("Presione una tecla para continuar o Ñ para salir")
    os.system('cls')
