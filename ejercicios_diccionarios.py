# Ejercicio 15
# Leer nombres y notas hasta 'FIN' y guardar en un diccionario.
# Luego mostrar promedio general, mejor estudiante y estudiantes por debajo del promedio.

notas = {}  # Diccionario para guardar {nombre: nota}

print("Ingrese nombres y notas de los estudiantes. Escriba 'FIN' para terminar.\n")

while True:
    nombre = input("Nombre del estudiante: ")
    if nombre.upper() == "FIN":
        break

    while True:  # Bucle interno para validar la nota
        try:
            nota = float(input("Nota (0-10): "))
            if 0 <= nota <= 10:
                notas[nombre] = nota
                break  # Nota válida, salimos del bucle interno
            else:
                print("Nota inválida. Debe estar entre 0 y 10.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

# Si se ingresaron notas
if notas:
    promedio = sum(notas.values()) / len(notas)
    mejor_estudiante = max(notas, key=notas.get)
    debajo_promedio = [nombre for nombre, nota in notas.items() if nota < promedio]

    print("\n--- Resultados ---")
    print(f"Promedio general: {promedio:.2f}")
    print(f"Mejor estudiante: {mejor_estudiante} ({notas[mejor_estudiante]})")

    if debajo_promedio:
        print("Estudiantes por debajo del promedio:")
        for nombre in debajo_promedio:
            print(f"- {nombre} ({notas[nombre]})")
    else:
        print("No hay estudiantes por debajo del promedio.")
else:
    print("No se ingresaron notas válidas.")

