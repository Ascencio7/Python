# Bucle while

i = 1

while i <= 18:
    print(i)
    i = i + 1
print("\nFin")


i = 3

while i <= 15:
    print(i)
    i = i + 3
print("\nFin")


i = 1

while i <= 5:
    print(i)
    i = i + 1
print("\nFin")


i = 1

while i != 6:
    print("Vladimir")
    i = i + 1
print("\nFin")


i = 1

while i <= 6:
    if i == 3:
        i = i + 1
        continue
    else:
        i = i + 1
        print("Vladimir")
print("\nFin")

i = 1

while i <= 6:
    if i == 3:
        break;
    else:
        i = i + 1
        print("Vladimir")
print("\nFin")


i = 1

while i <= 6:
    print("i = ", i)
    i = i + 1
else:
    print("\nFin")
    
    
# Importar el modulo math para sacar la raiz cuadrada
import math

i = 10

while i <= 50:
    print("Raiz cuadrada de ", i, " = ", (round(math.sqrt(i),2))) # roun para redondear el resultado
    i = i + 10 # va de 10 en 10 hasta 50
print("\nFin")


cont = 0

frase = str(input("\nIngresa una frase: "))

for i in frase:
    if i == ' ':
        cont = cont + 1

print(f"\nLa frase tiene {cont} espacios en blanco.")