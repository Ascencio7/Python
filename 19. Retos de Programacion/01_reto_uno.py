"""
    * Escribe un programa que muestre por consola (con un print) los
    * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    * cada impresión), sustituyendo los siguientes:
    * - Múltiplos de 3 por la palabra "fizz".
    * - Múltiplos de 5 por la palabra "buzz".
    * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
  
"""

# Se itera en un bucle for
for i in range(1, 101):
    # Se comprueba que sea multiplo de 3 y 5.
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz') # Si es asi, se imprime la palabra completa
    # Sino, se comprueba si es multiplo de 3
    elif i % 3 == 0:
        print('fizz') # Si es asi, se imprime la palabra fizz
    # Sino, se comprueba que sea multiplo de 5
    elif i % 5 == 0:
        print('buzz') # Si es asi, se imprime la palabra buzz
    # Si no se cumple ninguna, se imprime el numero como tal
    else:
        print(i)