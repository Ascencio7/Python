# 1. Hacer la tabla de multiplicar con el numero deseado por el usuario con for
num = int(input("\nIngresa el numero de la tabla de multiplicar que desea visualizar: "))
print("\n")

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

print("\nFin.")


# 2. Hacer la tabla de multiplicar con el numero deseado por el usuario con while
num = int(input("\nIngresa el numero de la tabla de multiplicar que desea visualizar: "))
print("\n")

i = 1
while i <= 10:
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
    i += 1
print("\nFin.")