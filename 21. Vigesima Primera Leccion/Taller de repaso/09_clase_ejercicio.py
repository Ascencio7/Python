"""
    Construir un programa que declare una clase SERVICIO y que instancie un objeto llamado ENERGIA.
"""

class Servicio:
    def __init__(self, servicio, proveedor, costo, duracion):
        # Asignar todos los parámetros a atributos privados
        self.__servicio = servicio
        self.__proveedor = proveedor
        self.__costo = costo
        self.__duracion = duracion
        
        # Calcular el total dentro del método
        self.__total = self.__duracion * self.__costo

        # Construir la cadena de información usando los atributos de la instancia
        self.info = (f'\nServicio: {self.__servicio}\n'
                     f'Proveedor: {self.__proveedor}\n'
                     f'Costo: ${self.__costo}\n'
                     f'Duracion: {self.__duracion} meses\n'
                     f'Total: ${self.__total}')
        
    
    def get_servicio(self):
        return f'Servicio de {self.__servicio} por el proveedor {self.__proveedor}\n'
    
    def activar(self):
        return f'El servicio de {self.__servicio} ha sido activado.\n'
    
    def cancelar(self):
        return f'El servicio de {self.__servicio} ha sido cancelado.\n'
    
    def pagar_servicio(self):
        return f'El servicio de {self.__servicio} ha sido pagado.\n'
    
    def servicio_mora(self):
        return f'El servicio de {self.__servicio} tiene un cargo por mora de pago.\n'
    
    def servicio_renovado(self):
        return f'El servicio de {self.__servicio} ha sido renovado nuevamente.\n'


# Instanciar la variable a la clase y asignar sus atributos
energia = Servicio('Luz', 'Energia S.A. de C.V.', 28.33, 12)

# Imprimir los resultados llamando a los metodos
print(energia.info)
print(energia.get_servicio())
print(energia.activar())
print(energia.pagar_servicio())
print(energia.servicio_mora())
print(energia.cancelar())
print(energia.servicio_renovado())