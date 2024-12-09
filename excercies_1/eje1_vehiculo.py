class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ", Velocidad (km/hr): " + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", Tipo: " + self.tipo


# Creamos un objeto heredado de la clase vehiculo
vehiculo1 = Vehiculo("Rojo", 4)
print(vehiculo1)

# Creamos un objeto de la clase hija Coche
coche = Coche("Azul", 4, 120)
print(coche)

# Creamos un objeto de la clase hija bicicleta
bicicleta = Bicicleta("Blanca", 2, "Urbano")
print(bicicleta)
