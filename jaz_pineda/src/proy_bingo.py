import random #genera nùmeros aleatoriamente
class carton:

    min= 1
    max= 15
    texto_b='BINGO'
    card={} #crea cartilla
    
    def __init__(self):
        for letra in self.texto_b:
            self.card[letra] = random.sample(range(self.min, self.max), 5)#toma una muestra del rango
            self.min += 15
            self.max += 15
    
    def imprimir_card(self):
        for letra in self.card:
            print(letra, end='\t')
            for numero in self.card[letra]:
                print(numero, end='\t')
            print()
        print()

class bingo:  
    def __init__(self):
        self.carton = carton()
        self.numer_bolilla = random.sample(range(1,76), 75)

    def sacar_bolilla(self):
        numr_bolilla = self.numer_bolilla.pop()#sacar bolilla uno a uno
        for letra in self.carton.card:
            i = 0
            for numero in self.carton.card[letra]:
                if numero == numr_bolilla:
                    self.carton.card[letra][i]='X'
                i += 1
        return numr_bolilla
    
    #verifica carton si gana
    def check_carton(self):
        ganador= False
        if self.carton.card['B'][0] =='X' and self.carton.card['I'][1]=='X' and self.carton.card['N'][2]=='X' and self.carton.card['G'][3]=='X' and self.carton.card['O'][4]=='X':
            ganador= True
        elif self.carton.card['O'][0] =='X' and self.carton.card['G'][1]=='X' and self.carton.card['N'][2]=='X' and self.carton.card['I'][3]=='X' and self.carton.card['B'][4]=='X':
            ganador= True
        for letra in self.carton.card:
            if self.carton.card[letra].count('X') == len(self.carton.card[letra]):
                ganador=True
        return ganador

if __name__=='__main__':
    # carton = carton()
    # carton.imprimir_card()
    juego = bingo()
    juego.carton.imprimir_card()
    print("La bolilla es...", juego.sacar_bolilla())
    respuesta=''
    while respuesta != "Salir":
        juego.carton.imprimir_card()
        print("La bolilla es...", juego.sacar_bolilla())
        respuesta= input()


