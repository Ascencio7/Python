# 1. Del conjunto de datos [20, 21, 30, 41, 50, 51, 201] mostrar en pantalla los que no terminen en 1.
print("\n1. Del conjunto de datos [20, 21, 30, 41, 50, 51, 201] mostrar en pantalla los que no terminen en 1.")
print("\n")

for i in [10, 11, 20, 21, 30, 31, 40, 41, 50, 51, 60, 61, 70, 71, 80, 81, 90, 91, 100, 101, 200, 201]:
    if i % 10 != 1:
        print(i)
print("\nFin")


# 2. Mostrar 10 veces la palabra "Programacion".
print("\n2. Mostrar 10 veces la palabra Programacion")
print("\n")

for i in range(10):
    print("Programacion")
print("\nFin")


# 3. Del conjunto de letras ["E", "F", "M", "A"] que corresponde a los meses del año, mostrar en pantalla el mes correspondiente de cada mes
print("\n3. Del conjunto de letras [E, F, M, A] que corresponde a los meses del año, mostrar en pantalla el mes correspondiente de cada mes")

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
letras = ["E", "F", "M", "A", "M", "J"]

print("\n")

for i in range(len(meses)):
    print(letras[i], " = ", meses[i])

print("\nFin")


# 4. Del conjunto de letras ["L", "M", "M", "J"] que corresponde a los dias de la semana, mostrar en pantalla el dia correspondiente
print("\n4. Del conjunto de letras [L, M, M, J, V, S, D] que corresponde a los dias de la semana, mostrar en pantalla el dia correspondiente")

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
letras = ["L", "M", "M", "J", "V", "S", "D"]

print("\n")

for i in range(len(dias)):
    print(letras[i], " = ", dias[i])

print("\nFin")


# 5. Del conjunto de datos ["Omar", 54, 2, 2, "Luis", 45, 3, "Juan", 39, 1] mostrar en pantalla los datos organizados en 3 columnas que tengan
# por titulo Nombre, Edad e Hijos

print("\n5. Del conjunto de datos [Omar, 54, 2, 2, Luis, 45, 3, Juan, 39, 1] mostrar en pantalla los datos organizados en 3 columnas que tengan por titulo Nombre, Edad e Hijos")
datos = ["Omar", 54, 2, "Luis", 45, 3, "Juan", 39,1]
print("\n")
print("{:<10} {:<5} {:<5}".format("Nombre", "Edad", "Hijos"))

for i in range(0, len(datos), 3):
    nombre = datos[i]
    edad = datos[i + 1]
    hijos = datos[i + 2]
    print("{:<10} {:<5} {:<5}".format(nombre, edad, hijos))
print("\nFin")


# 6. Leer una cadena de caracteres y mostrarla verticalmente.
print("\n6. Mostrar la cadena de texto verticalmente")
cadena = str(input("\nIngresa una cadena de texto: "))
print("\n")
for letra in cadena:
    print(letra)
print("\nFin")


# 7. Leer una cadena y determinar cuantas veces aparece la letra A.
print("\n7. Leer una cadena y determinar cuantas veces aparece la letra A")
cadena = str(input("\nIngresa una cadena de texto: "))
contador = 0
for letra in cadena:
    if letra == 'A': # mejor como comparador porque si se usa upper o lower cuenta las minusculas tambien
        contador += 1
print(f"La letra 'A' aparece {contador} veces en la cadena.")
print("\nFin")