# Ejercicio

""" 
    Si una empresa de comestibles tiene su tope de ventas promedio en 1000 articulos para el I trimestre de 2025,
    leer la informacion de articulos vendidos correspondiente a un vendedor, calcular su promedio y determinar si 
    alcanzo el promedio de ventas de la empresa.
"""

# titulo del programa
print("\nArticulos del I Trismestre de Almacenes S.A. de C.V.")

# Variables a usar y leer sus datos
codigo_Vendedor = str(input("\nIngresa el codigo del vendedor: "))
nombre_Vendedor = str(input("Ingresa el nombre del vendedor: "))
ventas_Enero = int(input("\nIngresa las ventas realizadas en Enero: "))
ventas_Febrero = int(input("Ingresa las ventas realizadas en Febrero: "))
ventas_Marzo = int(input("Ingresa las ventas realizas en Marzo: "))

promedio_Ventas = (ventas_Enero + ventas_Febrero + ventas_Marzo) / 3

# Redondear y mostrar 2 decimales
promedio_Ventas = round(promedio_Ventas, 2)

if promedio_Ventas >= 1000:
    print("\n\t\tReporte de Ventas:")
    print(f"\n\t\tCodigo del vendedor: {codigo_Vendedor}")
    print(f"\t\tNombre del Vendedor: {nombre_Vendedor}")
    print(f"\t\tVentas de Enero: {ventas_Enero}")
    print(f"\t\tVentas de Febrero: {ventas_Febrero}")
    print(f"\t\tVentas de Marzo: {ventas_Marzo}")
    print(f"\nEl vendedor {nombre_Vendedor} con codigo {codigo_Vendedor} realizo 1000 ventas en el I Trismestre de 2025.")
    print("\nFin del programa.")
else:
    print("\n\t\tReporte de Ventas:")
    print(f"\n\t\tCodigo del vendedor: {codigo_Vendedor}")
    print(f"\t\tNombre del Vendedor: {nombre_Vendedor}")
    print(f"\t\tVentas de Enero: {ventas_Enero}")
    print(f"\t\tVentas de Febrero: {ventas_Febrero}")
    print(f"\t\tVentas de Marzo: {ventas_Marzo}")
    print(f"\nEl vendedor {nombre_Vendedor} con codigo {codigo_Vendedor} no realizo 1000 ventas en el I Trismestre de 2025.")
    print("\nFin del programa.")