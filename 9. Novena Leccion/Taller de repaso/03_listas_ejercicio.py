"""
    Se pide crear un programa en el que pueda registrar nombres, edad y salario para n empleados,
    al final debera imprimir el nombre del empleado que mas gana.
"""

# Declarar las listas
list_nombres = []
list_edades = []
list_salarios = []


num_empleados = int(input("\nIngresa el numero de empleados a registrar: "))

for i in range(num_empleados):
    print(f"\nIngreso de datos del empleado N°{i+1}")
    list_nombres.append(input("\nIngrese el nombre: ")) # solicitar los datos al usuario
    edades = int(input("Ingrese la edad: "))
    list_edades.append(edades)
    salario = float(input("Ingrese el salario: $")) # se convierte a float el dato
    list_salarios.append(salario) # y se agrega a la lista
    print("\n") # un salto de linea opcional
    

for x in range(num_empleados):
    print(f"Datos del empleado N°{x + 1}:")
    print(f"Nombre: {list_nombres[x]}")
    print(f"Edad: {list_edades[x]}")
    print(f"Salario: ${list_salarios[x]}\n")
    
    
# Obtener al empleado que mas gana
salario_alto = max(list_salarios) # encuentra el salario mas alto de la lista
indice_salario_alto = list_salarios.index(salario_alto) # obtiene el indice del salario alto
nombre_salario_alto = list_nombres[indice_salario_alto] # y obtiene el nombre del empleado del salario alto

# Obtener al empleado que menos gana
salario_bajo = min(list_salarios)
indice_salario_bajo = list_salarios.index(salario_bajo)
nombre_salario_bajo = list_nombres[indice_salario_bajo]

# Mostrar los resultados
print(f"\nEl empleado que mas gana es {nombre_salario_alto} con ${salario_alto}\n")
print(f"\nEl empleado que menos gana es {nombre_salario_bajo} con ${salario_bajo}\n")
print("\nFin del programa...\n")