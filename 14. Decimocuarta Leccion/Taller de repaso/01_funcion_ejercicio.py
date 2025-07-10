"""
    Construir una funcion que reciba su nombre como parametro y que lo muestre 5 veces en 
    pantalla.
"""

# 1. Se define la funcion
def mostrar_nombre(nombre):
    for _ in range(5):
        print(nombre)        

nombre = input('\nIngrese su nombre: ')

mostrar_nombre(nombre)