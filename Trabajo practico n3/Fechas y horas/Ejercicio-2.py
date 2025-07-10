"""
Ejercicio 2:
Modificá el programa anterior para que muestre únicamente la fecha (sin la hora).

"""
import datetime
# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
# Mostrar la fecha actual
print("Fecha actual:", fecha_hora_actual.date())
# Mostrar la fecha actual en un formato más legible
formato_legible = fecha_hora_actual.strftime("%Y-%m-%d")
print("Fecha actual (formato legible):", formato_legible)
# Mostrar la fecha actual en un formato personalizado
formato_personalizado = fecha_hora_actual.strftime("%d/%m/%Y")
print("Fecha actual (formato personalizado):", formato_personalizado)