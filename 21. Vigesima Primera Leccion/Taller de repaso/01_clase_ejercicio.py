"""
    Construir un programa que declare una clase tipo ANIMAL y que instancie un objeto llamado PERRO.
"""

# Se crea la clase
class Animal:
    def __init__(self, nombre, edad, raza, color, peso, tamano):
        # Asignar todos los parámetros a atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza
        self.__color = color
        self.__peso = peso
        self.__tamano = tamano
        
        # Construir la cadena de información usando los atributos de la instancia
        self.nombre_animal = f'\nNombre: {self.__nombre}\nEdad: {self.__edad}\nRaza: {self.__raza}\nColor: {self.__color}\nPeso: {self.__peso}\nTamano: {self.__tamano}\n'
        
    def get_nombre(self):
        return self.__nombre
    
    def ladrir(self):
        return f'{self.__nombre} esta ladrando a lo wey.\n'
    
    def hambre(self):
        return f'{self.__nombre} tiene mucha hambre el dia de hoy.\n'
    

# Instanciar la variable a la clase y asignar sus atributos
perro = Animal('Firulais', 5, 'Labrador', 'Marron', '20 kg', 'Grande')

# Imprimir los resultados llamando a los metodos
print(perro.nombre_animal)
print(perro.get_nombre())
print(perro.ladrir())
print(perro.hambre())