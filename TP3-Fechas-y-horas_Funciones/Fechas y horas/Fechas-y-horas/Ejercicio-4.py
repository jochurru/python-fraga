"""
Ejercicio 4
Calculá cuántos días faltan para que termine el año (es decir, hasta el 31 de
diciembre del año actual).
"""

import datetime
# Obtener la fecha y hora actual
fecha_actual = datetime.datetime.now()
# Obtener el año actual
anio_actual = fecha_actual.year
# Crear un objeto datetime para el 31 de diciembre del año actual
fin_anio = datetime.datetime(anio_actual, 12, 31)   
# Calcular la diferencia entre el 31 de diciembre y la fecha actual
diferencia = fin_anio - fecha_actual
# Obtener la cantidad de días restantes
dias_restantes = diferencia.days
# Mostrar la cantidad de días restantes para que termine el año
print(f"Faltan {dias_restantes} días para que termine el año {anio_actual}.")
# Mostrar la fecha actual en un formato legible
formato_actual = fecha_actual.strftime("%d/%m/%Y")
print(f"Fecha actual: {formato_actual}")
# Mostrar la fecha de fin de año en un formato legible
formato_fin_anio = fin_anio.strftime("%d/%m/%Y")
print(f"Fecha de fin de año: {formato_fin_anio}")