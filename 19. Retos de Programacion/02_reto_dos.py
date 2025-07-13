"""
    * Escribe una función que reciba dos palabras (String) y retorne
    * verdadero o falso (Bool) según sean o no anagramas.
    * - Un Anagrama consiste en formar una palabra reordenando TODAS
    *   las letras de otra palabra inicial.
    * - NO hace falta comprobar que ambas palabras existan.
    * - Dos palabras exactamente iguales no son anagrama.

"""

# Se crea una funcion que recibe dos palabras
def anagrama(palabra_una, palabra_dos):
    # Se verifica que tanto la palabra uno y dos sean iguales al convertirlas en minusculas
    if palabra_una.lower() == palabra_dos.lower():
        return False # Retorna falso ya que las dos palabras idénticas no se consideran anagramas
    
    # Se compara las letras de ambas palabras ordenadas alfabéticamente.
    # Si las listas de letras ordenadas coinciden, son anagramas y retorna TRUE.
    return sorted(palabra_una.lower()) == sorted(palabra_dos.lower())


# Se hacen pruebas haciendo 'print()', llamando la funcion y pasandole valores de tipo string
print(anagrama('amor', 'roma')) # Si es anagrama
print(anagrama('love', 'elvo')) # Si es anagrama
print(anagrama('vladi', 'lavid')) # Si es anagrama
print(anagrama('vladi', 'Vladi')) # No es anagrama
print(anagrama('Jonathan', 'Jonathan')) # No es anagrama
print(anagrama('Juan', 'Leon')) # No es anagrama