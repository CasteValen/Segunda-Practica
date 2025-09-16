# Ejercicio 17
# Pedir dos listas de números y mostrar su intersección usando set

# Ingresar la primera lista de números
lista1 = input("Ingrese la primera lista de números (separados por espacios): ").split()
lista1 = [int(num) for num in lista1]  # Convertimos a enteros

# Ingresar la segunda lista de números
lista2 = input("Ingrese la segunda lista de números (separados por espacios): ").split()
lista2 = [int(num) for num in lista2]  # Convertimos a enteros

# Convertimos las listas a sets y calculamos la intersección
interseccion = set(lista1) & set(lista2)

# Mostramos el resultado
print("\nIntersección de las dos listas:", interseccion)
