# Ingresar los datos del empleado usando la estructura de un diccionario

# definir el diccionario con las claves que se van a manejar
registros = {
    'DUI': [],
    'Nombres': [],
    'Salario': [],
    'Puesto': []
}

# comprobar si es un diccionario
print(type(registros))


# Se define la cantidad de los registros como numero entero
cant = int(input("\nIngresa la cantidad de registros a ingresar: "))


# Se llena mediante un bucle for
for i in range(cant):
    print(f'\nEmpleado N°{i+1}:\n')
    dui = input('\nNumero de DUI: ') # Se crean variables para guardar los datos ingresados
    nombres = input('Nombre completo: ')
    salario = float(input('Salario: $'))
    puesto = input('Puesto laboral: ')
    
    # Se ingresan las variables al diccionario
    registros['DUI'].append(dui) # Se usa la funcion 'append' para agregar el valor guardado en la variable
    registros['Nombres'].append(nombres)
    registros['Salario'].append(salario)
    registros['Puesto'].append(puesto)
    

# Se imprimen los resultados con un bucle for
for x in range(cant):
    print(f'\n\t\tDatos del Empleado N°{x+1}\n')
    print(f'DUI: {registros["DUI"] [x]}')
    print(f'Nombre: {registros["Nombres"][x]}')
    print(f'Salario: ${registros["Salario"][x]}')
    print(f'Puesto: {registros["Puesto"][x]}')
    
print('\nFin del programa...')

"""
    Para llenar un diccionario se necesita:
    
        1. Definir las claves del diccionario y el valor vacio '[]'.
        2. Crear variables para guardar los datos.
        3. Agregar las variables con los datos ingresados al diccionario segun la clave que corresponda.
"""