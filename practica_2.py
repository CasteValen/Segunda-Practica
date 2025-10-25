import csv
from datetime import datetime
import json
from collections import Counter, defaultdict
from pathlib import Path

# 1. Leer el archivo CSV
def leer_archivo_csv(ruta_archivo):
    datos = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append(fila)
        print(f"Se leyeron {len(datos)} registros de {ruta_archivo}")
        return datos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

# 2. Identificar el día de la semana
def obtener_dia_semana(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M')
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        return dias_semana[fecha.weekday()]
    except ValueError as e:
        print(f"Error al parsear fecha '{fecha_str}': {e}")
        return "Desconocido"

# 3. Encontrar día(s) con más sesiones
def dia_mas_sesiones(datos):
    dias = [obtener_dia_semana(registro['timestamp']) for registro in datos]
    contador_dias = Counter(dias)
    
    max_sesiones = max(contador_dias.values())
    dias_max = [dia for dia, count in contador_dias.items() if count == max_sesiones]
    
    return dias_max, max_sesiones

# 4. Días entre primer y último entrenamiento
def dias_entre_entrenamientos(datos):
    if not datos:
        return 0
        
    fechas = [datetime.strptime(reg['timestamp'], '%Y-%m-%d %H:%M') for reg in datos]
    fecha_min = min(fechas)
    fecha_max = max(fechas)
    
    diferencia = fecha_max - fecha_min
    return diferencia.days

# 5. Campeón que más entrenó
def campeon_mas_entreno(datos):
    campeones = [registro['campeon'] for registro in datos]
    contador_campeones = Counter(campeones)
    
    # Uso de lambda para encontrar el máximo por cantidad
    campeon_max = max(contador_campeones.items(), key=lambda x: x[1])
    return campeon_max

# 6. Promedio de entrenamientos por día de la semana
def promedio_entrenamientos_por_dia(datos):
    dias = [obtener_dia_semana(registro['timestamp']) for registro in datos]
    contador_dias = Counter(dias)
    
    # Contar semanas únicas para el promedio
    semanas = set()
    for registro in datos:
        fecha = datetime.strptime(registro['timestamp'], '%Y-%m-%d %H:%M')
        año, semana, _ = fecha.isocalendar()
        semanas.add((año, semana))
    
    num_semanas = len(semanas) if semanas else 1
    
    promedios = {dia: count / num_semanas for dia, count in contador_dias.items()}
    return promedios

# 7. Campeón que más entrena los fines de semana
def campeon_mas_finde(datos):
    entrenamientos_finde = []
    for registro in datos:
        dia = obtener_dia_semana(registro['timestamp'])
        if dia in ['Sábado', 'Domingo']:
            entrenamientos_finde.append(registro['campeon'])
    
    if not entrenamientos_finde:
        return ("Ninguno", 0)
    
    contador = Counter(entrenamientos_finde)
    # Uso de lambda para encontrar el máximo por cantidad
    campeon_max = max(contador.items(), key=lambda x: x[1])
    return campeon_max

# 8. Crear CSV con cantidad de entrenamientos por campeón
def crear_csv_entrenamientos_por_campeon(datos, carpeta_salida):
    campeones = [registro['campeon'] for registro in datos]
    contador_campeones = Counter(campeones)
    
    # Crear carpeta 'salida'
    Path(carpeta_salida).mkdir(parents=True, exist_ok=True)
    
    ruta_csv = Path(carpeta_salida) / 'entrenamientos_por_campeon.csv'
    
    with open(ruta_csv, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['campeon', 'cantidad_entrenamientos'])
        
        # Uso de lambda para ordenar antes de escribir
        for campeon, cantidad in sorted(contador_campeones.items(), key=lambda x: x[1], reverse=True):
            escritor.writerow([campeon, cantidad])
    
    print(f"Archivo CSV creado: {ruta_csv}")

# 9. Crear JSON con resumen por día
def crear_json_resumen(datos, carpeta_salida):
    # Uso de defaultdict para agrupar y contar por fecha y campeón
    datos_por_dia = defaultdict(lambda: defaultdict(int))
    
    for registro in datos:
        fecha_obj = datetime.strptime(registro['timestamp'], '%Y-%m-%d %H:%M')
        fecha_str = fecha_obj.strftime('%Y-%m-%d')
        campeon = registro['campeon']
        datos_por_dia[fecha_str][campeon] += 1
    
    # Estructura de salida
    resumen = {
        'total_registros': len(datos),
        'dias': {}
    }
    
    for fecha, campeones in datos_por_dia.items():
        resumen['dias'][fecha] = {
            'campeones': dict(campeones),
            'total_entrenamientos_dia': sum(campeones.values())
        }
    
    # Crear carpeta 'salida'
    Path(carpeta_salida).mkdir(parents=True, exist_ok=True)
    
    ruta_json = Path(carpeta_salida) / 'resumen_entrenamientos.json'
    
    with open(ruta_json, 'w', encoding='utf-8') as archivo:
        json.dump(resumen, archivo, ensure_ascii=False, indent=2)
    
    print(f"Archivo JSON creado: {ruta_json}")

# Función principal
def main():
    print("=== PRÁCTICA 2 - LENGUAJES 2025 ===\n")
    
    # 1. Leer el archivo
    datos = leer_archivo_csv('actividad_2.csv')
    
    if not datos:
        print("No se pudieron cargar los datos. Terminando ejecución.")
        return
    
    print("\n" + "="*50)
    
    # 2. Agregar día de la semana (Preparación de datos)
    for registro in datos:
        registro['dia_semana'] = obtener_dia_semana(registro['timestamp'])
    
    # 3. Día(s) con más sesiones
    dias_max, cantidad_max = dia_mas_sesiones(datos)
    print(f"3. Día(s) con más sesiones: {', '.join(dias_max)} ({cantidad_max} sesiones)")
    
    # 4. Días entre primer y último entrenamiento
    dias_diferencia = dias_entre_entrenamientos(datos)
    print(f"4. Días entre primer y último entrenamiento: {dias_diferencia} días")
    
    # 5. Campeón que más entrenó
    campeon_max, cantidad_entrenos = campeon_mas_entreno(datos)
    print(f"5. Campeón que más entrenó: {campeon_max} ({cantidad_entrenos} entrenamientos)")
    
    # 6. Promedio de entrenamientos por día de semana
    promedios = promedio_entrenamientos_por_dia(datos)
    print("\n6. Promedio de entrenamientos por día de semana:")
    for dia, promedio in sorted(promedios.items()):
        print(f"   - {dia}: {promedio:.2f} entrenamientos/semana")
    
    # 7. Campeón que más entrena los fines de semana
    campeon_finde, cantidad_finde = campeon_mas_finde(datos)
    print(f"7. Campeón que más entrena fines de semana: {campeon_finde} ({cantidad_finde} entrenamientos)")
    
    print("\n" + "="*50)
    
    # 8. Crear CSV con entrenamientos por campeón
    crear_csv_entrenamientos_por_campeon(datos, 'salida')
    
    # 9. Crear JSON con resumen
    crear_json_resumen(datos, 'salida')
    
    print("\n" + "="*50)
    print("¡Análisis completado! Verifique la carpeta 'salida' para los archivos generados.")

# Ejecutar análisis
if __name__ == "__main__":
    main()