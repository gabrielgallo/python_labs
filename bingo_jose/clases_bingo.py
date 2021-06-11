import random

class InteraccionUsuario:
    def __init__(self,lineas):
        self.lineas = lineas

    def imprime_lineas(lineas):
        for n in lineas:
            print(n)

    def imprime_listas(lineas):
        print(lineas)

    def ingresar_numero(lineas):
        seguir = True
        while seguir:
            entrada = input(lineas[0])
            if entrada in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                break
            else:
                print(lineas[1])
        return entrada



class GeneradorCartones:
    def __init__(self,cart_num):
        self.cart_num = cart_num

    def genera_carton(cart_num):
        list_carton = list()
        while len(list_carton) < cart_num:
            j = int(random.random() * 100)
            if j not in list_carton:
                list_carton.insert(-1, j)
        return list_carton

