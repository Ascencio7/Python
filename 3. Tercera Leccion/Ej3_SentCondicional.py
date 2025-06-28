# Ejercicio

""" 
    Si una empresa de comestibles tiene su tope de ventas promedio en 1000 articulos para el I trimestre de 2025,
    leer la informacion de articulos vendidos correspondiente a un vendedor, calcular su promedio y determinar si 
    alcanzo el promedio de ventas de la empresa.
"""

# titulo del programa
print("\nArticulos del I Trismestre de Almacenes S.A. de C.V.")

# Variables a usar y leer sus datos
codigo_vendedor = str(input("\nIngresa el codigo del vendedor: "))
nombre_vendedor = str(input("Ingresa el nombre del vendedor: "))
ventas_enero = int(input("\nIngresa las ventas realizadas en Enero: "))
ventas_febrero = int(input("Ingresa las ventas realizadas en Febrero: "))
ventas_marzo = int(input("Ingresa las ventas realizas en Marzo: "))

promedio_ventas = (ventas_enero + ventas_febrero + ventas_marzo) / 3

# Redondear y mostrar 2 decimales
promedio_ventas = round(promedio_ventas, 2)

if promedio_ventas >= 1000:
    print("\n\t\tReporte de Ventas:")
    print(f"\n\t\tCodigo del vendedor: {codigo_vendedor}")
    print(f"\t\tNombre del Vendedor: {nombre_vendedor}")
    print(f"\t\tVentas de Enero: {ventas_enero}")
    print(f"\t\tVentas de Febrero: {ventas_febrero}")
    print(f"\t\tVentas de Marzo: {ventas_marzo}")
    print(f"\nEl vendedor {nombre_vendedor} con codigo {codigo_vendedor} realizo 1000 ventas en el I Trismestre de 2025.")
    print("\nFin del programa.")
else:
    print("\n\t\tReporte de Ventas:")
    print(f"\n\t\tCodigo del vendedor: {codigo_vendedor}")
    print(f"\t\tNombre del Vendedor: {nombre_vendedor}")
    print(f"\t\tVentas de Enero: {ventas_enero}")
    print(f"\t\tVentas de Febrero: {ventas_febrero}")
    print(f"\t\tVentas de Marzo: {ventas_marzo}")
    print(f"\nEl vendedor {nombre_vendedor} con codigo {codigo_vendedor} no realizo 1000 ventas en el I Trismestre de 2025.")
    print("\nFin del programa.")