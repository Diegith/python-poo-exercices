import random


class Poligono:
    def __init__(self, lados, color):
        self.color = color
        self.lados = lados
        self.base = 0
        self.altura = 0

    def show(self):
        return print("Color: ", self.color, "\n", "Lados: ", self.lados)


class Cuadrado(Poligono):
    def __init__(self, lado, color=None):
        Poligono.__init__(self, 4, color)
        self.lado = lado

    def show(self):
        super().show()
        print("Lado:", self.lado)


class Triangulo(Poligono):
    def __init__(self, color=None):
        Poligono.__init__(self, 3, color)
        self.base = random.randint(1, 10)
        self.altura = random.randint(1, 10)

    def show(self):
        super().show()
        print("Base: ", self.base)
        print("Altura: ", self.altura)


t1 = Triangulo("Blanco")
t2 = Triangulo("Azul")
c1 = Cuadrado(2, "verde")  # Declaramos un cuadrado

poligonos = t1, t2, c1
# Tupla con dos Trinagulos y un Cuadrado
for poligono in poligonos:
    poligono.show()
    print("")
