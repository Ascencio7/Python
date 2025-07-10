"""
    Construir una funcion que reciba una cadena digitada (como parametro) por el usuario y que lo muestre
    'n' veces en pantalla. El valor de n tambien es digitado por el usuario.
"""

def cadena_digitada(string_ingresado, cant):
    for _ in range(cant):
        print(string_ingresado)
        

cadena = input('\nIngresa la cadena: ')
cant = int(input('Ingresa la cantida de veces a mostrar la cadena: '))

print('\n')
cadena_digitada(cadena, cant)
print('\nFin del programa.\n')