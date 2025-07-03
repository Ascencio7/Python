"""
    Crear un programa que:
    Cree una tupla con 5 números ingresados por el usuario.
    Imprima la tupla completa.
    Imprima el primer y último elemento de la tupla.
    Imprima la suma de todos los elementos.
"""

list_numeros = [] # se define una lista para agregar los elementos

# se itera en 5 numeros segun el enunciado
for i in range(5):
    numero = int(input(f'\nIngresa el numero [{i+1}/5]: '))
    list_numeros.append(numero) # se agrega el numero ingresado a la lista
    
tupla_numeros = tuple(list_numeros) # se pasa la lista a una tupla inmutable luego de ingresar los datos


# Solo con fines de orden, se pasa la tupla ordenada con 'sorted' pero en si no se puede ordenar la tupla como tal
tupla_ordenada = sorted(tupla_numeros)


# Se imprimen los resultados

# Mostrar la tupla
print('\n\t\t======== DATOS FINALES ========')
print(f'\nTupla ingresada: {tupla_numeros}')

# Mostrar la tupla 'ordenada'
print(f'Tupla ordenada como lista: {tupla_ordenada}')

# Mostrar el primer elemento de la tupla
print('\nEl primer y ultimo elemento de la tupla ingresada:')
print(f'\nPrimer elemento: {tupla_numeros[0]}')
print(f'Ultimo elemento: {tupla_numeros[-1]}')

# La suma de todos los elementos de la tupla
print('\nSuma de los elementos de la tupla:')
print(f'\nTotal suma de la tupla ingresada: {sum(tupla_numeros)}')

print('\nFin del programa...\n')