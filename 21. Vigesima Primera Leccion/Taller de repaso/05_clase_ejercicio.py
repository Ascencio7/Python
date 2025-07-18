"""
    Construir un programa que declare una clase ARBOL y que instancie un objeto llamado CEDRO.
"""

class Arbol:
    def __init__(self, nombre, altura, tipo, color, edad):
        self.info = f'\nNombre: {nombre}\nAltura: {altura} metros\nTipo: {tipo}\nColor: {color}\nEdad: {edad} anos\n'
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre + '\n'
    
    def crecer(self):
        return f'El arbol de cedro ha crecido mucho.\n'
    
    def cortar(self):
        return f'El arbol de cedro ha sido cortado por completo :( \n'
    
cedro = Arbol('Cedro', 15, 'Conifera', 'Cafe oscuro', 2)

print(cedro.info)
print(cedro.get_nombre())
print(cedro.crecer())
print(cedro.cortar())