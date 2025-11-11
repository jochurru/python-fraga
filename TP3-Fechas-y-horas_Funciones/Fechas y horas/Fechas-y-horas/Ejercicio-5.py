"""
Ejercicio 5
Solicitá al usuario una fecha en formato dd/mm/aaaa. Validá si la fecha es válida
o no usando el manejo de excepciones. Ejercitación de Funciones

"""
import datetime
while True:
    fecha_str = input("Ingrese una fecha en formato dd/mm/aaaa: ")
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        print("La fecha es válida.")
        break
    except ValueError:
        print("Fecha inválida. Por favor, intente nuevamente.")
# Mostrar la fecha ingresada en un formato legible
formato_legible = fecha.strftime("%d/%m/%Y")
print(f"Fecha ingresada: {formato_legible}")
# Mostrar la fecha ingresada en un formato personalizado
formato_personalizado = fecha.strftime("%d de %B de %Y")
print(f"Fecha ingresada (formato personalizado): {formato_personalizado}")