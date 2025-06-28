"""
    Se tiene un automóvil que consume una cierta cantidad de gasolina por cada 100 kilómetros recorridos. 
    
    Ejemplo de entrada/salida:

    Si el usuario ingresa:

    Distancia: 250 km
    Consumo: 8 litros/100 km
    El programa debería mostrar:

    Para un viaje de 250 km, se necesitarán 20 litros de gasolina.
    
"""

def gasto_gasolina(distancia, consumo):
    gasto = (distancia / 100) * consumo # formula general
    return gasto # retorna el gasto calculado

# se piden los datos
distancia = float(input("\nIngresa la distancia del viaje en km: "))
consumo = float(input("Ingresa el consumo de gasolina en litros: "))

gasto = gasto_gasolina(distancia, consumo) # se llama a la funcion y se pasan los argumentos
gasto = round(gasto, 2) # se redondea a 2 decimales

print(f"\nPara viajes de {distancia} km, se requieren {gasto} litros de gasolina.") # imprimir el resultado final
print("\nFin del programa.")