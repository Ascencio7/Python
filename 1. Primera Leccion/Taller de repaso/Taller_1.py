# Ejercicios para practicar

# 1. Construir un programa que muestre su nombre completo
print("\n1. Construir un programa que muestre su nombre completo.")

myName = 'Jonathan Vladimir Ascencio Ramos'

print(myName)


# 2. Construir un programa que muestre su nombre completo centrado en la ventana de ejecución
print("\n2. Construir un programa que muestre su nombre completo centrado en la ventana de ejecución.")
ancho = 500; # Aqui defino el centrado para el texto
nameCenter = myName.center(ancho)

print(nameCenter)


# 3. Construir un programa que almacene dos valores y muestre su suma.
print("\n3. Construir un programa que almacene dos valores y muestre su suma.")

num1 = 100
num2 = 50
suma = num1 + num2

print(f"\nLa suma entre {num1} y {num2} es: {suma}")


# 4. Construir un programa que almacene dos valores y muestre su producto
print("\n4. Construir un programa que almacene dos valores y muestre su producto")

num1 = 673.83
num2 = 3.3
producto = num1 * num2
# Redondear y mostrar 2 decimales
producto = round(producto, 2)

print(f"\nEl producto entre {num1} y {num2} es: {producto}")


# 5. Construir un programa que almacene dos valores y muestre el resultado de su resta.
print("\n5. Construir un programa que almacene dos valores y muestre el resultado de su resta.")

num1 = 783
num2 = 198
resta = num1 - num2

print(f"\nLa resta entre {num1} y {num2} es: {resta}")


# 6. Construir un programa que almacene dos valores y muestre el resultado de su division
num1 = 892
num2 = 100
division = num1 / num2

print(f"\nLa división entre {num1} y  {num2} es: {division}")


# 7. Construir un programa que muestre la 1° ocurrencia de la cadena "verso" en la palabra "Universo"
print("\n7. Construir un programa que muestre la 1° ocurrencia de la cadena 'verso' en la palabra 'Universo'.")

var1 = "Universo"
var2 = "verso"
buscar_Cadena = var1.find(var2)
print("\nSe encuentra en la posición: " + str(buscar_Cadena))


# 8. Construir un programa que concatene sus nombres con sus apellidos.
print("\n8. Construir un programa que concatene sus nombres con sus apellidos.")
firstName = "Jonathan Vladimir"
lastName = "Ascencio Ramos"

print("\nNombres: " + firstName + ", Apellidos: " + lastName)


# 9. Construir un programa que escriba su nombre y al frente escriba su edad.
print("\n9. Construir un programa que escriba su nombre y al frente escriba su edad.")
edad = 21
print("\nNombre: " + myName + ", Edad: " + str(edad))


# 10. Construir un programa que escriba su nombre, edad y su estatura en el mismo renglon utilizando variables.
print("\n10. Construir un programa que escriba su nombre, edad y su estatura en el mismo renglon utilizando variables.")
estatura = 1.69
print("\nNombre: " + myName + ", Edad: " + str(edad) + ", Estatura: " + str(estatura))