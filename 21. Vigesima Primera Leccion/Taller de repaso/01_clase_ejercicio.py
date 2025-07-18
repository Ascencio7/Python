"""
    Construir un programa que declare una clase tipo ANIMAL y que instancie un objeto llamado PERRO.
"""

# Se crea la clase
class Animal:
    def __init__(self, nombre, edad, raza, color, peso, tamano):
        self.nombre_animal = f'\nNombre: {nombre}\nEdad: {edad}\nRaza: {raza}\nColor: {color}\nPeso: {peso}\nTamano: {tamano}\n'
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def ladrir(self):
        return f'{self.__nombre} esta ladrando a lo wey.\n'
    
    def hambre(self):
        return f'{self.__nombre} tiene mucha hambre el dia de hoy.\n'
    

perro = Animal('Firulais', 5, 'Labrador', 'Marron', '20 kg', 'Grande')

print(perro.nombre_animal)
print(perro.get_nombre())
print(perro.ladrir())
print(perro.hambre())