# Tipos de variables en Python

# Variables con datos tipo texto
nombre = "Jonathan Vladimir"
apellido = "Ascencio Ramos"

# Variables con datos tipo entero
edad = 21
costo = 199

# Variables con datos tipo decimal
salario = 402.75
descuento = 78.39

# Variables con datos booleanos
variableFalse = False
variableTrue = True

# Variables declaradas en una sola linea
name, lastname, alias, edad = "Vladimir", "Ascencio", "VladiDev", 21
# Es mejor evitar crear las variables con este estilo para evitar errores futuros
# y esta practica hace que el mantenimiento del codigo sea muy dificil

# Imprimir los datos
print("\nVariables de tipo String")
print("\nMi nombre es", nombre, apellido)

print("\nVariables de tipo Int")
print("\nEdad:", edad, ", Costo:", costo)

print("\nVariables de tipo Float (decimal)")
print("\nSalario:", salario, ", Descuento:", descuento)

print("\nVariables de tipo Booleano (true, false)")
print("\nFalso:", variableFalse, ", Verdad:", variableTrue)

print("\nVariables declaradas en una sola linea")
print(f"\nMi nombre es {name} {lastname}. Tengo {edad} años, y mi alias es {alias}")