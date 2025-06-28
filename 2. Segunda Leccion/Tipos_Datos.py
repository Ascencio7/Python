# Ejemplo de ingreso de datos.

# Programa para verificacion de tipos de datos
valor_entero = int(input("\nIngresa un valor entero sin punto decimal: "))
valor_enteroLargo = int(input("\nIngresa un valor entero largo sin punto decimal: "))
valor_decimal = float(input("\nIngresa un numero con punto decimal: "))
valor_complejo = complex(input("\nIngrese un valor complejo (a + bj): ")) # siempre debe ir nj, sin la 'j' no funciona y termina
valor_cadena = str(input("\nIngresa una cadena de texto: "))
valor_bool = bool(input("\nIngresa un valor booleano (True/False): ").lower()) # upper() o lower() manejan las mayusculas y misculas


print("\nSe muestran los valores ingresados y su tipo de dato según Python:")
print("\n")
print(valor_entero, type(valor_entero)) # type() verifica que tipo de valor es para Python
print(valor_enteroLargo, type(valor_enteroLargo))
print(valor_decimal, type(valor_decimal))
print(valor_complejo, type(valor_complejo))
print(valor_cadena, type(valor_cadena))
print(valor_bool, type(valor_bool))