# 1. Construir un programa que reciba dos numeros enteros y calcule el resultado de elevar el 1° numero leido a la potencia representada
# por el 2° numero leido.
print("\n1. Construir un programa que reciba dos numeros enteros y calcule el resultado de elevar el 1° numero leido a la potencia representada por el 2° numero leido.")

num1 = int(input("\nIngrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

potencia = num1 ** num2

print(f"El numero {num1} elevado a la potencia de {num2} es: {potencia}")



# 2. Construir un programa que reciba un numero entero y obtenga su mitad entera.
print("\n2. Construir un programa que reciba un numero entero y obtenga su mitad entera.")

num = int(input("\nIngresa un numero entero: "))

mitad = num // 2

print(f"\nLa mitad entera de {num} es: {mitad}")



# 3. Constuir un programa que reciba un numero entero y muestre su ultimo digito.
print("\n3. Constuir un programa que reciba un numero entero y muestre su ultimo digito.")

num_ultimo_digito = int(input("\nIngresa un numero entero para saber su ultimo digito: "))

ultimo_digito = num_ultimo_digito % 10

print(f"\nEl ultimo digito de {num_ultimo_digito} es {ultimo_digito}")



# 4. Construir un programa que reciba un numero entero y muestre el resultado de sumar sus dos ultimos digitos.
print("\n4. Construir un programa que reciba un numero entero y muestre el resultado de sumar sus dos ultimos digitos.")

num = float(input("\nIngresa el numero: "))

last_digito = num % 10
penul_digitos = (num // 10) % 10
suma_digitos = last_digito + penul_digitos

print(f"\nLa suma entre los ultimos digitos de {num} es {suma_digitos}")



# 5. Construir un programa que reciba un numero entero y muestre el resultado de elevar su penultimo digito a la potencia representada
# por su ultimo digito
print("\n5. Construir un programa que reciba un numero entero y muestre el resultado de elevar su penultimo digito a la potencia representada por su ultimo digito")

num = int(input("\nIngresa el numero: "))

last_digito = num % 10
penul_digitos = (num // 10) % 10

potencia = penul_digitos ** last_digito

print(f"\nElevar {penul_digitos} a la potencia de {last_digito} es {potencia}")



# 6. Construir un programa que reciba un numero entero y muestre el residuo de dividirlo entre 6 y 8
print("\n6. Construir un programa que reciba un numero entero y muestre el residuo de dividirlo entre 6 y 8")

num = int(input("\nIngresa el numero: "))

div1 = num % 6
div2 = num % 8

print(f"\nEl residuo de {num} dividido con 6 es {div1} y con 8 es {div2}")



# 7. Construir un programa que reciba dos numeros enteros y muestre el resultado de sumar el ultimo digito de cada numero.
print("\n7. Construir un programa que reciba dos numeros enteros y muestre el resultado de sumar el ultimo digito de cada numero.")

num1 = int(input("\nIngresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

last_digNum1 = num1 % 10
last_digNum2 = num2 % 10

suma_digitos = last_digNum1 + last_digNum2

print(f"\nLa suma de los ultimos digitos de {num1} y {num2} es: {suma_digitos}")



# 8. Construir un programa que reciba dos numeros y muestre la suma de sus ultimos tres digitos.
print("\n8. Construir un programa que reciba dos numeros y muestre la suma de sus ultimos tres digitos.")

num1 = int(input("\nIngresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

num1_digito1 = (num1 // 1) % 10
num1_digito2 = (num1 // 10) % 10
num1_digito3 = (num1 // 100) % 10

num2_digito1 = (num2 // 1) % 10
num2_digito2 = (num2 // 10) % 10
num2_digito3 = (num2 // 100) % 10

suma_digitos = num1_digito1 + num1_digito2 + num1_digito3 + num2_digito1 + num2_digito2 + num2_digito3

print(f"\nLa suma de los tres ultimos digitos de {num1} y {num2} es {suma_digitos}")



# 9. Construir un programa que reciba dos cadenas y determine si las dos cadenas son exactamente iguales
print("\n9. Construir un programa que reciba dos cadenas y determine si las dos cadenas son exactamente iguales")

cadena1 = str(input("\nIngresa la primer cadena: "))
cadena2 = str(input("Ingresa la segunda cadena: "))

if cadena1 == cadena2:
    print("\nLas cadenas son iguales.")
else:
    print("\nLas cadenas no son iguales.")
    
    

# 10. Construir un programa que reciba dos numeros complejos y muestre la suma de dichos numeros
print("\n10. Construir un programa que reciba dos numeros complejos y muestre la suma de dichos numeros")

num1 = complex(input("\nIngresa el primer numero complejo (9+5j): "))
num2 = complex(input("Ingresa el segundo numero complejo (10+2j): "))

suma_complex = num1 + num2

print(f"\nLa suma de {num1} y {num2} es {suma_complex.real} + {suma_complex.imag}j")