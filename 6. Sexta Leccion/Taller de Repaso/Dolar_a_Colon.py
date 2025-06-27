# Crear un programa que imprima la cantidad en colones equivalente a un monto ingresado en dolares

# Declarar una constante para guardar el valor del colon
colon = 8.75

# pedir los datos
dolar = float(input("\nIngresa los dolares a convertir en colon: "))

# Realizar la conversion y redondearlo a 2 decimales
conver = dolar * colon
conver = round(conver, 2)

# Mostrar el resultado
print(f"El monto de ${dolar} a colon es {conver} colones.")
print("\nFin del programa.\n")