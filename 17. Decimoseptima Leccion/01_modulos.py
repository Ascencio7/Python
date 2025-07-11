# Modulos

# Es como una libreria
# modulo fuera del sistema
from module import sumar, imprimir_nombre_por_defecto

print('La suma es:\n')
sumar(10,50, 100)

imprimir_nombre_por_defecto('Vladimir', 'Ascencio', 'VladiDev')
imprimir_nombre_por_defecto('Vladimir', 'Ascencio')


# Modulos dentro del sistema
# import math

# print(math.pi)
# print(math.log(10))
# print(math.sqrt(25))
# print(math.sqrt(781))
# print(math.pow(80,2))

from math import pi as pi_valor # como un alias

print(pi_valor)