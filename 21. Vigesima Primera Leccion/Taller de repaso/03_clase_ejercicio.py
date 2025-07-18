
"""
    Construir un programa que declare una clase VEHICULO y que instancie un objeto llamado CARRO.
"""

class Vehiculo:
    def __init__(self, marca, modelo, color, anio, capacidad):
        self.info = f'\nMarca: {marca}\nModelo: {modelo}\nColor: {color}\nAño: {anio}\nCapacidad: {capacidad} personas\n'
        self.__nombre = marca
               
    
    def get_nombre(self):
        return self.__nombre
    
    def conducir(self):
        return f'{self.__nombre} ha arrancado.\n'
    
carro = Vehiculo('Lamborghini', 'Huracan', 'Negro', 2024, 2)

print(carro.info)
print(carro.get_nombre())
print(carro.conducir())