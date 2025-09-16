# Ejercicio 8: Verificar si una palabra o frase es palíndromo

def es_palindromo(cadena: str) -> bool:
    # Eliminar espacios y pasar todo a minúsculas
    texto = cadena.replace(" ", "").lower()
    # Comparar la cadena con su reverso
    return texto == texto[::-1]

# Pedir al usuario palabras o frases hasta que escriba 'FIN'
while True:
    palabra = input("Ingrese una palabra o frase (FIN para salir): ")
    if palabra.upper() == "FIN":
        print("Programa finalizado")
        break
    # Mostrar True si es palíndromo, False si no
    print(es_palindromo(palabra))