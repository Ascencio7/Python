# Los Operadores en Python
# OPERADORES ARITMETICOS
print(8 + 10)
print(8 - 10)
print(8 * 10)
print(8 / 10)
print(8 // 10)
print(8 % 10)
print(2 ** 5) # y todos los simbolos se pueden combinar

# sumar dos cadenas
print("Hola " + "Vladi") # es la unica operacion con operador que se puede usar con cadenas de string

print("Hola " + str(5)) # se puede concatenar numeros pero se deben convertir a string con 'str'

print("Vladi " * 5) # una cadena puede ser multiplicada varias veces siempre y cuando sea un numero entero

# Pero no es habitual hacerlo


# OPERADORES COMPARATIVOS
print("\n")
print(5 > 10)
print(8 < 10)
print(10 >= 20)
print(10 <= 20)
print(10 == 20)
print(10 != 20)

# Se pueden comparar las cadenas de texton tambien
# pero compara por orden alfabetico
print("\n")

# ordena por orden ASCII
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")


# OPERADORES LOGICOS
print(10 == 10 and 20 <= 40 )
print(10 != 10 or 10 != 20 )
print(not(10 > 20)) # not es para negar toda la condicion, false es true, si es true es false