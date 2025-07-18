"""
    Construir un programa que declare una clase VEHICULO y que instancia un objeto llamado AVION
"""

class Vehiculo:
    def __init__(self, marca, modelo, color, anio, capacidad):
        self.info = f'\nMarca: {marca}\nModelo: {modelo}\nColor: {color}\nAño: {anio}\nCapacidad: {capacidad} personas\n'
        self.__nombre = marca
               
    
    def get_nombre(self):
        return self.__nombre
    
    def volar(self):
        return f'{self.__nombre} ha despegado con exito.\n'


avion = Vehiculo('Boeing', '747', 'Blanco', 2022, 170)

print(avion.info)
print(avion.get_nombre())
print(avion.volar())