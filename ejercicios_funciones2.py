# Ejercicio 9: Contar vocales en una palabra o frase

def contar_vocales(cadena: str) -> dict:
    # Pasar todo a minúsculas
    cadena = cadena.lower()
    
    # Equivalencias de vocales con tilde a vocales sin tilde
    equivalencias = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u"
    }
    
    # Inicializar el contador para cada vocal
    vocales = "aeiou"
    contador = {v: 0 for v in vocales}

    # Recorrer cada letra de la cadena
    for letra in cadena:
        # Reemplazar vocal con tilde por su equivalente
        if letra in equivalencias:
            letra = equivalencias[letra]
        # Contar la vocal si corresponde
        if letra in contador:
            contador[letra] += 1

    return contador

# Solicitar al usuario que ingrese una palabra o frase
frase = input("Ingrese una palabra o frase: ")
resultado = contar_vocales(frase)

# Mostrar el resultado
print("Cantidad de vocales:", resultado)