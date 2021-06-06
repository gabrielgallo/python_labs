import random


# Falta al desarrollo entre otros
# - Evitar nros repetidos al sacar el nro
# - Evitar nros repetidos al genrar carton
# - Se puede pedir nro de carton


def _generar_cartones_():
    for c in range(4): #cartones o líneas
        print(f"\nCarton: {c}")
        for n in range(5):
            print(int(random.random()*100), end=', ')

def _sacar_nros_():
    seguir = True
    while seguir:
        nro_sacado = int(random.random() * 100)
        print(f"\nSalió el nro: {nro_sacado}")
        op =input("Enter para próximo nro, 'x' para salir:")
        seguir = False if 'x' == op else True


def bingo_start():
    _generar_cartones_()
    _sacar_nros_()




if __name__ == "__main__":
    bingo_start()