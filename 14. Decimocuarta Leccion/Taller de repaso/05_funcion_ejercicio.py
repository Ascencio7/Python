"""
    Construir una funcion que reciba una lista de cadenas y retorne la suma de la cantidad
    de las letras de cada cadena.    
"""

# Crear la funcion
def lista_cadena(list_cadenas):
    # Se retorna la suma de cada cadena y se itera por cada una de ellas
    return sum(len(cadena) for cadena in list_cadenas)

# Se crea una lista
lista = list()

# Se inicializa la lista con las cadenas
lista = ['Vladimir', 'Ascencio', 'Rodriguez', 'Alondra', 'Pablo']

# Se llama a la funcion en la impresion y se pasa la lista
print(lista_cadena(lista))