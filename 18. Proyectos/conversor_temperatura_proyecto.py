# ✅ Conversor de unidades (metros a pies, °C a °F, etc.)

# Iniciar la variable a usar en 0
opcion = 0

# Usar un bucle while que se repetira hasta ingresar la opcion 5
while True:
    # Mensaje de bienvenida
    print('\n========== BIENVENIDO AL CONVERSOR DE UNIDADES ==========\n')  
    print('1. Metros a Pies.')
    print('2. Grados C a grados F.')
    print('3. Grados F a grados C.')
    print('4. Kilometros a Millas.')
    print('5. Salir del programa.')
    
    # Manejo de error sobre el ingreso numerico de la opcion
    try:
        opcion = int(input('\nIngrese la opcion del menu deseada: '))
    except ValueError:
        print('\nDebes ingresar un numero valido del menu mostrado.\n')
        continue # Retornara al menu
       
    # Verifica que la opcion sea 1, que es para convertir los metros a pies
    if opcion == 1:
        print('\n========== Metros a Pies ==========')
            
        # Manejo de error sobre el ingreso del valor de metros
        try:
            metros = float(input('\nIngrese los metros: '))

            # Se calcula y redondea el resultado de la conversion a 2 decimales
            pies = round(metros * 3.281, 2)
            
            # Se muestra el resultado
            print(f'\nLos {metros} metros a pies son: {pies}')
        
        except ValueError as error:
            print(f'\nError de tipo ValueError: {error}')
            continue # Retorna al menu
                    
    # Verifica que la opcion sea 2, que es para la conversion de grados c a grados f
    elif opcion == 2:
        print('\n========== Grados C a Grados F ==========')
        
        # Manejo de error sobre el ingreso del valor de los grados c
        try:
            grados_c = float(input('\nIngrese los grados c: '))

            # Realiza la conversion
            grados_f = (grados_c * 1.8) + 32
            
            # Se redonda la conversion a 2 decimales
            grados_f = round(grados_f, 2)
            
            # Mostrar el resultado
            print(f'\nLos grados {grados_c}°C a Fahrenheit son: {grados_f}°F.')
                
        except ValueError as error:
            print(f'\nError de tipo ValueError: {error}')
            continue # Retorna al menu
            
    # Verifica que la opcion sea 3, que es para convertir los grados f a grados c
    elif opcion == 3:
        print('\n========== Grados F a Grados C ==========')
            
        # Manejo de error sobre el ingreso del valor de los grados f
        try:
            grados_fa = float(input('\nIngrese los grados F: '))
                
            # Realiza la conversion
            grados_cen = (5/9) * (grados_fa - 32)
            
            # Se redondea el resultado a 2 decimales
            grados_cen = round(grados_cen, 2)
            
            # Se muestra el resultado
            print(f'\nLos grados {grados_fa}°F a centigrados son: {grados_cen}°C.')
            
        except ValueError as error:
            print(f'\nError de tipo ValueError: {error}')
            continue # Retorna al menu
    
    # Se verifica que la opcion sea 4, que es para convertir los kilometros a millas
    elif opcion == 4:
        print('\n========== Kilometros a Millas ==========')
             
        # Manejo de error sobre el ingreso del valor de los kilometros
        try:
            kilometros = float(input('\nIngresa los kilometos: '))
                
            # Iniciar el valor de Una milla para multiplicarlo con los kilometros ingresados
            valor_millas = 0.62137
            
            # Se realiza la conversion y se redondea a 4 decimales
            millas = round(kilometros * valor_millas, 4)
            
            # Se muestra el resultado
            print(f'\nLos {kilometros}km a millas son: {millas}')
                
        except ValueError as error:
            print(f'\nError de tipo ValueError: {error}')
            continue # Retorna al menu
            
    # Verifica que la opcion sea 5, que es para finalizar el menu
    elif opcion == 5:
        print('\n========== Saliendo del programa ==========')
        print('\nFin del programa. Gracias por utilizar nuestro conversor.\n')
        break # fin del bucle      
    else:
        print('\nOpcion invalida ingresada. Debe ser una del menu mostrado.\n')
        continue # Retorna al menu