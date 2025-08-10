"""
Ejemplo 3
Pedile al usuario que ingrese su fecha de nacimiento con el formato dd/mm/aaaa
y calculá su edad actual en años.

"""
import datetime
# Solicitar al usuario que ingrese su fecha de nacimiento
fecha_nacimiento_str = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
# Convertir la cadena de texto a un objeto datetime
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
# Obtener la fecha y hora actual
fecha_actual = datetime.datetime.now()
# Calcular la diferencia entre la fecha actual y la fecha de nacimiento
diferencia = fecha_actual - fecha_nacimiento
# Calcular la edad en años
edad = diferencia.days // 365
# Mostrar la edad del usuario
print(f"Su edad actual es: {edad} años")
# Mostrar la fecha de nacimiento en un formato legible
formato_legible = fecha_nacimiento.strftime("%d/%m/%Y")
print(f"Su fecha de nacimiento es: {formato_legible}")
# Mostrar la fecha actual en un formato legible
formato_actual = fecha_actual.strftime("%d/%m/%Y")
print(f"Fecha actual: {formato_actual}")
