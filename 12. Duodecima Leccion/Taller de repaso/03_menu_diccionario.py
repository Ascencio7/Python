"""
    Crear un programa con un menú interactivo que permita:
        Agregar clientes (nombre, edad, ciudad).
        Mostrar todos los clientes ingresados.
        Eliminar un cliente por su índice.
        Mostrar datos del cliente por su indice.
        Salir del programa.

    Con validaciones de datos:
        Edad debe ser un entero positivo.
        No permitir eliminar si no hay registros.
        Evitar errores si se ingresa un índice inválido.

"""

# Se declara el diccionario
clientes = {
    'Nombre': [],
    'Edad': [],
    'Ciudad': []
}

# Una variable para guardar la opcion del menu por el usuario
opcion = 0

# Usar un bucle while para mostrar el menu con las opciones
while True:
    print('\n\t\t======= Menu del Diccionario =======\n')
    print('1. Agregar clientes.')
    print('2. Mostrar todos los clientes ingresados.')
    print('3. Eliminar un cliente por su indice.')
    print('4. Mostrar un cliente por su indice.')
    print('5. Salir del programa.')
    
    # Se pide la opcion del usuario segun el menu anterior
    opcion = int(input('\nIngresa tu opcion deseada: '))
    
    # Validaciones
    
    # Se verifica si la opcion es 1 que es la de agregar clientes
    if opcion == 1:
        print('\n\t\t======= AGREGAR CLIENTES =======\n')
        
        # Se pide la cantidad de clientes a ingresar
        cant_clientes = int(input('Ingrese la cantidad de clientes a ingresar: '))
        
        # Se itera segun la cantidad de clientes a ingresar
        for i in range(cant_clientes):
            print(f'\n\t\tCliente{i+1}\n')
            nombre = input('Nombre: ') # Se crean variables para guardar los datos
            
            # Validar que la edad sea positiva
            while True: # Se usa un bucle while
                try: # Se intenta capturar un numero entero en la variable
                    edad = int(input("Edad: "))
                    
                    # Si la edad es menor a 0, osea un numero negativo se muestra el siguiente mensaje
                    if edad <= 0:
                        print("\nLa edad debe ser positiva. Intenta nuevamente.")
                    else:
                        break # Si la edad es un entero se rompe este bucle
                except ValueError: # Si el dato no es un numero valido se muestra el siguiente mensaje
                    print("\nIngresa un número válido para la edad.")            
            ciudad = input('Ciudad: ')
            
            # Asignar las variables al diccionario
            clientes['Nombre'].append(nombre)
            clientes['Edad'].append(edad)
            clientes['Ciudad'].append(ciudad)
        
        # Mensaje de exito
        print('\nCliente ingresado correctamente') 
        continue # Retorna al menu de nuevo
    
    # Se verifica que la opcion sea 2 que es para mostrar los clientes
    elif opcion == 2:
        print('\n\t\t======= MOSTRAR CLIENTES =======\n')
        
        # Verifica si hay clientes registrados con 'len'
        if len(clientes['Nombre']) == 0: # si no hay entonces se muestra el siguiente mensaje
            print('\nNo hay clientes para mostrar.') 
            continue # Retorna al menu principal
        
        # Si hay clientes recorre y muestra los datos
        for i in range(len(clientes['Nombre'])):
            print(f'\n\t\tDatos del Cliente N°{i+1}')
            print(f'Nombre: {clientes["Nombre"][i]}')
            print(f'Edad: {clientes["Edad"][i]}')
            print(f'Ciudad: {clientes["Ciudad"][i]}')
        continue # Y vuelve al menu principal

    # Se verifica que la opcion sea 3 la que es para eliminar a los clientes por indice
    elif opcion == 3:
        print('\n\t\t======= ELIMINAR CLIENTES POR INDICE =======\n')
        print('=== Los indices inician desde 0 ===\n')
        
        # Verifica si hay clientes para eliminar
        if len(clientes['Nombre']) == 0: # Si no hay muestra el siguiente mensaje
            print('\nNo hay clientes para eliminar.')
            continue # Retorna al menu principal
        
        try:
            # Muestra el listado de clientes con su indice
            for i in range(len(clientes['Nombre'])):
                print(f"{i}: {clientes['Nombre'][i]}, {clientes['Edad'][i]}, {clientes['Ciudad'][i]}")
            
            # Se solicita el indice del cliente que se desea eliminar
            indice_cliente = int(input('\nIngrese el indice del cliente a eliminar: '))
            
            # Verifica que el indice este dentro del rango del diccionario
            if 0 <= indice_cliente < len(clientes['Nombre']):
                # Si es asi, va eliminando los datos del cliente
                clientes['Nombre'].pop(indice_cliente)
                clientes['Edad'].pop(indice_cliente)
                clientes['Ciudad'].pop(indice_cliente)
                
                print('\nCliente eliminado correctamente.') # Un mensaje de exito
            
            else: 
                # Si el indice no existe en el diccionario muestra el siguiente mensaje
                print('\nÍndice inválido.')
        except ValueError:
            print('\nPor favor ingrese un número válido.') # Si el usuario ingresa un valor no numerico
        continue # Y retorna al menu principal
    
    # Verifica que sea la opcion 4 que es la de mostrar datos del cliente por indice
    elif opcion == 4:
        print('\n\t\t======= MOSTRAR CLIENTES POR INDICE =======\n')
        print('=== Los indices inician desde 0 ===\n')
        
        # Verifica si hay clientes para eliminar
        if len(clientes['Nombre']) == 0: # Si no hay muestra el siguiente mensaje
            print('\nNo hay clientes para mostrar.')
            continue # Retorna al menu principal
        
        try:
            # Muestra el listado de clientes con su indice
            for i in range(len(clientes['Nombre'])):
                print(f"{i}: {clientes['Nombre'][i]}, {clientes['Edad'][i]}, {clientes['Ciudad'][i]}")
            
            # Se solicita el indice del cliente que se desea eliminar
            indice_cliente = int(input('\nIngrese el indice del cliente a mostrar: '))
            
            # Verifica que el indice este dentro del rango del diccionario
            if 0 <= indice_cliente < len(clientes['Nombre']):
                # Si es asi, va mostrando los datos del cliente
                print('\nDatos del cliente:\n')
                print(f'Nombre: {clientes["Nombre"][indice_cliente]}')
                print(f'Edad: {clientes["Edad"][indice_cliente]}')
                print(f'Ciudad: {clientes["Ciudad"][indice_cliente]}')    
                # Hasta aqui llegaria lo de mostrar clientes por indice
                 
            else: 
                # Si el indice no existe en el diccionario muestra el siguiente mensaje
                print('\nÍndice inválido.')
        except ValueError:
            print('\nPor favor ingrese un número válido.') # Si el usuario ingresa un valor no numerico
        continue # Y retorna al menu principal
    
    # Verifica que la opcion sea 5 que es para finalizar el programa
    elif opcion == 5:
        print('\nFin del programa\n')
        break # Sale del bucle infinito del while y cierra el programa
    
    # Si la opcion ingresada no es del rango valido se muestra el siguiente mensaje
    else:
        print('\nOpcion invalida. Ingresas las opciones 1 a 5 del menu. Intentalo de nuevo.\n')
        continue # Y retorna al menu principal de nuevo.