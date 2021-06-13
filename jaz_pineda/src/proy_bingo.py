import random #genera nùmeros aleatoriamente


def armar_carton(numeros):
# numeros random para armar carton 
# sample(sec, num). Esta función devuelve num elementos aleatorios de la secuencia sec.
# acción de repartir num cartas a un jugador.
    n_arma_cart1= random.sample(numeros, 20)
    
    
    celda= {'valor', 'numero', 'estado'} #creo dicc
    carton = []


    for i in range(0, len(n_arma_cart1), 5): #  i = 0, 5
        columna=[]
        for num in n_arma_cart1[0 + i: 5 + i]: # 1 n_arma_cart1[0:5] 2 n_arma_cart1[5,10] 
            columna.append({'valor': num, 'formato':f"{num:02}",'estado':False })
        carton.append(columna)
    return carton

def imprimir(carton):
    fieldnames = ['B', 'I', 'N', 'G', 'O']
    for n in fieldnames:
        print(n,  end='\t')
    print()
    for columna in carton:
        for celda in columna:
            print(celda['formato'], end='\t' )
        print() #tiene salto de linea

def main():
    print("Bienvenido al juego Multi Bingo ")
    #numeros q salen en la bolilla
    numeros=[]
    for i in range(1, 100):
        numeros.append(i)

    carton1 = armar_carton(numeros)
    carton2 = armar_carton(numeros)
    imprimir(carton1)
    print()
    # imprimir(carton2)
    


if __name__ == "__main__":
    main()
   
