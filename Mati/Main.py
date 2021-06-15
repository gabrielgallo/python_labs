from Mati.Carton import Carton
from Mati.Global import constantes

#Con listas

cartones = list()

for i in range(constantes.c_num_jugadores):
    cartones.append(Carton())
    cartones[i].generar_numeros()

for j in range(constantes.c_num_jugadores):
    print(cartones[j].obtener_numeros())
