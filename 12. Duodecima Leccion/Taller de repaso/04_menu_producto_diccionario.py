"""
    Programa con diccionarios para registrar productos:
    - Registrar producto (nombre, precio, cantidad a llevar).
    - Mostrar todos los productos con su total (precio * cantidad).
    - Salir del programa.
"""


# Declarar el diccionario de los productos
productos = {
    'Nombre': [],
    'Precio': [],
    'Cantidad': [],
    'Total': [] # total = precio * cantidad
}


# Una variable para guardar la opcion del menu por el usuario
opcion = 0

# Usar un bucle while para mostrar el menu con las opciones
while True:
    print('\n\t\t======= Menu del Diccionario =======\n')
    print('1. Registrar productos.')
    print('2. Mostrar todos los productos ingresados.')
    print('3. Eliminar un producto por su indice.')
    print('4. Mostrar un producto por su indice.')
    print('5. Salir del programa.')
    
    # Se pide la opcion del usuario segun el menu anterior
    try:
        opcion = int(input('\nIngresa la opcion deseada: '))
    except ValueError:
        print('\nDebes ingresar un numero valido.\n')
        continue
    
    # Validaciones
    
    # Se verifica si la opcion es 1 que es la de agregar clientes
    if opcion == 1:
        print('\n\t\t======= AGREGAR PRODUCTOS =======\n')
        
        # Solicitar la cantidad de productos a ingresar
        try:
            cant_productos = int(input('\nIngresa la cantidad de productos a ingresar: '))
        except ValueError: # Si ingresa un numero invalido se muestra el siguiente mensaje
            print('\nDebes ingresar un numero valido.\n')
            continue # Retorna al menu
                
                
        # Se itera segun la cantidad de clientes a ingresar
        for i in range(cant_productos):
            print(f'\nProducto N°{i+1}:\n')
            nombre_producto = input('Nombre del producto: ') # Se crean variables para guardar los datos
            
            # Validar que el precio sea positivo con un bucle while
            while True:
                try: # Se hace un manejo de errores por si el precio es negativo o un dato incorrecto
                    precio_producto = float(input('Precio del producto: $'))
                    
                    # Si el producto es menor a 0, osea un numero negativo se muestra el siguiente mensaje
                    if precio_producto <= 0:
                        print('\nEl precio debe ser positivo. Intentalo de nuevo.')
                    else: 
                        break
                except ValueError:
                    print('\nIngresa un numero valido para el precio.\n')
            
            # Validar que el precio sea positivo (lo mismo que el anterior bucle)
            while True:
                try:
                    cantidad_producto = int(input('Cantidad del producto a llevar: '))
                    
                    if cantidad_producto <= 0:
                        print('\nEl precio debe ser positivo. Intentalo de nuevo.')
                    else:
                        break
                except ValueError:
                    print('\nIngresa un numero valido para la cantidad.\n')
            
            # Se calcula el total de producto por multiplicar el precio por la cantidad, y se redondea a 2 decimales
            total_producto = round(cantidad_producto * precio_producto,2)
            
            # Agregar al diccionario los datos
            productos['Nombre'].append(nombre_producto)
            productos['Precio'].append(precio_producto)
            productos['Cantidad'].append(cantidad_producto)
            productos['Total'].append(total_producto)
                
            # Un mensaje de exito
            print('\nProducto ingresado correctamente.\n')
            continue # Y se retorna al menu
           
            
    # Se verifica que la opcion sea 2 que es para mostrar los productos
    elif opcion == 2:
        print('\n\t\t======= MOSTRAR PRODUCTOS =======\n')
        
        # Verifica si hay productos registrados con 'len'
        if len(productos['Nombre']) == 0: # Si no hay entonces se muestra el siguiente mensaje
            print('\nNo hay productos para mostrar.\n') 
            continue # Retorna al menu principal
        
        # Si hay productos recorre y muestra los datos
        for i in range(len(productos['Nombre'])):
            print(f'\n\t\tDatos del Producto N°{i+1}')
            print(f'Nombre: {productos["Nombre"][i]}')
            print(f'Precio: {productos["Precio"][i]:.2f}')
            print(f'Cantidad: {productos["Cantidad"][i]}')
            print(f'Total: ${productos["Total"][i]:.2f}\n')
        continue # Y vuelve al menu principal
    
    
    # Se verifica que la opcion sea 3 que es para eliminar un producto por su indice
    elif opcion == 3:
        print('\n======= ELIMINAR PRODUCTOS POR ÍNDICE =======\n')
        print('=== Los índices inician desde 0 ===\n')

        # Verificar si hay productos para eliminar
        if len(productos['Nombre']) == 0: # Si no hay muestra el siguiente mensaje
            print('\nNo hay productos para eliminar.')
            continue # Retorna al menu

        # Mostrar el listado de productos con índice
        for i in range(len(productos['Nombre'])):
            print(f"{i}: {productos['Nombre'][i]}, ${productos['Precio'][i]:.2f}, "
                f"{productos['Cantidad'][i]} unidades, Total: ${productos['Total'][i]:.2f}")

        try:
            # Solicitar el índice a eliminar
            indice = int(input('\nIngrese el índice del producto a eliminar: '))

            # Validar rango del índice
            if 0 <= indice < len(productos['Nombre']):
                eliminado = productos['Nombre'][indice]

                # Eliminar de todas las listas en el diccionario
                productos['Nombre'].pop(indice)
                productos['Precio'].pop(indice)
                productos['Cantidad'].pop(indice)
                productos['Total'].pop(indice)

                # Un mensaje de exito
                print(f'\nProducto "{eliminado}" eliminado correctamente.')
            else:
                print('\nÍndice inválido.') # Si ingreso un indice correcto se le muestra el mensaje siguiente
        except ValueError: 
            print('\nPor favor ingrese un número válido.') # Si ingreso un dato incorrecto se muestra el siguiente mensaje


    # Se verifica que la opcion sea 4 que es para mostrar un producto segun su indice
    elif opcion == 4:
        print('\n\t\t======= MOSTRAR PRODUCTOS POR INDICE =======\n')
        print('=== Los indices inician desde 0 ===\n')
        
        # Verifica si hay productos para eliminar
        if len(productos['Nombre']) == 0:
            print('\nNo hay productos para mostrar.\n')
            continue # Retorna al menu principal
        
        # Muestra el listado de los productos con su indice
        for i in range(len(productos['Nombre'])):
            print(f'{i}: {productos["Nombre"][i]}, {productos["Precio"][i]}, {productos["Cantidad"][i]}, {productos["Total"][i]}\n')
        
        try:
            
            # Se solicita el indice del producto a mostrar
            index_product = int(input('\nIngresa el indice del producto a mostrar: '))
            
            # Verifica que el indice este dentro del rango del diccionario
            if 0 <= index_product < len(productos['Nombre']):
                
                # Si es asi va mostrando los datos del cliente
                print('\nDatos del producto:\n')
                print(f'Producto: {productos["Nombre"][index_product]}')
                print(f'Precio: ${productos["Precio"][index_product]:.2f}')
                print(f'Cantidad: {productos["Cantidad"][index_product]}')
                print(f'Total: ${productos["Total"][index_product]:.2f}')
                
            else:
                print('\nIndice invalido.\n') # Si el indice no existe en el diccionario muestra el mensaje
        except ValueError:
            print('\nIngrese un numero valido. Intentelo de nuevo.\n') # Si el usuario ingresa un dato invalido muestra el siguiente mensaje
        continue # Retorna al menu
    
    # Se verifica que sea la opcion 5 que es para finalizar el programa.
    elif opcion == 5:
        print('\nFin del programa...\n')
        break # Sale del bucle infinito del while y cierra el programa.
    
    # Si la opcion ingresada no es del rango valido se muestra el siguiente mensaje.
    else:
        print('\nOpcion invalida. Ingrese la opcion 1 a 5 del menu. Intentalo de nuevo.\n')
        continue # Y lo retorna al menu principal de nuevo.