"""
    Construir un programa que declare una clase DISPOSITIVO y que instancie un objeto llamado PORTATIL.
"""

class Dispositivo:
    def __init__(self, marca, modelo, procesador, ram, almacenamiento):
        # Asignar todos los parámetros a atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__procesador = procesador
        self.__ram = ram
        self.__almacenamiento = almacenamiento
        
        # Construir la cadena de información usando los atributos de la instancia
        self.info = f'\nMarca: {self.__marca}\nModelo: {self.__modelo}\nProcesador: {self.__procesador}\nRAM: {self.__ram} GB\nAlmacenamiento: {self.__almacenamiento} GB\n'
        
    def get_dispositivo(self):
        return f'{self.__marca} {self.__modelo}\n'
    
    def encender(self):
        return f'El dispositivo {self.__marca} {self.__modelo} se ha encendido.\n'
    
    def apagar(self):
        return f'El dispositivo {self.__marca} {self.__modelo} se ha apagado.\n'


# Instanciar la variable a la clase y asignar sus atributos
portatil = Dispositivo('Dell', 'XPS 13', 'Intel Core i7', 16, 512)

# Imprimir los resultados llamando a los metodos
print(portatil.info)
print(portatil.get_dispositivo())
print(portatil.encender())
print(portatil.apagar())