# Calculadora basica con funciones y manejo de errores


# Funciones a usar


# Funcion de sumar que retornaria la suma de dos numeros
def funcion_sumar(num_uno, num_dos):
    return round(num_uno + num_dos, 2)
  
    
# Funcion de restar que retornaria la resta de dos numeros
def funcion_restar(num_uno, num_dos):
    return round(num_uno - num_dos, 2)


# Funcion de multiplicar que retornaria la multiplicacion de dos numeros
def funcion_multiplicar(num_uno, num_dos):
    return round(num_uno * num_dos, 2)


# Funcion de dividir que retornaria la division de dos numeros
def funcion_dividir(num_uno, num_dos):
    # Se hace un manejo de errores
    try:
        # Se crea una variable 'resultado' para guardar la division
        resultado = round(num_uno / num_dos, 2)
        return resultado # Retorna el resultado de la division
    except ZeroDivisionError: # Se realiza una excepcion por el error de dividir un numero con 0
        # Se muestra el siguiente mensaje
        print('\nNo se puede dividir un numero con 0.\n') 
        return None # Y retorna un valor nulo
    
    
# Funcion de Modulo que retornaria el valor del modulo de dos numeros
def funcion_modulo(num_uno, num_dos):
    # Se hace un manejo de errores
    try:
        # Se crea una variable 'resultado' para guardar la operacion del modulo
        resultado = round(num_uno % num_dos, 2)
        return resultado # Retorna el resultado del modulo
    except ZeroDivisionError: # Se realiza una excepcion por el error calcular el modulo con un numero 0
        # Se muestra el siguiente mensaje
        print('\nNo se puede calcular el modulo de un numero con 0.\n')
        return None # Y retorna un valor nulo
    
    
