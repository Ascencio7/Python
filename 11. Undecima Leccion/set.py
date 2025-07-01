# Los SET: No es una estructura ordenada. No existe acceder a un elemento en especifico
# SET no admite REPETIDOS

""" 
    Ventajas:
    
        No acepta repetidos
        Trabajar con datos que no son ordenados (depende de la necesidad)
        
"""

mi_set = set() # forma de declarar un set
print(type(mi_set)) # verificar que tipo es

mi_otro_set = {}

print(type(mi_otro_set)) # esto es un diccionario

mi_otro_set = { # al hacerlo asi el dic se vuelve un set
    "Vladimir",
    "Ascencio",
    21
}

print(mi_otro_set)
print(type(mi_otro_set))

# Operaciones a nivel sistema
print(len(mi_otro_set)) # cuenta cuantos elementos

mi_otro_set.add("VladiDev")

print(mi_otro_set)

# NO ADMITE AGREGAR ELEMENETOS REPETIDOS
mi_otro_set.add("VladiDev")

print(mi_otro_set)

# NO SE IMPRIMIRA EL DATO PORQUE YA EXISTE


# Se puede reazilar busquedas en los set

print("Ascencio" in mi_otro_set)
print("Vladi" in mi_otro_set)

# devolveran TRUE o FALSE

# Se pueden eliminar datos
mi_otro_set.remove(21) # elimino la edad
print(mi_otro_set)


# El CLEAR: Limpia/borra todos los elementos del SET

mi_otro_set.clear()
print(mi_otro_set)


# del

del mi_otro_set
# print(mi_otro_set) # NameError: name 'mi_otro_set' is not defined


mi_set = {
    "Vladimir",
    "Ascencio",
    21
}

# ES MUY ARRIESGADO CONVERTIR UN SET A UNA LISTA
# YA QUE NO SE SABE EL ORDEN DE LOS DATOS

mi_lista = list(mi_set)
print(mi_lista)
print(mi_lista[0])


# unir los dos sets

mi_otro_set = {
    "Python",
    "C#",
    "MySQL",
    "SQL Server"
}

# Se une un set con la palabra reservada 'union'
mi_nuevo_set = mi_set.union(mi_otro_set)

# No pasa nada si se une de nuevo el set, pues NO ADMITE REPETIDOS
print(mi_nuevo_set.union(mi_nuevo_set))

# Agregar más datos al set en una línea
mi_nuevo_set = mi_nuevo_set.union({
    "HTML", 
    "CSS", 
    "JavaScript", 
    "MongoDB"
})

print(mi_nuevo_set)


# Diferencia: Muestra la diferencia de los elementos de mi_nuevo_set del mi_set
print(mi_nuevo_set.difference(mi_set))