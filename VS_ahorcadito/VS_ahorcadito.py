import os
from time import sleep

def inicializar():
    for i in palabra:
        letras[i] = "_"
    print(letras)


def my_function():
    os.system("cls")
    print("Bienvenido al juego Ahorcadito")
    print("La Cantidad de letras es " + str(len(palabra)))
    for i in palabra:
        print(letras.get(i), end=' ')
    print("", end='\n')
    print("Las letras igresadas son: " + str(listLetrasUsu))
    print("Cantidad de fallos " + str(fallos))


archivo = open("C:\python\conjunto_palabras.txt", "r")
palabra = archivo.readline()

listLetrasUsu = list()
letras = {}
fallos = 0
inicializar()
fallos = 0
my_function()
while fallos < 8:
    print('Ingrese letra:')
    x = input()
    if x in listLetrasUsu:
        print("Letra Ya ingresada previamente")
    else:
        listLetrasUsu.append(x)
        if x in letras:
            letras[x] = x
        else:
            print("Letra Inexistente")
            fallos += 1
    sleep(2)
    # crear funcion verificar fin del juego
    my_function()