# Tuplas

# definir la tupla
mi_tupla = tuple()

mi_otra_tupla = ()

# estas son las dos formas de definir las tuplas
# Una vez creadas NO SE PUEDEN MODIFICAR
mi_tupla = (21, 1.69, "Vladimir", "Ascencio")

mi_otra_tupla = (21, 21, 30, 27, 27, 28, 30, 31)

print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[0])
print(mi_tupla[1])
print(mi_tupla[-1]) # el ultimo elemento

# operaciones
print(mi_tupla.count("Ascencio")) # como las listas, retorna las coincidencia encontradas
print(mi_tupla.index("Vladimir"))
print(mi_tupla.index("Ascencio"))

print(mi_tupla + mi_otra_tupla) # no se modifica pero si se suman la tuplas

mi_suma_tupla = mi_tupla + mi_otra_tupla
print(mi_suma_tupla)

print(mi_suma_tupla[3:5])

# NO SE PUEDE MODIFICAR LAS TUPLAS 

# Si en verdad se quiere modificar las tuplas, se debe reasignar el valor
mi_tupla = list(mi_tupla)

print(type(mi_tupla))

# si se desea, si es necesario cambiar la tupla, se hace lo anterior y lo siguiente:
mi_tupla[1] = 1.70 # modificar un dato
mi_tupla.insert(1, "Negro") # insertar un nuevo dato en una posicion especifica

# volver a reasignar el valor de una tupla
mi_tupla = tuple(mi_tupla)

print(type(mi_tupla))
print(mi_tupla)

# del mi_tupla[2] no se puede borrar un elemento de la tupla

# Borrar una tupla
del mi_tupla
# print(mi_tupla) da error porque ya no esta definida porque fue borrada