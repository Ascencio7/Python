"""
    Crear un programa en Python que pida la siguiente informacion:
    
        Nombre, Apellido, Edad, Salario Mensual
    
    Al final el programa debe imprimir el nombre completo de la persona y la cantidad de sueldo liquido a recibir
    si se sabe que existen los siguientes descuentos de ley:
    
        Renta --> 10% del salario
        AFP --> 6.25% del salario
        Cuota de prestamo --> $25.00

"""

# Declarar las constantes a usar
RENTA = 0.10
AFP = 0.0625
CUOTA = 25

# Pedir los datos
nombre = input("\nIngrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = int(input("Ingrese la edad: "))
salario_mensual = float(input("Ingrese el salario: $"))

# Realizar los calculos
desRenta = round(salario_mensual * RENTA, 2) # calcular la renta y redondear a 2 decimales
desAFP =  round(salario_mensual * AFP, 2) # calcular la afp y redondear a 2 decimales
prest = CUOTA # solo asignar el valor de la constante a la variable

# Luego se calcula el sueldo liquido a recibir con la resta del salario inicial con los descuentos y el prestamo y redondearlo a 2 decimales
sueldoLiquido = round(salario_mensual - desRenta - desAFP - prest, 2)

# Mostrar los resultado
print(f"\nResumen del Salario del empleado")
print(f"\nSueldo a recibir final: ${sueldoLiquido}")
print("Fin del programa.\n")