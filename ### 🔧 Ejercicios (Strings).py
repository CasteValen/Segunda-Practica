# Ejercicios (Strings)

# Ejercicio 1: palabra en mayúsculas, minúsculas y title case
palabra = input("Ingrese una palabra: ")
print("Mayúsculas: ", palabra.upper())
print("Minúsculas: " , palabra.lower())
print("TitleCase: " , palabra.title())

print("-" * 40)

# Ejercicio 2: contar cuántas veces aparece cada vocal
frase = input("Ingrese una frase: ")
frase = frase.lower()
print("a:", frase.count("a") + frase.count("á"))
print("e:", frase.count("e") + frase.count("é"))
print("i:", frase.count("i") + frase.count("í"))
print("o:", frase.count("o") + frase.count("ó"))
print("u:", frase.count("u") + frase.count("ú"))

print("-" * 40)

# Ejercicio 3: mostrar 3 primeras y 3 últimas letras con slicing
frase2 = input("Ingrese otra frase: ")
print("Primeras 3 letras:", frase2[:3])
print("Últimas 3 letras:", frase2[-3:])

print("-" * 40)

# Ejercicio 4: verificar si una palabra contiene la letra 'r'
palabra2 = input("Ingrese otra palabra: ")
if "r" in palabra2.lower():
    print("La palabra contiene la letra r")
else: 
    print("La palabra NO contiene la letra r")   