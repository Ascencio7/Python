# Funciones
# puede no solo recibir o desencadenar codigo, puede devolver codigo y recibir codigo

# Funcion simple
def mi_funcion():
    print('Esto es una funcion')
    
# se llama la funcion
mi_funcion()

# funcion que recibe parametros
def sumar_dos_valores(a,b):
    print(a + b)

# se llama la funcion   
sumar_dos_valores(44.45, 89.36)

sumar_dos_valores('44.45', '89.36')


# funcion que retorna los parametros
def sumar_dos_valores_con_retorno(a,b):
    return a + b


mi_resultado = sumar_dos_valores_con_retorno(10,50)

print(mi_resultado)

def imprimir_nombre(nombre, apellido):
    print(f'Mi nombre es {nombre} {apellido}')
    
imprimir_nombre('Vladimir', 'Ascencio')

# se puede cambiar el orden, pero NO SE PUEDEN BORRAR U OMITIR
imprimir_nombre(apellido='Vladimir', nombre='Ascencio')


# Parametros con valores por defecto
def imprimir_nombre_por_defecto(nombre, apellido, alias = "Sin alias."):
    print(f'Mi nombre es {nombre} {apellido}. Y mi alias es {alias}')
    

imprimir_nombre_por_defecto('Vladimir', 'Ascencio', 'VladiDev')
imprimir_nombre_por_defecto('Vladimir', 'Ascencio')        

# Con el '*' se pueden pasar infinitos datos
def imprimir_textos(*texts):
    for text in texts:
        print(text)
    
imprimir_textos('Hola', 'Vladimir', 'Ascencio')