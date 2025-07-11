# Clases: Se definen con el PascalCase, mayuscula la primer letra

# definir la clase
class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

# el self DEBE IR SI O SI
class Person:
    def __init__(self, nombre, apellido, alias = 'Sin alias'):
        # self.nombre = nombre
        # self.apellido = apellido
        # self.edad = edad
        # self.estatura = estatura
        
        # Esta es otra forma de hacerlo: Propiedad Almacenada
        # evita acceder a todos los campos, en vez, solo accede a uno solo que puede representar esos campos ocultos
        self.full_name = f'\n{nombre} {apellido} ({alias})' # Propiedad publica
        self.__name = nombre # Propiedad privada
        
    def get_nombre(self):
        return self.__name
        
    
    def caminar(self):
        print(f'{self.full_name} esta caminando')
        
        
        
        
        
# se pasan los valores
mi_resultado = Person('Vladimir', 'Ascencio')

# se imprime la clase accediento a la unica propiedad accesible de la clase
print(mi_resultado.full_name)

mi_resultado.caminar()

mi_otra_persona = Person('Ruth', 'Vaquerano', 'Manita :3')
print(mi_otra_persona.full_name)
mi_otra_persona.caminar()


mi_otra_persona.full_name = 'Allison Servano (La Chelita de ojos no claros)'
print(mi_otra_persona.full_name)