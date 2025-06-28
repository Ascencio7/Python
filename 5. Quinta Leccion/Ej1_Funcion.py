# 1. Construir una funcion que permita determinar si un valor escrito por el usuario, esta o no esta dentro de un conjunto de datos.

# declarar la funcion
def encontrar_dato(datos, dato_encontrar):
    if dato_encontrar in datos:
        print("\nEl dato se encuentra en la lista.")
    else:
        print("\nEl dato no se encuentra en la lista.")
        
# Declarar los datos
a = [1, 2, 3, 4, 5] # se almacena una lista de datos

b = int(input("\nDato a encontrar: ")) # se pide el dato al usuario

encontrar_dato(a, b) # se llama a la funcion
print("\nFin.")