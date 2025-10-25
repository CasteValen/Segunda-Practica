# Práctica 2 - Lenguajes 2025

## Objetivos
- Practicar lectura de archivos CSV con la librería estándar (`csv`, `with open`).
- Manipular fechas con `datetime` (parseo, día de la semana, rangos).
- Aplicar funciones `lambda` con `map`, `filter` y `sorted` en problemas simples de análisis.
- Producir salidas claras (impresiones, tablas CSV y/o JSON breve).

Se usará un dataset temático de **sesiones de entrenamiento de campeones del League of Legends**, con una fecha y hora por registro.

---

## Archivo principal
- `actividad_2.csv`

### Columnas
- `timestamp`
- `campeon`
- `actividad`
- `entrenador`

---

## Enunciado
Desarrollar un script o notebook que realice lo siguiente:

1. Leer el archivo CSV.
2. Identificar el **día de la semana** de cada entrenamiento.
3. Indicar cuál es el/los **día/s de la semana** que tienen más sesiones de entrenamiento.
4. Calcular **cuántos días pasaron** entre el primer y último entrenamiento.
5. Mostrar el **campeón que más entrenó**.
6. Calcular el **promedio de entrenamientos por cada día de la semana**.
7. Determinar el **campeón que más entrena los fines de semana** (sábado y domingo).
8. En una carpeta llamada `salida` (a generar), crear un archivo `.csv` que para cada campeón muestre la cantidad de entrenamientos (campeón y cantidad).
9. Generar un archivo `.json` en la misma carpeta `salida` que indique:
   - El total de registros.
   - Para cada día, los campeones que entrenaron y cuántas veces entrenó cada uno.

---

## Video de explicación
Se debe grabar un **video con cámara** explicando la resolución del ejercicio.  
- Duración máxima: 10 minutos.

---

## Puntaje
- Ejercicio: 20 pts  
- Explicación en video: 20 pts  
**Total máximo:** 40 pts

---

## Fecha límite
**31/10/2025 a las 23:59:59**