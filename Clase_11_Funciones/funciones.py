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

#calcular IMC

def calcular_imc(peso, altura):
    imc= peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Vas bien"
    elif 25 <= imc < 29.9:
        return "Estas abrazable 😄"
    else:
        return "Sos un osito🐻"
# Solicitar datos al usuario
peso = float(input("Por favor ingresa tu peso en kg: "))
altura = float(input("Por favor ingresa tu altura en metros: "))

# Calcular IMC
imc = calcular_imc(peso, altura)

# Clasificar IMC
clasificacion = clasificar_imc(imc)
print(f"Tu IMC es: {imc:.2f} y tu clasificación es: {clasificacion}")

#--------------------------------------------------------------------------------------------
