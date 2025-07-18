# Se define la clase

class Libro():
    # Se define unos campos ya con valores determinados
    Tamano = "17x24"
    Peso = "200 gms"
    Paginas = 150
    Registrado = False
    Coleccion = "No definida"
    Precio = 49.50
    
    # Se define una funcion para registrar el libro
    def registrar(self):
        self.Registrado = True # El libro fue registrado
        return 'Registrado' # Retorna un mensaje de confirmacion
    
    # Se define una funcion para inscribir el libro
    def inscribir(self):
        # Se incluye el nombre de la coleccion del libro
        self.Coleccion = 'Programacion Orientada a Objetos'
        return self.Coleccion # Y retorna el nombre de la coleccion definida
    
# Se crea una instancia de la clase para poder acceder a los atributos y metodos ** funciones creadas **
print(type(Libro()))
libro_python = Libro()

# Se impre la informacion del libro
print(f'\nTamano: {libro_python.Tamano}')
print(f'Peso: {libro_python.Peso}')
print(f'Paginas: {libro_python.Paginas}')
print(f'Registrado: {libro_python.registrar()}')
print(f'Coleccion: {libro_python.inscribir()}')
print(f'Precio: ${libro_python.Precio}\n')