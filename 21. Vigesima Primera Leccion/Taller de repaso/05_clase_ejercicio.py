"""
    Construir un programa que declare una clase ARBOL y que instancie un objeto llamado CEDRO.
"""

class Arbol:
    def __init__(self, nombre, altura, tipo, color, edad):
        # Asignar todos los parámetros a atributos privados
        self.__nombre = nombre
        self.__altura = altura
        self.__tipo = tipo
        self.__color = color
        self.__edad = edad
        
        # Construir la cadena de información usando los atributos de la instancia
        self.info = f'\nNombre: {self.__nombre}\nAltura: {self.__altura} metros\nTipo: {self.__tipo}\nColor: {self.__color}\nEdad: {self.__edad} anos\n'
        
    def get_nombre(self):
        return self.__nombre + '\n'
    
    def crecer(self):
        return f'El arbol de cedro ha crecido mucho.\n'
    
    def cortar(self):
        return f'El arbol de cedro ha sido cortado por completo :( \n'


# Instanciar la variable a la clase y asignar sus atributos
cedro = Arbol('Cedro', 15, 'Conifera', 'Cafe oscuro', 2)

# Imprimir los resultados llamando a los metodos
print(cedro.info)
print(cedro.get_nombre())
print(cedro.crecer())
print(cedro.cortar())