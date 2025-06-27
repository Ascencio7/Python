"""
    Un alumno ha realizado 3 evaluaciones parciales. Él desea saber cuál es su promedio final del módulo DLP, si se sabe que las dos primeras
    evaluaciones valen 30% y la tercera 40%.
"""

# afuera para que no ingrese el nombre de nuevo si se equivoca
nombre = input("\nIngrese el nombre del estudiante: ")


while(True):
    # Pedir los datos
    evaUno = float(input("\nIngresa la primer nota: "))
    evaDos = float(input("Ingresa la segunda nota: "))
    evaTres = float(input("Ingresa la tercera nota: "))
    
    # Verificar que 10 no lleve decimales
    if evaUno and evaDos and evaTres == 10 and ".":
            print("\nNota invalida. El 10 no debe llevar decimales.")
            continue # si es asi, que vuelva a ingresar los datos
    
    # Si las notas estan entre el rango de 0 y 10 se hace la operacion de sacar el promedio
    if all(0 <= nota <=10 for nota in [evaUno, evaDos, evaTres]): # otra forma de if para evitar usar 'and' varias veces
         
        promedio = (evaUno * 0.30) + (evaDos * 0.30) + (evaTres * 0.40) # no dividir entre la cantidad sino se baja el promedio y reprueba
        promedio = round(promedio, 2) # redondear el promedio a 2 decimales

        # imprimir los resultados
        print("\nResultados:")
        print(f"\nEstudiante: {nombre}")
        print(f"Primera Evaluacion: {evaUno}")
        print(f"Segunda Evaluacion: {evaDos}")
        print(f"Tercera Evaluacion: {evaTres}")
        print(f"Promedio Final: {promedio}")
    
        # Verificar si el estudiante aprobo o reprobo el modulo
        if promedio >= 7:
            print(f"\n{nombre} ha aprobado el modulo DLP")
            break # se rompe el bucle
        else:
            print(f"\n{nombre} ha reprobado el modulo DLP")
            break # se rompe el bucle
    else:
        print("\nHa ingresado valores fuera del rango. Deben ser entre 0 y 10 y con decimales.") # si los valores fueron fuera de rango mostrar mensaje
        continue # vuelve a pedir las notas otra vez


print("\nFin del programa.\n")