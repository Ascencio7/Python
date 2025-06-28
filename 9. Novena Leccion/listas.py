# Las Listas

# Con () o [] se declaran las listas
mi_lista = list()
mi_otra_lista = []

mi_lista = ('Hola', 23.4, True)
mi_otra_lista = ['Banana', (89 + 100), False]

print(mi_lista)
print(len(mi_lista)) # contara cuantos elementos hay en la lista

print(mi_otra_lista)

lista_edades = [21, 45, 65, 30, 30, 17, 20, 19]

print(lista_edades)

print(lista_edades[1]) # mostrara solo el elemento 45.

print(lista_edades[1::]) # mostra 45 hasta el ultimo elemento

print(len(lista_edades))

print(type(lista_edades))

print(lista_edades[-1]) # imprime el ultimo elemento

# en reverso no existe el -0 para iniciar desde el ultimo

# Count: retorna el numero de ocurrencias de un valor

print(mi_otra_lista.count('Banana'))

print(mi_otra_lista.count(189))


# Contar elementos de la propia lista


# Se pueden asignar los valores de la lista a variables creadas en una sola linea
# y necesita todos los elementos en orden, no se puede asignar 3 variables con una lista de 5 elementos
palabra, suma, boleano = mi_otra_lista

print(palabra)
print(suma)
print(boleano)


# aunque hacerlo es un posible foco de errores


# sumar listas
print(mi_lista, mi_otra_lista, lista_edades)

# crear listas en print
print(list([1,2,3,4,5]))
print([1,2,3,4,5])


mi_otra_lista.insert(1, "Negro")
print(mi_otra_lista)

mi_otra_lista.remove("Negro") # se debe pasar el elemento a eliminar
print(mi_otra_lista)


# operaciones propias de los arrays: Las Colas
# mi_lista.pop()
# print(mi_lista.pop())
# no me encuentra pop

# del mi_lista(2)
# print(mi_lista)

# mi_lista.clear()
# print(mi_lista)

# no me funciona xd

mi_otra_lista.insert(1, "Rojo")
print(mi_otra_lista)

# cambiar de valor
mi_otra_lista[1] = "Azul" # reemplaza el valor
print(mi_otra_lista)

# crear una nueva referencia y ha copiado el objeto: copia los elementos de la lista
mi_nueva_lista = mi_otra_lista.copy()
print(mi_nueva_lista)

# dar la vuelta a la lista
mi_otra_lista.reverse()
print(mi_otra_lista)

lista_edades.sort() # ordena la lista
print(lista_edades)

print(mi_nueva_lista[1:3])
print(mi_nueva_lista)