# 1. Del conjunto de datos [20, 21, 30, 41, 50, 51, 201] mostrar en pantalla los que no terminen en 1.

print("\n1. Del conjunto de datos [20, 21, 30, 41, 50, 51, 201] mostrar en pantalla los que no terminen en 1.")

print("\n")

for i in [10, 11, 20, 21, 30, 31, 40, 41, 50, 51, 60, 61, 70, 71, 80, 81, 90, 91, 100, 101, 200, 201]:
    if i % 10 != 1:
        print(i)
print("\nFin")

print("\n")

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