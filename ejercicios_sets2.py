# Ejercicio 18
# Eliminar duplicados de una lista manteniendo el orden

# Ingresamos la lista de números separados por espacios
entrada = input("Ingrese una lista de números separados por espacios: ").split()

# Convertimos a enteros
lista = [int(x) for x in entrada]

# Inicializamos set para llevar el control de elementos ya vistos
vistos = set()
lista_sin_duplicados = []

# Recorremos la lista y agregamos solo elementos no vistos
for num in lista:
    if num not in vistos:
        lista_sin_duplicados.append(num)
        vistos.add(num)

# Mostramos la lista resultante
print("Lista sin duplicados, manteniendo el orden:", lista_sin_duplicados)
