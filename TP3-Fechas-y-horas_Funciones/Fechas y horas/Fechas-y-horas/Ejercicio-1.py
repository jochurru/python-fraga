"""
Ejemplo 1 
Escribí un programa que obtenga la fecha y hora actual del sistema y la muestre por
pantalla.
"""
import datetime
# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
# Mostrar la fecha y hora actual
print("Fecha y hora actual:", fecha_hora_actual)
# Mostrar la fecha y hora actual en un formato más legible
formato_legible = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
print("Fecha y hora actual (formato legible):", formato_legible)