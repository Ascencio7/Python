"""
    Construir un programa que declare una clase EMPAQUE y que instancie un objeto llamado CAJA.
"""

class Empaque:
    def __init__(self, tipo, peso, volumen, contenido):
        # Asignar todos los parámetros a atributos privados
        self.__tipo = tipo
        self.__peso = peso
        self.__volumen = volumen
        self.__contenido = contenido
        
        # Construir la cadena de información usando los atributos de la instancia
        self.info = f'\nTipo: {self.__tipo}\nPeso: {self.__peso}\nVolumen: {self.__volumen}\nContenido: {self.__contenido}\n'
        
    def get_empaque(self):
        return self.__tipo + '\n'

# Instanciar la variable a la clase y asignar sus atributos
caja = Empaque('Tecnologia', 15.25,150,'Computadora MacOS Pro')

# Imprimir los resultados llamando a los metodos
print(caja.info)
print(caja.get_empaque())