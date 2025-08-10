from datetime import datetime

ahora= datetime.now()
print("Fecha y hora actual:", ahora)

from datetime import date

inicio = date(2025, 5, 20)  

hoy= date.today()

dias_transcurridos = (hoy - inicio).days
print("Días transcurridos desde el 20 de junio de 2025:", dias_transcurridos)

from datetime import timedelta

futuro= hoy + timedelta(days=30)

print(f"Fecha dentro de 30 dias: {futuro}")

#calcular edad a partir de la fecha de nacimiento
def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad
# Solicitar fecha de nacimiento al usuario
fecha_nacimiento_str = input("Por favor ingresa tu fecha de nacimiento (YYYY-MM-DD): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
edad = calcular_edad(fecha_nacimiento)
print(f"Tu edad es: {edad} años")


