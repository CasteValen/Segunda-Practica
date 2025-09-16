# Ejercicio 19
# Función que devuelve un diccionario con la frecuencia de cada letra,
# considerando vocales con tilde como normales

def frecuencias_letras(frase: str) -> dict:
    # Equivalencias de vocales con tilde a sin tilde
    equivalencias = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u"
    }

    # Convertimos a minúsculas
    frase = frase.lower()
    
    freq = {}
    for letra in frase:
        if letra in equivalencias:
            letra = equivalencias[letra]
        if letra.isalpha():  # Solo letras
            if letra in freq:
                freq[letra] += 1
            else:
                freq[letra] = 1
    return freq

# Entrada del usuario
entrada = input("Ingrese una frase: ")
resultado = frecuencias_letras(entrada)

# Mostramos el resultado
print("Frecuencia de letras:", resultado)