#Ingresar 5 números y mostrar la suma de los números que sean mayores a 0 y menores que 50.
numeros = []
print("Ingrese 5 números para calcular la suma de los que son mayores a 0 y menores que 50.")
for i in range(5):
    try:
        numero = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")
suma = sum(num for num in numeros if 0 < num < 50)
print("La suma de los números mayores a 0 y menores que 50 es:", suma)
# Fin del ejercicio