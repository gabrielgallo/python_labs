
class Figura:
    name = None

    def __init__(self, name):
        self.name = name

    def description(self):
        return {"name": self.name}




class Poligono(Figura):
    lados = []

    def __init__(self,name, lados):
        self.lados = lados
        super().__init__(name)

    def description(self):
        return {"name": self.name, "lados": self.lados}

    def perimetro(self):
        return sum(self.lados)

class Cuadrado(Poligono):
    def __init__(self,name, lado):
        lados = [lado]*4
        super(Cuadrado, self).__init__(name, lados)


if __name__ == "__main__":
    #figura = Figura("Cuadrado 1")
    #figura = Poligono("Cuadrado 2",[ 2.3, 2.3, 2.3, 2.3])
    figura = Cuadrado("Cuadrado 3", 2.3)
    print(figura.description())
    print(f'Perímetro {figura.perimetro()}')

