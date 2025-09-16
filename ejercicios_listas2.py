# Ejercicio 12
# Dada una lista de palabras, construir otra con las que tengan más de 5 letras.

def palabras_mayores_a_cinco(palabras: list) -> list:
    return [p for p in palabras if len(p) > 5]

# Programa principal
entrada = input("Ingrese palabras separadas por espacios: ")

# Convertimos la entrada en lista
lista_palabras = entrada.split()

# Aplicamos la función
resultado = palabras_mayores_a_cinco(lista_palabras)

print("Palabras con más de 5 letras:", resultado)