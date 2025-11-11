#Pedir 7 números al usuario y mostrar cuál fue el mayor número ingresado.
numeros =[]
print("Ingrese 7 números para determinar cuál es el mayor.")
for i in range(7):
    try:
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")
mayor_numero = max(numeros) if numeros else None
if mayor_numero is not None:
    print("El mayor número ingresado es:", mayor_numero)
else:
    print("No se ingresaron números válidos.")
# Fin del ejercicio