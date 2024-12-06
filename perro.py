class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return f"{self.nombre} dice ¡guau!"


# Crear una instancia de la clase Perro
mi_perro = Perro("Rex", 5)
print(mi_perro.ladrar())
