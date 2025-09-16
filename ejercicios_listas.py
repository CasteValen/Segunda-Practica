# Ejercicio 11: Ingresar notas hasta -1, calcular el promedio y cuántos están por debajo del promedio

notas = []  # Lista para guardar las notas ingresadas

while True:
    # Pedimos al usuario que ingrese una nota
    entrada = input("Ingrese una nota del 1 al 10 (-1 para terminar): ")

    # Verificamos si quiere salir del programa
    if entrada == "-1":
        break

    try:
        nota = float(entrada)  
        if 1 <= nota <= 10:
            notas.append(nota)  # Agregamos nota válida a la lista
        else:
            print("Nota inválida. Ingrese un número entre 1 y 10.")
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")

# Si se ingresaron notas válidas, calculamos y mostramos resultados
if notas:
    promedio = sum(notas) / len(notas)
    print(f"\nNotas ingresadas: {notas}")
    print(f"Promedio: {promedio:.2f}")

    # Contamos cuántas notas están por debajo del promedio
    debajo = sum(1 for n in notas if n < promedio)
    print(f"La cantidad de notas por debajo del promedio es de: {debajo}")
else:
    print("No se ingresaron notas válidas")