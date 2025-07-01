# Los Diccionarios: Es como una clave y valor

mi_dic = dict()
mi_otro_dic = {}

print(type(mi_dic))
print(type(mi_otro_dic))

mi_otro_dic = {
    "Nombre": "Vladimir",
    "Apellido": "Ascencio",
    "Edad": 21,
    1:"Python"
}

print(mi_otro_dic)
print(type(mi_otro_dic))

print(mi_otro_dic["Nombre"])


# dentro de un dic se puede tener otro diccionario, un set
mi_dic = {
    "Nombre": "Vladimir",
    "Apellido": "Ascencio",
    "Edad": 21,
    "Lenguajes":{"Python", "C#", "MySQL"}, # un set dentro de un diccionario
    1: 1.70
}

print(mi_dic)
print(len(mi_dic))
print(mi_dic["Lenguajes"])

print(mi_dic["Nombre"])

# Actualizar el dato
mi_dic["Nombre"] = "Jonathan"
print(mi_dic["Nombre"])

print(mi_dic[1]) # se debe representar si entero o string

# Agrar un nueva clave y valor al diccionario
mi_dic["Ciudad"] = "Lourdes Colon"
print(mi_dic)


# Borra todas las claves valores del diccionario
# mi_dic.clear()
# print(mi_dic)

# se puede eliminar una clave en el diccionario con del
del mi_dic["Ciudad"]

print(mi_dic)


# Comprobar si un dato esta en el diccionario
print("Nombre" in mi_dic) # verifica que el campo exista

# para acceder al campo
print(mi_dic["Nombre"])


print(mi_dic.items()) # se obtiene el diccionario
print(mi_dic.keys()) # solo las claves formato lista
print(mi_dic.values()) # obtiene los valores 


mi_lista = ["Nombre", 1, "Piso"]

# Se crea un nuevo diccionario sin valores
mi_nuevo_dic = dict.fromkeys(mi_lista)
print(mi_nuevo_dic)
print(type(mi_nuevo_dic))

mi_nuevo_dic = dict.fromkeys(("Nombre", 1, "Piso"))
print(mi_nuevo_dic)

mi_nuevo_dic = dict.fromkeys(mi_dic) # tiene sentido crearlo
print(mi_nuevo_dic) # obtiene todas las claves, de ahi uno agrega los valores

mi_nuevo_dic = dict.fromkeys(mi_dic, "Allison") # si es asi, en todas las claves tendran esos valores
print(mi_nuevo_dic)

# no es diccionario ni listado
mi_values = mi_nuevo_dic.values()
print(type(mi_values))


print(mi_nuevo_dic.values())

# Se crea un diccionario de las fromkeys de un diccionario de sus valores que es una lista
print(dict.fromkeys(list(mi_nuevo_dic.values())).keys())


# Si se quiere un listado como tal, se debe transformarlo a una lista
print(list(mi_nuevo_dic))

print(tuple(mi_nuevo_dic))

print(set(mi_nuevo_dic))