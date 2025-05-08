# Tipos de variables en Python

# 1. Tipo String
nombre = "Vladimir Ascencio"
print(nombre)

# 2. Tipo Int, numeros enteros
edad = 21
print(edad)

# 3. Tipo float, numeros con decimales
suma = 3.48 + 88.384
# Se redondea a 2
suma = round(suma, 2)
print(suma)

# 4. Variables con texto y +
var1 = "Hola"
var2 = "Adios"
print(var1 + " " + var2)

# 5. Variables con texto con +=
var2 += nombre
print(var2)

# 6. Cadenas con vales numericos
v1 = 3
v2 = "Valor = "
v2 += v2 + str(v1)
print(v2)

# 7. Encontrar una subcadena dentro de otra cadena
var1 = "Unamano"
var2 = "ano"
buscar_Cadena = var1.find(var2)
print(buscar_Cadena) # Dara el numero 4 porque busca la primera letra y aca se cuenta la primera
# posicion 0 hasta n.

# 7.1 Mostrar la palabra que se quiere buscar
var1 = "Unamano"
extraer_Cadena = var1[3:7]
print(extraer_Cadena)

# 8. Numeros complejos
num1 = 7 + 5j
print(num1)

# 9. Tipos Booleanos
apagado = True
encendido = False

print(apagado)
print(encendido)