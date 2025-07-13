"""
    Construir una funcion que reciba dos datos enteros y retorne el dato mayor.
"""

# Se crea la funcion para ver cuál es el numero mayor
def numero_mayor(num_1, num_2):
    # Se verifica si el numero 1 es mayor que el numero 2
    if num_1 > num_2:
        # Se crea una variable que guarda el mensaje
        resultado = f'\nEl {num_1} es mayor que {num_2}\n'
        # Se retorna el resultado
        return resultado
    # Se verifica si el numero 2 es mayor que el numero 1
    elif num_2 > num_1:
        # Se crea una variable que guarda el mensaje
        resultado = f'\nEl {num_2} es mayor que {num_1}\n'
        # Se retorna el resultado
        return resultado
    # Se verifica que si los dos numeros son iguales
    else:
        # Se crea una variable que guarda el mensaje
        resultado = '\nLos numeros son iguales\n'
        # Se retorna el resultado
        return resultado
    
# Se imprime, se llama a la funcion y se les pasa los dos numeros a comprobar.
print(numero_mayor(2, 12))