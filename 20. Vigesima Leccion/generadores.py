# Generadores

"""
    Construir un programa, utilizando funciones, que muestre los multiplos de 3 en el rango de 1 a tope siendo numero un valor especificado.
"""

# Usando una funcion como tal
def multiplo_tres(numero): # Se define la funcion
    num = 3 # se inicia la variable con el valor de 3
    mi_lista = [] # Se crrea una lista vacia
    while num < numero: # Se inicia un bucle while que se ejecuta mientras num sea menor que el numero ingresado
        mi_lista.append(num) # Si es asi se agrega a la lista el numero
        num += 3 # Se incrementa en 3 para obtener el multiplo del siguiente numero
    return mi_lista # Y se retorna la lista con los multiplos

# Se prueba la funcion
print('\n')
print(multiplo_tres(20))
print(multiplo_tres(50))


# Ejemplo usando generador
def multi_tres(numero): # Se crea la funcion
    num = 3 # Se inicia con valor de 3
    while num < numero: # Mientras que num sea menor que el numero ingresado
        yield num # Retorna el numero y que temporalmente pause el funcionamiento de la funcion mientras se realiza el proceso
        num += 3 # Se incrementa en 3

# Almacena el resultado de la funcion con una variable
multi_gen = multi_tres(20) # Se le pasa el valor

print('\n')
for i in multi_gen: # Por cada valor almacenado en i que esta en 'multi_gen'
    print(i) # Que muestre el valor de i
print('\n')