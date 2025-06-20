# 1. Construir una funcion que permita iniciar sesion validando usaurio y contrasena
import getpass # para ocultar la contrasena

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

usuario = input("\nUsuario: ")
password = getpass.getpass("Contrasena: ")

# Llamar a la funcion
login(usuario, password)