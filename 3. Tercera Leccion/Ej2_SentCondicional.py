# Programa para determinar si un valor leido es un numero positivo con 3 digitos.

# Nombre del programa
print("\nPrograma que verifica si el numero ingresado es de 3 digitos.")

# Declarar la variable a usar
num = int(input("\nIngresa el numero entero de 3 digitos: "))

if num >= 100 and num <= 999:
    print(f"\nEl numero ingresado {num} es de 3 digitos.")
    print("\nFin del programa.")
else:
    print(f"\nEl numero ingresado {num} no es de 3 digitos.")
    print("\nFin del programa.")