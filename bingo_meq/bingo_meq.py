import random

def _generar_cartones_(cant_jug,cant_num):
    #genero_numeros_para_generar_cartones
    numeros = []
    for x in range(100):
        numeros.append(x)
    for c in range(cant_jug): #cartones o líneas
        print(f"\nCarton: {c+1}")
        print(random.sample(numeros,cant_num))

def _sacar_nros_():
    bolillero = []
    for x in range(100):
        bolillero.append(x)
    seguir = True
    while seguir:
        saca_bolilla = bolillero.pop(random.randint(0,len(bolillero)))
        print(f"\nSalió el nro: {saca_bolilla}")
        op =input("Enter para próximo nro, 'x' para salir:")
        seguir = False if 'x' == op else True

def bingo_start():
    print('BINGO VERSION 1.0')
    cant_jug=input('Ingrese cantidad de jugdores: ')
    cant_num = input('Ingrese cantidad de numeros por cartón: ')
    _generar_cartones_(int(cant_jug),int(cant_num))
    _sacar_nros_()

if __name__ == "__main__":
    bingo_start()
