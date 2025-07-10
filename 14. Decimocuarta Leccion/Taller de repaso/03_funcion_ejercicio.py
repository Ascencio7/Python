"""
    Construir un programa que reciba (como parametro) una lista de datos numericos y retorne la suma 
    de dichos datos.
"""

def lista_numeros(lista_datos):
    return sum(lista_datos)

lista = [12, 65, 100]

resultado = lista_numeros(lista)
print(resultado)