# Funcion de Modulo que retornaria el valor del modulo de dos numeros
def funcion_division_entera(num_uno, num_dos):
    # Se hace un manejo de errores
    try:
        # Se crea una variable 'resultado' para guardar la division
        resultado = round(num_uno // num_dos, 2)
        return resultado # Retorna el resultad de la division entera
    except ZeroDivisionError: # Se realiza una excepcion por el error calcular la division entera con un numero 0
        # Se muestra el siguiente mensaje
        print('\nNo se puede calcular la division entera de un numero con 0.\n')
        return None

# Fin de las funciones para la calculadora


# Iniciar la variable 'opcion' a usar para el menu en 0
opcion = 0

# Se crea un bucle while true con las opciones del menu
while True:
    print('\n========== CALCULADORA BASICA ==========\n')
    print('1. Sumar dos numeros.')
    print('2. Restar dos numeros.')
    print('3. Multiplicar dos numeros.')
    print('4. Dividir dos numeros.')
    print('5. Modulo de dos numeros.')
    print('6. Division Entera de dos numeros.')
    print('7. Salir del programa.')
    
    # Se hace un manejo de errores para evitar que al ingresar un tipo diferente se cierre el programa
    try:
        # Se pide que se ingrese una opcion
        opcion = int(input('\nElige una opcion: '))
    except ValueError:
        # Si ingresar un valor diferente se muestra el siguiente mensaje
        print('\nDebes ingresar una opcion del menu mostrado (1-5).\n')
        continue # Retorna al menu de nuevo
    
    # Verifica que sea la opcion 1 que es la de sumar
    if opcion == 1:
        print('\n========== SUMAR DOS NUMEROS ==========\n')
        
        # Se hace un manejo de errores para capturar el valor de los dos numeros
        try:
            num_uno = float(input('Ingresa el primer numero: '))
            num_dos = float(input('Ingresa el segundo numero: '))
            
            # Se crea una variable para llamar a la funcion y se pasa las dos variables solicitadas
            resultado = funcion_sumar(num_uno, num_dos)
            
            # Se muestra el resultado
            print(f'\nSumar {num_uno} y {num_dos} es igual a: {resultado}\n')
            
        except ValueError:
            print('\nDebes ingresar un numero valido.\n')
            continue # Retorna al menu
    
    # Verifica que sea la opcion 2 que es la de restar
    elif opcion == 2:
        print('\n========== RESTAR DOS NUMEROS ==========\n')
        
        # Se hace un manejo de errores para capturar el valor de los dos numeros
        try:
            num_uno = float(input('Ingresa el primer numero: '))
            num_dos = float(input('Ingresa el segundo numero: '))
            
            # Se crea una variable para llamar a la funcion y se pasa las dos variables solicitadas
            resultado = funcion_restar(num_uno, num_dos)
            
            # Se muestra el resultado
            print(f'\Restar {num_uno} y {num_dos} es igual a: {resultado}\n')

        except ValueError:
            print('\nDebes ingresar un numero valido.\n')
            continue # Retorna al menu
        
    # Verifica que sea la opcion 3 que es la de restar
    elif opcion == 3:
        print('\n========== MULTIPLICAR DOS NUMEROS ==========\n')
        
        # Se hace un manejo de errores para capturar el valor de los dos numeros
        try:
            num_uno = float(input('Ingresa el primer numero: '))
            num_dos = float(input('Ingresa el segundo numero: '))
            
            # Se crea una variable para llamar a la funcion y se pasa las dos variables solicitadas
            resultado = funcion_multiplicar(num_uno, num_dos)

            # Se muestra el resultado
            print(f'\nMultiplicar {num_uno} y {num_dos} es igual a: {resultado}\n')
            
        except ValueError:
            print('\nDebes ingresar un numero valido.\n')
            continue # Retorna al menu
        
    # Verifica que sea la opcion 4 que es la de dividir
    elif opcion == 4:
        print('\n========== DIVIDIR DOS NUMEROS ==========\n')
        
        # Se hace un manejo de errores para capturar el valor de los dos numeros
        try:
            num_uno = float(input('Ingresa el primer numero: '))
            num_dos = float(input('Ingresa el segundo numero: '))
            
            # Se crea una variable para llamar a la funcion y se pasa las dos variables solicitadas
            resultado = funcion_dividir(num_uno, num_dos)
            
            # Verifica si el resultado no es nulo, entonces se muestra el resultado de la division
            if resultado is not None:
                print(f'\nDividir {num_uno} y {num_dos} es igual a: {resultado}\n')
                
            # Si es el resultado es None, entonces mostrara el mensaje de error de la funcion creada anteriormente
        
        except ValueError:
            print('\nDebes ingresar un numero valido.\n')
            continue # Retorna al menu
        
    # Verifica que la opcion sea 5 que es la del modulo
    elif opcion == 5:
        print('\n========== MODULO DOS NUMEROS ==========\n')
        
        # Se hace un manejo de errores para capturar el valor de los dos numeros
        try:
            num_uno = float(input('Ingresa el primer numero: '))
            num_dos = float(input('Ingresa el segundo numero: '))
            
            # Se crea una variable para llamar a la funcion y se pasa las dos variables solicitadas
            resultado = funcion_modulo(num_uno, num_dos)
            
            # Verifica si el resultado no es nulo, entonces se muestra el resultado del modulo
            if resultado is not None:
                print(f'\nEl Modulo de {num_uno} y {num_dos} es igual a: {resultado}\n')
            
            # Si es el resultado es None, entonces mostrara el mensaje de error de la funcion creada anteriormente
            
        except ValueError:
            print('\nDebes ingresar un numero valido.\n')
            continue # Retorna al menu
        
    # Verifica que la opcion sea 6 que es la division entera
    elif opcion == 6:
        print('\n========== DIVISION ENTERA DE DOS NUMEROS ==========\n')
        
        # Se hace un manejo de errores para capturar el valor de los dos numeros
        try:
            num_uno = float(input('Ingresa el primer numero: '))
            num_dos = float(input('Ingresa el segundo numero: '))
            
            # Se crea una variable para llamar a la funcion y se pasa las dos variables solicitadas
            resultado = funcion_division_entera(num_uno, num_dos)
            
            # Verifica si el resultado no es nulo, entonces se muestra el resultado de la division entera
            if resultado is not None:
                print(f'\nLa division entera de {num_uno} y {num_dos} es igual a: {resultado}\n')
            
            # Si es el resultado es None, entonces mostrara el mensaje de error de la funcion creada anteriormente
            
        except ValueError:
            print('\nDebes ingresar un numero valido.\n')
            continue # Retorna al menu

    # Verifica que sea la opcion 5 que es para cerrar el programa
    elif opcion == 7:
        print('\n========== Saliendo del programa ==========\n')
        print('Fin del programa.\n')
        break # Fin del bucle