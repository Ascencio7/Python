"""
    Python es un lenguaje de tipado debil, es decir, las variables declaradas de un tipo anteriormente, se pueden cambiar de tipo
    despues y el programa no va a dar error.
"""

# Se puede forzar el tipo?
address: str = "Mi direccion"
print(address)
print(type(address))

address = 1945
print(address)
print(type(address))

address = True
print(address)
print(type(address))

address = 1945.45
print(address)
print(type(address))