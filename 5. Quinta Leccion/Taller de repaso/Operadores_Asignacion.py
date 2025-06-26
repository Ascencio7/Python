# Crear un programa que verifique la comparacion de dos numeros ingresados

# declarar las variables a usar
num1 = float(input("\nIngresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

print(f"\nLos numeros a comparar son {num1} y {num2}")

print("\nLos resultados son")

# Usar condicionales para el manejo de las operaciones
if num1 == num2:
    print("\nLos numeros son iguales.")
if num1 != num2:
    print(f"\nEs diferente")
if num1 > num2:
    print(f"\nEl primer numero es mayor que el segundo.")
if num1 < num2:
    print(f"\nEl primer numero es menor que el segundo.")
if num1 >= num2:
    print(f"\nEl primer numero es mayor o igual que el segundo.")
if num1 <= num2:
    print(f"\nEl primer numero es menor o igual que el segundo.")

print("\nFin del programa.")