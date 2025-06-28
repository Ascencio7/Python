""" 
    Se desea calcular el área de un círculo dado su radio.
"""

from math import pi # importar solo la libreria necesario de pi

# funcion para calcular el area del circulo
def calcular_radio(radio):
    area = pi * (radio ** 2) # formula del area del circulo
    return area # retorna el resultado

# se pide el dato
radio = float(input("\nIngresa el radio del circulo: "))

area = calcular_radio(radio) # se llama la funcion
area = round(area, 2) # se redondea el resultado

print(f"\nEl area del circulo con un radio de {radio} es {area} unidades cuadradas.") # se imprime el resultado
print("Fin del programa.")