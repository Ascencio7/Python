"""
    Construir un programa que declare una clase COMIDA y que instancie un objeto llamado ARROZCONPOLLO.
"""

class Comida:
    def __init__(self, nombre, tipo, precio, cantidad):
        # Asignar todos los parámetros a atributos privados
        self.__nombre = nombre
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__precio = precio
        
        self.__total = self.__precio * self.__cantidad
        
        # Construir la cadena de información usando los atributos de la instancia
        self.info = f'\nNombre: {self.__nombre}\nTipo: {self.__tipo}\nPrecio: ${self.__precio}\nTotal: ${self.__total}\n'
        
    def get_nombre(self):
        return self.__nombre
    
    def comer(self):
        return f'{self.__nombre} es muy buena comida.\n'


# Instanciar la variable a la clase y asignar sus atributos
arroz_pollo = Comida('Arroz con pollo', 'En Salsa', 3.25)

# Imprimir los resultados llamando a los metodos
print(arroz_pollo.info)
print(arroz_pollo.get_nombre())
print(arroz_pollo.comer())