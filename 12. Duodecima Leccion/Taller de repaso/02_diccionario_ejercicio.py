"""
    Crear un programa que:
        Cree un diccionario con nombre, edad y ciudad ingresados por el usuario.
        Imprima el diccionario completo.
        Imprima cada valor de forma separada usando las claves.
"""

# Se define el diccionario
cliente = {
    'Nombre': [],
    'Edad': [],
    'Ciudad': []
}

# definir la cantidad de datos a ingresar
cant_clientes = int(input('\nIngresa la cantidad de clientes a ingresar: '))

# iterar con un bucle for
for i in range(cant_clientes):
    print(f'\n\t\tCliente {i+1}\n')
    nombres = input('Nombre completo: ') # Se crean variables para guardar los datos
    edad = int(input('Edad: '))
    ciudad = input('Ciudad: ')
    
    # Agregar las variables al diccionario
    cliente['Nombre'].append(nombres)
    cliente['Edad'].append(edad)
    cliente['Ciudad'].append(ciudad)
    

# imprimir el diccionario completo
for x in range(cant_clientes):
    print(f'\n\t\tDatos del Cliente N°{x+1}')
    print(f'\nNombre: {cliente["Nombre"][x]}')
    print(f'Edad: {cliente["Edad"][x]}')
    print(f'Ciudad: {cliente["Ciudad"][x]}')
    
    
# Imprimir los datos de forma separada
print('\n\t\tDatos separados de los clientes')
print(f'\nNombre: {cliente["Nombre"]}')
print(f'Edad: {cliente["Edad"]}')
print(f'Ciudad: {cliente["Ciudad"]}')

print('\nFin del programa...\n')