class Book:
    """
    Clase para trabajar con libros
    """

    def __init__(self, title, author="", electronic=False):
        self.title = title
        self.author = author
        self.is_electronic = electronic

    def __del__(self):
        print("Acabas de llamar al método destructor. El objeto acaba de ser eliminado")


book = Book("El Señor de los Anillos")
book.title

del book
