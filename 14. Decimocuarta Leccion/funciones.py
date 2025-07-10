def dato_lista_buscar(dato_buscar, lista):
    r = False
    
    for i in lista:
        if i == dato_buscar:
            r = True
            
    return r

mi_lista = [1, 2, 3, 4, 5]

dato = int(input('\nIngresa un dato a buscar: '))

if dato_lista_buscar(dato, mi_lista):
    print('\nSe encontro el dato.\n')
else:
    print('\nNo se encontro el dato.\n')
    
print('\nFin del programa.\n')