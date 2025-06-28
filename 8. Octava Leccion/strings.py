# Stings

mi_cadena = "Vladimir Ascencio"# string con dobles comillas
mi_segunda_cadena = 'Vladi' # string con comillas simples
# ambas forman estan correctas, no habra problemas

print(len(mi_cadena)) # muestra la longitud del string no de la variable
print(len(mi_segunda_cadena))

# se pueden concatenas/sumar las cadenas
print(mi_cadena + " " + mi_segunda_cadena)

# Los strings pueden llevar ciertos caracteres
mi_nueva_linea = "Este es un string \ncon salto de linea"
print(mi_nueva_linea)

# tabulaciones en string
mi_tab_nueva_linea = "\tEste es un string con tabulacion"
print(mi_tab_nueva_linea)

# string con scape
mi_scape_nueva_linea = "\tEste es un string \nescapado"
print(mi_scape_nueva_linea)

# como formatear el string
name, lastname, edad = 'Vladimir', 'Ascencio', 21

print("Mi nombre es {} {} y mi edad es {}".format(name, lastname, edad)) # usando format

print("Mi nombre es %s %s y mi edad es %d" %(name, lastname, edad)) # usando el %s --> string y %d --> numero si de verdad se formatea

print(f"Mi nombre es {name} {lastname} y tengo {edad} años de edad.") # usando la inferencia de datos

# esta manera no es tan optima, es cutre xd
# print("Mi nombre es " + name + " " + lastname + " y mi edad es " + str(edad))


# Desempaquetado de caracteres: segun la longitud del texto se crean las variables
lenguaje = 'Python'
a, b, c, d, e, f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division de caracteres
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:2] # se puede obviar algunos caracteres
print(lenguaje_slice)


# Dar la vuelta al string
reversed_lenguaje = lenguaje[::-1] # una manera sencilla de darle vuelta al string
print(reversed_lenguaje)


# Funciones

print(lenguaje.capitalize()) # convierte la primer letra en mayuscula
print(lenguaje.upper()) # convierte el texto a mayuscula
print(lenguaje.lower()) # para minusculas
print(lenguaje.swapcase()) # convierte todo en mayuscula menos el primer elemento
print(lenguaje.count("t")) # cuenta cuantas coincidencias hay en la cadena
print(lenguaje.isnumeric()) # verifica si es numero
print("1".isnumeric())
print(lenguaje.upper().isupper()) # isupper verifica comprueba si esta en mayuscula la cadena
print(lenguaje.lower().islower()) #isupper verifica comprueba si esta en minuscula la cadena
print(lenguaje.startswith("py")) # verifica si la cadena inicia con un cierto caracter, pero diferencia entre mayusculas y minusculas