"""
    Construir un programa que declare una clase COMIDA y que instancie un objeto llamado ARROZCONPOLLO.
"""

class Comida:
    def __init__(self, nombre, tipo, precio):
        self.info = f'\nNombre: {nombre}\nTipo: {tipo}\nPrecio: ${precio}\n'
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def comer(self):
        return f'{self.__nombre} es muy buena comida.\n'
    
arroz_pollo = Comida('Arroz con pollo', 'En Salsa', 3.25)

print(arroz_pollo.info)
print(arroz_pollo.get_nombre())
print(arroz_pollo.comer())