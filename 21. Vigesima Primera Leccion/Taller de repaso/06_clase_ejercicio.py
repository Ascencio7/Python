"""
    Construir un programa que declare una clase LIBRO y que instancie un objeto llamado NOVELA.
"""

class Libro:
    # Asignar todos los parámetros a atributos privados
    def __init__(self, titulo, autor, genero, paginas, fecha):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__paginas = paginas
        self.__fecha = fecha
        
        # Construir la cadena de información usando los atributos de la instancia
        self.info = f'\nTitulo: {self.__titulo}\nAutor: {self.__autor}\nGenero: {self.__genero}\nPaginas: {self.__paginas}\nFecha de publicacion: {self.__fecha}\n'

    def get_libro(self):
        return self.__titulo + '\n'
    
    def leer(self):
        return f'Leyendo el libro {self.__titulo} de {self.__autor}.\n'

  
# Instanciar la variable a la clase y asignar sus atributos
novela = Libro('IT', 'Stephen King', 'Terror', 1500, '1986')

# Imprimir los resultados llamando a los metodos
print(novela.info)
print(novela.get_libro())
print(novela.leer())