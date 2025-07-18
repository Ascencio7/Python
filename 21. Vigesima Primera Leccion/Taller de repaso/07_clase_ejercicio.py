"""
    Construir un programa que declare una clase PELICULA y que instancie un objeto llamado MONSTERSINC.
"""

class Pelicula:
    def __init__(self, titulo, director, genero, duracion):
        # Asignar todos los parámetros a atributos privados
        self.__titulo = titulo
        self.__director = director
        self.__genero = genero
        self.__duracion = duracion
        
        # Construir la cadena de información usando los atributos de la instancia
        self.info = f'\nPelicula: {self.__titulo}\nDirector: {self.__director}\nGenero: {self.__genero}\nDuracion: {self.__duracion} minutos\n'        
        
    def get_pelicula(self):
        return self.__titulo + '\n'
    
    def reproducir(self):
        return f'Reproduciendo la pelicula {self.__titulo}.\n'


# Instanciar la variable a la clase y asignar sus atributos
monstersinc = Pelicula('Monsters Inc', 'Pete Docter', 'Animacion', 92)

# Imprimir los resultados llamando a los metodos
print(monstersinc.info)
print(monstersinc.get_pelicula())
print(monstersinc.reproducir())