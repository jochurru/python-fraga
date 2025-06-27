# Definición de funciones
#Este es un procedimiento que retorna un valor
def datos_personales():
    nombre=input("Por favor ingresa tu nombre:").capitalize().strip()
    apellido=input("Por favor ingresa tu apellido:").capitalize().strip()
    edad=int(input("Por favor ingresa tu edad:"))
    return nombre, apellido, edad

saludar= datos_personales()

print(f"Hola {saludar[0]} {saludar[1]}, tienes {saludar[2]} años de edad")

#--------------------------------------------------------------------------------------------
def suma(a, b):
    resultado = a + b
    return resultado

a=int(input("Por favor ingresa el primer número: "))
b=int(input("Por favor ingresa el segundo número: "))

resultado_suma = suma(a, b)
print(f"La suma de {a} y {b} es: {resultado_suma}")
#--------------------------------------------------------------------------------------------
