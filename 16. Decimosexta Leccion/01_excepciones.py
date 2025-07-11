# Manejo de Errores

num1 = 5
num2 = 1
num2 = '1'

try:
    print(num1 + num2)
    print('No se encontro un error')
except: # Debe ir siempre con el try
    print('Se ha producido un error')

    
try:
    print(num1 + num2)
    print('No se encontro un error')
except:
    print('Se ha producido un error')
else: # es opcional
    print('La ejecucion continua correctamente')
    
    
try:
    print(num1 + num2)
    print('No se encontro un error')
except:
    print('Se ha producido un error')
else:
    print('La ejecucion continua correctamente')
finally:
    print('La ejecucion continua')
    
    
# Excepciones por tipo
    
try:
    print(num1 + num2)
    print('No se encontro un error')
except ValueError as ve:
    print(f'Se ha producido un ValueError: {ve}')
except TypeError as te:
    print(f'Se ha producido un TypeError: {te}')
except Exception as error:
    print(error)