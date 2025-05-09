# 1. Construir un programa que reciba dos numeros enteros y calcule el resultado de elevar el 1° numero leido a la potencia representada
# por el 2° numero leido.

num1 = int(input("\nIngrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

potencia = num1 ** num2

print(f"El numero {num1} elevado a la potencia de {num2} es: {potencia}")

# 2. Construir un programa que reciba un numero entero y obtenga su mitad entera.

num = int(input("\nIngresa un numero entero: "))

mitad = num // 2

print(f"\nLa mitad entera de {num} es: {mitad}")