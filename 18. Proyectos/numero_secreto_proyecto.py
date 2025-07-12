# ✅ Juego del número secreto

# Importar el modulo para generar numeros aleatorios
import random

# Se crea una funcion unica para el juego
def juego_numero():
    # Se genera un numero secreto aleatorio entre 1 al 100
    num_secreto = random.randint(1, 100)
    # Se crea una variable contadora para capturar los intentos del usuario
    intentos = 0
    # Se crea una variable booleana para saber si se adivino el numero
    adivinado = False
    
    # Mensajes de bienvenida
    print('\n========== Bienvenido al juego del Numero Secreto ==========\n')
    print('He elegido un numero entre 1 y 100. Intenta adivinarlo.')
    
    # Si no se ha adivinado el numero, se itera en un bucle while
    while not adivinado:
        try:
            # Se solicita el numero y se convierte en entero
            intento = int(input('\nIntroduce tu intento: '))
            intentos += 1 # Se incrementa el contador con 1
        
            # Se verifica si el numero ingresado es menor al numero secreto
            if intento < num_secreto:
                print('\nNumero demasiado bajo...')
            
            # Se verifica si el numero ingresado es mayor al numero secreto
            elif intento > num_secreto:
                print('\nNumero demasiado alto...')
            else:
                # Si el usuario adivina el numero se muestran los siguientes mensajes
                print('\n========== Correct adivinaste el numero secreto ==========\n')
                print(f'Adivinaste el numero en {intentos} intentos.\n') # Se muestran los intentos que hizo hasta adivinar el numero
                print('Fin del juego.\n')
                adivinado = True # Se sale del bucle al adivinar el numero
        except ValueError:
            # Un mensaje de error si se ingresa un dato que no sea un numero entero
            print('\nIngresa un numero valido.')
            continue # Retorna al inicio del bucle de nuevo

# Se llama a la funcion para ser ejecutado
juego_numero()