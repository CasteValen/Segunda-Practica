# Ejercicio 14
# Dada una lista de tuplas (nombre, edad), imprimir solo los mayores de 18.

personas = []

print("Ingrese los nombres y edades de las personas. Escriba 'fin' para terminar.\n")

while True:
    nombre = input("Nombre: ")
    if nombre.lower() == "fin":
        break

    try:
        edad = int(input("Edad: "))
        personas.append((nombre, edad))
    except ValueError:
        print("⚠️ Edad inválida, intente nuevamente.")

print("\nPersonas mayores de 18 años:\n")
for nombre, edad in personas:
    if edad > 18:
        print(f"{nombre} ({edad} años)")
