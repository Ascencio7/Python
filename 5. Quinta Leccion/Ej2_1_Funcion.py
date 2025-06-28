# 1. Construir una funcion que permita iniciar sesion validando usaurio y contrasena
# La contrasena se muestra con asteriscos en la terminal

import sys # Funcion que interactua con el sistema
import msvcrt # Solo para Windows, da funciones para manejar la entrada del teclado

""" 
    Una funcion para obtener la contra del usuario.
    Se mostrara asteriscos en lugar de los caracteres reales para mayor seguridad.
    Y retornara: la contrasena ingresada por el usuario.
"""

def tener_contra():
    print("Contrasena: ", end='', flush=True) # Imprime el mensaje sin saltos de lineas
    password = [] # Una lista para guardar los caracteres de la contra
    while True:
        ch = msvcrt.getch().decode('utf-8') # Lee un caracter de la entrada sin mostrarlo
        if ch == '\r': # Si se presiona ENTER 
            print() # da un salto de linea
            break # y sale del bucle
        elif ch == '\b': # Si presiona BACKSPACE
            if password: # va a verificar que la lista no este vacia
                password.pop() # y elimina el ultimo caracter de la lista
                print('\b \b', end='', flush=True) # y va a borrar el ultimo asterico mostrado
        else:
            password.append(ch) # se agrega el caracter a la lista
            print('*', end='', flush=True) # mostrara un asterisco en la pantall
    return ''.join(password) # y devolvera la contra como una cadena



"""
    Una funcion para verificar el inicio de sesion del usuario.
    Se esperan 2 argumentos: usuario y password.
"""

def login(usuario, password):
    # Iniciar por defecto los datos
    usuario = "Ascencio7"
    password = "wirtaryen17"
    
    # Verificar si el usuario y contra son correctos
    if usuario == "Ascencio7" and password == "wirtaryen17":
        print("\nInicio de sesion exitoso. Bienvenido, Ascencio7")
    else:
        print("\nUsuario o contrasena incorrectos. Intente de nuevo")
        
        
        
# Solicitar los datos
print("\nATLAS CORP | INICIAR SESION")

usuario = input("\nUsuario: ") # pedir el usuario
password = tener_contra() # se llama la funcion para obtener la contra

# Llamar la funcion
login(usuario, password) # se verifica el inicio de sesion