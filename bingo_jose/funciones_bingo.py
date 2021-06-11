import random

def nueva_bolilla():
    seguir = True
    bolillas_jugadas = list()
    while seguir:
        bolilla = int(random.random() * 100)
        if bolilla in bolillas_jugadas:
            continue
        else:
            bolillas_jugadas.insert(0, bolilla)
        print(f"\nSalió la bolilla número: {bolilla}, bolillas ya jugadas: {bolillas_jugadas}")
        op = input("Pulse Enter para obtener la próxima bolilla, 'x' para salir:")
        if op == 'x':
            seguir = False