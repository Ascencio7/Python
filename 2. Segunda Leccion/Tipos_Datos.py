# Ejemplo de ingreso de datos.

# Programa para verificacion de tipos de datos
valor_Entero = int(input("\nIngresa un valor entero sin punto decimal: "))
valor_EnteroLargo = int(input("\nIngresa un valor entero largo sin punto decimal: "))
valor_Decimal = float(input("\nIngresa un numero con punto decimal: "))
valor_Complejo = complex(input("\nIngrese un valor complejo (a + bj): ")) # siempre debe ir nj, sin la 'j' no funciona y termina
valor_Cadena = str(input("\nIngresa una cadena de texto: "))
valor_Bool = bool(input("\nIngresa un valor booleano (True/False): ").lower()) # upper() o lower() manejan las mayusculas y misculas


print("\nSe muestran los valores ingresados y su tipo de dato según Python:")
print("\n")
print(valor_Entero, type(valor_Entero)) # type() verifica que tipo de valor es para Python
print(valor_EnteroLargo, type(valor_EnteroLargo))
print(valor_Decimal, type(valor_Decimal))
print(valor_Complejo, type(valor_Complejo))
print(valor_Cadena, type(valor_Cadena))
print(valor_Bool, type(valor_Bool))