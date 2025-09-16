# Ejercicio 16
# Construir un diccionario {palabra: longitud} a partir de una frase ingresada por el usuario.

def normalizar_palabras(frase: str) -> list: #Convierte la frase a minúsculas, elimina signos de puntuación y retorna una lista de palabras.
    frase = frase.lower()
    signos = ".,;:!?¡¿\"'()[]{}"
    for s in signos:
        frase = frase.replace(s, "")
    palabras = frase.split()
    return palabras

# Entrada del usuario
frase = input("Ingrese una frase: ")

# Normalizamos las palabras
palabras = normalizar_palabras(frase)

# Construimos el diccionario {palabra: longitud}
diccionario_longitudes = {palabra: len(palabra) for palabra in palabras}

# Mostramos el resultado
print("\nDiccionario de palabras y su longitud:")
for palabra, longitud in diccionario_longitudes.items():
    print(f"{palabra}: {longitud}")
