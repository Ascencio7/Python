""" 
    Se desea convertir una distancia dada en kilómetros a millas.
"""
# funcion para calcular las millas
def kmAMillas(kilometros):
    millas = kilometros * 0.621371 # este valor es de una milla por km
    return millas # se retorna el resultado

# se pide el dato
kilometros = float(input("\nIngresa la distancia en KM: "))

millas = kmAMillas(kilometros) # se llama la funcion
millas = round(millas, 5) # se redondea el resultado

print(f"\nLa distancia de {kilometros} km a Millas es {millas}") # se muestra el resultado
print("Fin del programa.")