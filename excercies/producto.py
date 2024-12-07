class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion, productor, distribuidor):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor

    def descr(self):
        print(
            "REFERENCIA:",
            self.referencia,
            "\n",
            "NOMBRE:",
            self.nombre,
            "\n",
            "PVP:",
            self.pvp,
            "\n",
            "DESCRIPCIÓN:",
            self.descripcion,
            "\n",
            "PRODUCTOR:",
            self.productor,
            "\n",
            "DISTRIBUIDOR:",
            self.distribuidor,
            "\n",
        )


producto = Producto(
    2035, "Botella de Aceite de Oliva", 5, "250 ML", "La Aceitera", "Distribuiciones SA"
)
producto.descr()


def rebajar_producto(producto, rebaja):
    producto.pvp = producto.pvp - (producto.pvp / 100 * rebaja)
    return producto.pvp


productoReba = Producto(
    2035,
    "Botella de Aceite de Oliva",
    rebajar_producto(producto, 10),
    "250 ML",
    "La Aceitera",
    "Distribuiciones SA",
)
productoReba.descr()
