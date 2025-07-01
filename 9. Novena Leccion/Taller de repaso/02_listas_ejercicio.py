"""
    Se pide crear un programa en el que pueda registrar nombres, edad y salario para 5 empleados,
    al final debera imprimir el nombre del empleado que mas gana.
"""

# Declarar las listas
list_nombres = list()
list_edades = list()
list_salarios = list()


# Como son 5 registros, se itera en 5 para pedir los datos
for i in range(5):
    print(f"\nIngreso de datos del empleado N°{i+1}")
    list_nombres.append(input("\nIngrese el nombre: ")) # solicitar los datos al usuario
    list_edades.append(input("Ingrese la edad: "))
    salario = float(input("Ingrese el salario: $")) # se convierte a float el dato
    list_salarios.append(salario) # y se agrega a la lista
    print("\n") # un salto de linea opcional
    

# Mostrar los resultados en otro for con 5 iteraciones y concatenar los resultados
for x in range(5):
    print(f"Datos del empleado N°{x + 1}:")
    print(f"Nombre: {list_nombres[x]}")
    print(f"Edad: {list_edades[x]}")
    print(f"Salario: ${list_salarios[x]}\n")

# Mostrar al empleado que mas gana
salario_alto = max(list_salarios) # encuentra el salario mas alto de la lista
indice_salario_alto = list_salarios.index(salario_alto) # obtiene el indice del salario alto
nombre_salario_alto = list_nombres[indice_salario_alto] # y obtiene el nombre del empleado del salario alto

print(f"\nEl empleado que mas gana es {nombre_salario_alto} con ${salario_alto}\n")
print("\nFin del programa...\n")