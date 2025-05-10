# Ejercicios practicos

# 1. Construir un programa que lea un numero entero y determine si es un numero positivo de 4 digitos.
print("\n1. Construir un programa que lea un numero entero y determine si es un numero positivo de 4 digitos.")

# Declarar la variable y pedir el numero
num = int(input("\nIngresa el numero entero de 4 digitos: "))

if num >= 1000 and num <= 9999:
    print(f"\nEl numero {num} es de 4 digitos.")
    print("\nFin del programa")
else:
    print(f"\nEl numero {num} no es de 4 digitos.")
    print("\nFin del programa")
    
    

# 2. Construir un programa que lea un numero entero y determine si es un numero par o impar.
print("\n2. Construir un programa que lea un numero entero y determine si es un numero par o impar.")

# Declarar la variable y pedir su numero
num = int(input("\nIngresa el numero entero para verificar si es par o impar: "))

if num % 2 == 0:
    print(f"\nEl numero {num} es un numero par.")
    print("\nFin del programa.")
else: 
    print(f"\nEl numero {num} es un numero impar.")
    print("\nFin del programa.")
    


# 4. Construir un programa que lea un numero entero y determinar si su ultimo digito es un digito par.
print("\n4. Construir un programa que lea un numero entero y determinar si su ultimo digito es un digito par.")

# Declarar la variable y pedir su numero
num = int(input("\nIngresa el numero para ver si su ultimo digito es par o impar: "))

lastDigito = (num // 1) % 10

if lastDigito % 2 == 0:
    print(f"\nEl ultimo digito de {num} si es un numero par.")
    print("\nFin del programa.")
else:
    print(f"\nEl ultimo digito de {num} si es un numero impar.")
    print("\nFin del programa.")



# 6. Construir un programa que lea un numero entero y determine si sus dos ultimos digitos son iguales.
print("\n6. Construir un programa que lea un numero entero y determine si sus dos ultimos digitos son iguales.")

# # Declarar la variable y pedir el numero
num = int(input("\nIngresa el numero entero: "))

primerDigito = (num // 1) % 10 # Para el primer digito
segundoDigito = (num // 10) % 10 # Para el segundo digito
# tercerDigito = (num // 100) % 100 # Para el tercer digito

if primerDigito == segundoDigito:
    print(f"\nLos ultimos dos digitos de {num} son iguales.")
    print("\nFin del programa.")
else:
    print(f"\nLos ultimos dos digitos de {num} no son iguales.")
    print("\nFin del programa.")



# 7. Construir un programa que lea un numero entero y determine si la suma de sus dos ultimos digitos es igual a 7.
print("\n7. Construir un programa que lea un numero entero y determine si la suma de sus dos ultimos digitos es igual a 7.")

# Declarar la variable y pedir el numero
num = int(input("\nIngresa el numero entero: "))

primerDigito = (num // 1) % 10 # Para el primer digito
segundoDigito = (num // 10) % 10 # Para el segundo digito

sumaDigitos = primerDigito + segundoDigito

if sumaDigitos == 7:
    print(f"\nLa suma de los dos ultimos digitos de {num} es igual a 7.")
    print("\nFin del programa.")
else:
    print(f"\nLa suma de los dos ultimos digitos de {num} NO es igual a 7.")
    print("\nFin del programa.")



# 8. Construir un programa que lea un numero entero y determine si el resultado de sumar sus dos ultimos digitos es un numero de 1 digito. GPT
print("\n8. Construir un programa que lea un numero entero y determine si el resultado de sumar sus dos ultimos digitos es un numero de 1 digito.")

# Declarar la variable y pedir el numero
num = int(input("\nIngresa el numero entero: "))

primerDigito = abs(num) % 10 # Para el primer digito: OTRA FORMA DE HACERLO
segundoDigito = (abs(num) // 10) % 10 # Para el segundo digito: OTRA FORMA DE HACERLO

sumaDigitos = primerDigito + segundoDigito

if sumaDigitos < 10:
    print(f"\nLa suma de los dos ultimos digitos de {num} es igual a 1.")
    print("\nFin del programa.")
else:
    print(f"\nLa suma de los dos ultimos digitos de {num} NO es igual a 1.")
    print("\nFin del programa.")



# 9. Construir un programa que lea dos numeros enteros y determine si el 1° numero leido es mayor que el 2° numero leido.
print("\n9. Construir un programa que lea dos numeros enteros y determine si el 1° numero leido es mayor que el 2° numero leido.")

# Declarar la variable y pedir los dos numeros
num1 = int(input("\nIngresa el primer numero entero: "))
num2 = int(input("Ingresa el segundo numero entero: "))

if num1 > num2:
    print(f"\nEl primer numero que es {num1} es mayor que {num2} que es el segundo numero.")
    print("\nFin del programa.")
else:
    print(f"\nEl segundo numero que es {num2} es mayor que {num1} que es el primer numero.")
    print("\nFin del programa.")



# 10. Construir un programa que lea dos numeros enteros y determine si el ultimo digito del 1° numero leido es par, y al mismo tiempo
# si el penultimo digito del 2° numero es impar. GPT
print("\n10. Construir un programa que lea dos numeros enteros y determine si el ultimo digito del 1° numero leido es par, y al mismo tiempo si el penultimo digito del 2° numero es impar.")

# Declarar las variables y pedir los numeros
num1 = int(input("\nIngresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

ultimoDigito = abs(num1) % 10
penulDigito = (abs(num2) // 10) % 10

if (ultimoDigito % 2 == 0) and (penulDigito % 2 != 0):
    print(f"\nEl ultimo digito del primer numero {num1} es un numero par.")
    print(f"El penultimo digito del segundo numero {num2} es un numero impar.")
    print("\nSe cumplen ambas condiciones.")
    print("\nFin del programa.")
else:
    if ultimoDigito % 2 != 0:
        print(f"\nEl ultimo digito del primer numero {num1} No es un numero par.")
    else:
        print(f"\nEl ultimo digito del primer numero {num1} es un numero par.")
        
    if penulDigito % 2 == 0:
        print(f"\nEl penultimo digito del segundo numero {num2} NO es un numero impar.")
    else:
        print(f"El penultimo digito del segundo numero {num2} es un numero par.")
    print("\nNo se cumplen ambas condiciones.")
    print("\nFin del programa.")