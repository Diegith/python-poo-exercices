class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion, productor, distribuidor):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.desc


def rebajar_producto(producto, rebaja):
    producto.pvp = producto.pvp - (producto.pvp / 100 * rebaja)
