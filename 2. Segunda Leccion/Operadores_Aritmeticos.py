# Comentario de una linea
""" 
Comentario
de 
varias 
lineas
"""

# 2. Leccion 2: Operadores Aritmeticos

# Se almacenan valores en variables con datos enteros
var1 = 5
var2 = 3

# 1. Se calcula la suma
print("\nResultado de la suma:")
suma = var1 + var2
print(var1, "+", var2, "=", suma) # Otra forma de imprimir datos


# 2. Se calcula la resta
print("\nResultado de la resta:")
resta = var1 - var2
print(var1, "-", var2, "=", resta)


# 3. Se calcula la multiplicacion
print("\nResultado de la multiplicacion:")
multi = var1 * var2
print(var1, "x", var2, "=", multi)


# 4. Se calcula la division
print("\nResultado de la division:")
division = var1 / var2
# Redondear y mostrar 2 decimales
division = round(division, 2)
print(var1, "/", var2, "=", division)


# 5. Se calcula la division entera
print("\nResultado de la division entera:")
division_Entera = var1 // var2
# Redondear y mostrar 2 decimales
division = round(division, 2)
print(var1, "//", var2, "=", division_Entera)


# 6. Se calcula el modulo
print("\nResultado del modulo:")
modulo = var1 % var2
# Redondear y mostrar 2 decimales
modulo = round(modulo, 2)
print(var1, "%", var2, "=", modulo)


# 7. Se calcula la potencia
print("\nResultado de la potencia:")
potencia = var1 ** var2
print(var1, "^", var2, "=", potencia)