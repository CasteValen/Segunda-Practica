# Ejercicio 21: letras únicas de una frase

# Pedimos al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# Convertimos todo a minúsculas para que las mayúsculas no cuenten como letras diferentes
frase = frase.lower()

# Creamos un set con las letras, ignorando espacios
letras_unicas = set(frase.replace(" ", ""))

# Mostramos la cantidad de letras únicas
print(f"Cantidad de letras únicas: {len(letras_unicas)}")

# Creamos una lista ordenada de las letras únicas
lista_ordenada = sorted(letras_unicas)
print("Lista ordenada de letras únicas:", lista_ordenada)