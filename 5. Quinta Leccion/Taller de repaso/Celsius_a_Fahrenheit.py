""" 
    Se deseas convertir una temperatura dada en grados Celsius a grados Fahrenheit. 
    
        1. Solicita al usuario que ingrese una temperatura en grados Celsius.

        2. Utiliza la fórmula de conversión para calcular la temperatura en grados Fahrenheit:

        3. Muestra el resultado al usuario de manera clara, indicando la temperatura original en Celsius y la temperatura convertida en Fahrenheit. 
"""

# funcion para calcular la temperatura Fahrenheit
def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32 # formula de la conversion
    return fahrenheit # retorna el resultado

# se pide el dato
celsius = float(input("\nIngresa la temperatura en grados Celsius: "))

fahrenheit = celcius_a_fahrenheit(celsius) # se llama la funcion
fahrenheit = round(fahrenheit, 2) # se redondea el resultado

print(f"\nLa temperatura de {celsius}°C a Fahrenheit es: {fahrenheit}°F") # se imprime el resultado
print("\nFin del programa.")