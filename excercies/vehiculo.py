class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True

    def arrancar(self):
        self.arrancado = True
        self.parado = False

    def parar(self):
        self.parado = True
        self.arrancado = False

    def resumen(self):
        print(
            "Marca:",
            self.marca,
            "\n",
            "Modelo:",
            self.modelo,
            "\n",
            "Color:",
            self.color,
            "\n",
            "Está arrancado:",
            self.arrancado,
            "\n",
            "Está parado:",
            self.parado,
        )


miCoche = Vehiculo("Renault", "Megane")

miCoche.arrancar()

miCoche.resumen()

"""
class Moto(Vehiculo): 
    pass 
 
miMoto = Moto("Kawasaki", "Ninja") 
 
miMoto.resumen() 
"""


class Moto(Vehiculo):
    is_carenado = False

    # Método propio de la clase Moto, no heredado del padre.
    def poner_carenado(self):
        self.is_carenado = True

    # La clase Moto sobrescribe el método resumen() heredado del padre
    def resumen(self):
        print(
            "El modelo es una moto",
            "\n",
            "Marca:",
            self.marca,
            "\n",
            "Modelo:",
            self.modelo,
            "\n",
            "Color:",
            self.color,
            "\n",
            "Está arrancado:",
            self.arrancado,
            "\n",
            "Está parado:",
            self.parado,
            "\n",
            "Tiene carenado:",
            self.is_carenado,
        )


miMoto = Moto("Kawasaki", "Ninja")
miMoto.resumen()


class kwad(Moto):
    pass


miKwad = kwad("Linhai", "LH 500")
miKwad.resumen()


class V_electricos(Vehiculo):

    def cilindrada(self):
        self.cilindrada = 3000

    def estado(self):
        print("Marca", self.marca, "Modelo", self.modelo, "Cilindrada", self.cilindrada)


class B_electrica(Vehiculo, V_electricos):
    pass
