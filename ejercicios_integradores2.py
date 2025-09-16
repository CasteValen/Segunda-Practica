# Ejercicio 20 sin usar statistics

# Diccionario para almacenar {nombre: nota}
notas = {}

while True:
    nombre = input("Ingrese el nombre del alumno (FIN para terminar): ")
    if nombre.upper() == "FIN":
        break

    while True:
        try:
            nota = float(input(f"Ingrese la nota de {nombre} (1-10): "))
            if 1 <= nota <= 10:
                notas[nombre] = nota
                break
            else:
                print("Nota inválida. Debe ser un número entre 1 y 10.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

if notas:
    # Cálculos
    valores = list(notas.values())
    promedio = sum(valores) / len(valores)

    # Mediana manual
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    if n % 2 == 1:
        mediana = valores_ordenados[n // 2]
    else:
        mediana = (valores_ordenados[n//2 - 1] + valores_ordenados[n//2]) / 2

    mejor_nombre = max(notas, key=notas.get)
    peor_nombre = min(notas, key=notas.get)

    print("\n📊 Resultados generales:")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Mejor nota: {notas[mejor_nombre]} ({mejor_nombre})")
    print(f"Peor nota: {notas[peor_nombre]} ({peor_nombre})")

    # Informe ordenado por nombre
    print("\n📝 Informe ordenado por nombre:")
    for alumno in sorted(notas):
        print(f"{alumno}: {notas[alumno]}")
else:
    print("No se ingresaron notas.")