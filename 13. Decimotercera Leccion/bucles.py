# Los bucles en Python

# while
# se le pasa una condicion al bucle while
# se repite varias en funcion de una condicion

mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 1 # aca se puede cambiar la condicion para terminar el bucle
else: # se pueden usar los 'else' con los while, ya que es literal un if infinito, y este else es opcional
    print('\nEl valor es mayor o igual que 10.\n')
    
print('El programa sigue ejecutandose.\n')


while mi_condicion < 20:
    mi_condicion += 2
    if mi_condicion == 15:
        print('Mi condicion es 15.')
        break
    print(mi_condicion)

    
print('\nEl programa sigue ejecutandose.\n')


# FOR: se repetira tantas veces como cuantos elementos se tenga iterables
# y cada vez que le de vuelta al for, accedera a uno de sus elementos del listado

lista_edades = [21, 45, 65, 30, 30, 17, 20, 19]

for element in lista_edades:
    print(element)
    

mi_tupla = (21, 1.69, "Vladimir", "Ascencio")

for element in mi_tupla:
    print(element)


mi_set = {
    "Vladimir",
    "Ascencio",
    21
}

for element in mi_set:
    print(element)

mi_dic = {
    "Nombre": "Vladimir",
    "Apellido": "Ascencio",
    "Edad": 21,
    1:"Python"
}

# Con values() se muestran los valores del diccionario, sin usar values() solo mostrara las claves
for element in mi_dic.values():
    print(element)
    
    
for element in mi_dic.values():
    print(element)
    if element == "Edad":
        continue # no se aconseja, pues vuelve al bucle y no ejecuta lo que esta despues
    print('Se ejecuta')
else:
    print('El bucle for para diccionario ha finalizado.\n')