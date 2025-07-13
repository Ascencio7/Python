"""
    Construir una funcion que reciba un valor entero y muestre la tabla de multiplicar de dicho numero.
"""

# Se crea la funcion con el parametro del numero
def numero_tabla(num):
    # Se itera de un rango de 1 a 10 (los valores inician desde 0 por eso el 11 = 10)
    for i in range(1,11):
        # Se crea una variable que guarda la multiplicacion del numero por la variable iteradora 'i'
        resultado = num * i
        # Se impreme el resultado
        print(f'{num} x {i} = {resultado}')
        
# Se usa un bucle while y manejo de errores
while True:
    try:
        # Se solicita el numero
        numero = int(input('\nIngresa el numero de la tabla: '))
    # Si se ingresa no numerico se muestra el siguiente mensaje
    except ValueError:
        print('\nDebes ingresar un numero valido.\n')
        continue # Retorna de nuevo a la solicitud del numero
    else:
        # Si esta correcto, se llama a la funcion y se pasa el numero
        numero_tabla(numero) # Imprime la tabla de multiplicar
        break # Se rompre el bucle