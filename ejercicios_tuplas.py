# Ejercicio 13
# Guardar coordenadas (x, y) en una tupla e imprimir la distancia al origen.

def distancia_al_origen(coordenada: tuple) -> float:
    x, y = coordenada
    return (x**2 + y**2) ** 0.5   # Calculamos la distancia al origen (Teorema de Pitágoras)


# Programa principal
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

coordenada = (x, y)  # Guardamos en una tupla

print(f"La coordenada ingresada es: {coordenada}")
print(f"Distancia al origen: {distancia_al_origen(coordenada):.2f}")
