"""
    Construir un programa que declare una clase VEHICULO y que instancia un objeto llamado AVION
"""

class Vehiculo:
    def __init__(self, marca, modelo, color, anio, capacidad):
        # Asignar todos los parámetros a atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__anio = anio
        self.__capacidad = capacidad
        
        # Construir la cadena de información usando los atributos de la instancia
        self.info = f'\nMarca: {self.__marca}\nModelo: {self.__modelo}\nColor: {self.__color}\nAño: {self.__anio}\nCapacidad: {self.__capacidad} personas\n'               
    
    def get_nombre(self):
        return self.__nombre
    
    def volar(self):
        return f'{self.__nombre} ha despegado con exito.\n'


# Instanciar la variable a la clase y asignar sus atributos
avion = Vehiculo('Boeing', '747', 'Blanco', 2022, 170)

# Imprimir los resultados llamando a los metodos
print(avion.info)
print(avion.get_nombre())
print(avion.volar())