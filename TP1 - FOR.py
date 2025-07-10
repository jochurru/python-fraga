# TP1 - FOR, ACUMULADOR Y CONTADOR

# Ejercicio 1
suma = 0
for _ in range(5):
    num = int(input("Ejercicio 1 - Ingrese un número: "))
    suma += num
print("Suma total:", suma)

# Ejercicio 2
contador = 0
for _ in range(5):
    num = int(input("Ejercicio 2 - Ingrese un número: "))
    contador += 1
print("Cantidad ingresada:", contador)

# Ejercicio 3
suma = 0
for _ in range(5):
    num = int(input("Ejercicio 3 - Ingrese un número: "))
    suma += num
print("Promedio:", suma / 5)

# Ejercicio 4
suma = 0
for i in range(5):
    num = int(input("Ejercicio 4 - Ingrese un número PAR: "))
    while num % 2 != 0:
        num = int(input("No es par. Ingrese un número PAR: "))
    suma += num
print("Suma de los números pares:", suma)

# Ejercicio 5
contador = 0
for _ in range(5):
    num = int(input("Ejercicio 5 - Ingrese el número 0: "))
    contador += 1
print("Veces que se ingresó:", contador)

# Ejercicio 6
print("Ejercicio 6 - Mostrar los números uno debajo del otro:")
for _ in range(5):
    num = int(input("Ingrese un número: "))
    print(num)

# Ejercicio 7
suma = 0
print("Ejercicio 7 - Acumulando suma:")
for _ in range(5):
    num = int(input("Ingrese un número: "))
    suma += num
    print("Suma acumulada:", suma)

# Ejercicio 8
cadena = ""
for _ in range(5):
    num = input("Ejercicio 8 - Ingrese un número: ")
    cadena += num
print("Cadena final:", cadena)

# Ejercicio 9
print("Ejercicio 9 - Mostrar 'Hola Mundo' 5 veces:")
for _ in range(5):
    print("Hola Mundo")

# Ejercicio 10
suma = 0
for _ in range(5):
    num = int(input("Ejercicio 10 - Ingrese el número 100: "))
    suma += num
print("Suma total:", suma)

# Ejercicio 11
suma = 0
contador = 0
for _ in range(5):
    num = int(input("Ejercicio 11 - Ingrese un número: "))
    suma += num
    contador += 1
print("Suma:", suma)
print("Cantidad de números:", contador)

# Ejercicio 12
suma_cuadrados = 0
for _ in range(5):
    num = int(input("Ejercicio 12 - Ingrese un número: "))
    suma_cuadrados += num ** 2
print("Suma de los cuadrados:", suma_cuadrados)

# Ejercicio 13
num = int(input("Ejercicio 13 - Ingrese un número: "))
suma = 0
for _ in range(5):
    suma += num
print("Suma del número 5 veces:", suma)

# Ejercicio 14
producto = 1
for _ in range(5):
    num = int(input("Ejercicio 14 - Ingrese un número: "))
    producto *= num
print("Producto total:", producto)

# Ejercicio 15
numeros = []
for _ in range(5):
    num = input("Ejercicio 15 - Ingrese un número: ")
    numeros.append(num)
print("Números juntos separados por espacios:", " ".join(numeros))
