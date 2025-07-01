"""
    Hacer diferentes listados de una lista de 15 numeros segun el siguiente criterio:
    
    si numero >=0 y < 50, ponerlo en lista1
    Si numero >= 50 y <100, ponerlo en lista2
    Si numero >= 100 y <=150, ponerlo en lista3
    
"""

# Declarar las listas
list_uno = []
list_dos = []
list_tres = []


# Usar un bucle for por ser 15 iteraciones necesarias
for i in range(15):
    numero = int(input(f'\n[{i+1}/15] Ingresa un numero: ')) # solicitar el dato
    
    # Verificar las condiciones que pide el ejercicio
    if 0 <= numero < 50:
        list_uno.append(numero) # se agrega a la lista los numeros de la condicion
        list_uno.sort() # ordena la lista de menor a mayor
    elif 50 <= numero < 100:
        list_dos.append(numero)
        list_dos.sort()
    elif 100 <= numero <=150:
        list_tres.append(numero)
        list_tres.sort()
    else:
        print("El numero no esta en el rango, no se agrego a las listas.")
        
        
# Mostrar los resultados
print('\nResultados:')
print(f'Lista Uno: {list_uno}')
print(f'Lista Dos: {list_dos}')
print(f'Lista Tres: {list_tres}')
print(f'Fin del programa...')