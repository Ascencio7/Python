# Declarando la lista vacia

list_nombres = []
list_edades = []
lst_estaturas = []


# Como se va a definir el listado se usa el bucle for
for i in range(5):
    list_nombres.append(input('\nIngresa el nombre: ')) # se solicitan los datos
    list_edades.append(input('Ingresa la edad: '))
    lst_estaturas.append(input('Ingresa la estatura: '))
    print('\n')
    
    
# Se imprimen los resultados
for x in range(5):
    print(f'\nEstudiante N°{x+1}:\n')
    print(f'Nombre: {list_nombres[x]}\nEdad: {list_edades[x]}\nEstatura: {lst_estaturas[x]}')
    
print('\nFin del programa...')