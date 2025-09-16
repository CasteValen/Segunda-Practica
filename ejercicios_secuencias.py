# Ejercicios (Secuencias)

# Ejercicio 5: Pedir una palabra y contar cuántas vocales tiene
palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()
contador_vocales = 0

for letra in palabra:
    if letra in "aeiouáéíóú":
        contador_vocales += 1

print("La palabra tiene", contador_vocales, "vocales")        

print("\n" + "-"*40 + "\n")  

# Ejercicio 6: Ingresar 4 palabras y mostrar únicamente las que contengan la letra 'r'
palabras_con_r = []

for i in range(4):
    palabra2 = input("Ingrese una palabra: ")
    if "r" in palabra2.lower():
        palabras_con_r.append(palabra2)

# Mostrar resultado al final
if palabras_con_r:
    print("Las siguientes palabras contienen la 'r':", palabras_con_r)
else:
    print("Ninguna de las palabras ingresadas contiene la 'r'")

print("\n" + "-"*40 + "\n")  

# Ejercicio 7: Ingresar palabras hasta escribir "FIN"; imprimir las que empiecen y terminen con la misma letra
palabras = []

while True:
    palabra3 = input("Ingrese una palabra. Para terminar ingrese FIN: ")
    if palabra3.upper() == "FIN":
        break
    if palabra3[0].lower() == palabra3[-1].lower():
        palabras.append(palabra3)

if palabras:
    print("Palabras que empiezan y terminan con la misma letra:", palabras)
else:
    print("Ninguna palabra ingresada empieza y termina con la misma letra")
