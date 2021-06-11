#import generabolilla
import random
import os

def genbolilla(desde,hasta):
    existe = True
    if len(listabolillas) == 0:
        numero = random.randint(desde,hasta)
        listabolillas.append(numero)
        return numero
    else:
        while existe:
            numero = random.randint(desde, hasta)
            if numero not in listabolillas:
                listabolillas.append(numero)
                return numero

listabolillas = []
boldesde = 1
bolhasta = 10

dif = bolhasta - boldesde + 1
'''
x = 1
while x <= dif: #llamo a la funcion la cantidad máxima de
    bola = genbolilla(boldesde,bolhasta)
    #print(listabolillas)
    #print("Bolilla: ",x," Número: ",bola)
    print(bola)
    x = x + 1
'''
salir = False
x = 1
while salir == False:
    os.system("cls")
    print("Presione la tecla G para generar bolilla o la tecla X para salir")
    tecla = input("Tecla: ")
#    print("Tecla pres: ",tecla)
    if tecla == "g" or tecla == "G":
        bola = genbolilla(boldesde, bolhasta)
        print("Bolilla: ", x, " Número: ", bola," Historial: ",listabolillas)
    if (tecla == "X" or tecla == "x"):
        salir = True
    if x == dif:
        print("Ya sacó todas las bolillas")
        exit()
    x = x + 1