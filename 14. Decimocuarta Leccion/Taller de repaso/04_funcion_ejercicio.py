"""
    Construir una funcion que reciba una lista de datos numericos y retorne el promedio de los datos.
"""

def lista_promedio(lista_datos):
    if not lista_datos:
        return 0
    return sum(lista_datos) / len(lista_datos)


lista = [12, 65, 100, 13, 67.3]

resultado = lista_promedio(lista)
resultado = round(resultado, 2)

print(resultado)