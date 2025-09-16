# Ejercicio 10: Normalizar palabras

def normalizar_palabras(frase: str) -> list:
    # Pasar todo a minúsculas
    frase = frase.lower()

    # Lista de signos de puntuación a eliminar
    signos = ".,;:!?¡¿\"'()[]{}"

    # Reemplazar cada signo por nada
    for s in signos:
        frase = frase.replace(s, "")

    # Separar la frase en palabras
    palabras = frase.split()

    return palabras

# Solicitar al usuario que ingrese una frase
entrada = input("Ingrese una frase o palabra: ")
resultado = normalizar_palabras(entrada)

# Mostrar la lista normalizada
print("Lista normalizada:", resultado)