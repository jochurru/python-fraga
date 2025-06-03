# Definimos las funciones matemáticas
def sumar(a, b):
    print("Resultado:", a + b)

def restar(a, b):
    print("Resultado:", a - b)

def multiplicar(a, b):
    print("Resultado:", a * b)

def dividir(a, b):
    try:
        print("Resultado:", a / b)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

# Bucle principal del programa
while True:
    try:
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))

        print(f"\n¿Qué cálculo quieres realizar entre {a} y {b}?")
        print("1 - Sumar")
        print("2 - Restar")
        print("3 - Multiplicar")
        print("4 - Dividir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            sumar(a, b)
            break
        elif opcion == '2':
            restar(a, b)
            break
        elif opcion == '3':
            multiplicar(a, b)
            break
        elif opcion == '4':
            dividir(a, b)
            break
        else:
            print("Has ingresado una opción incorrecta.\n")
    except ValueError:
        print("Error: Ingresa solo números válidos.\n")


# Definimos las funciones matemáticas
def sumar(a, b):
    print("Resultado:", a + b)

def restar(a, b):
    print("Resultado:", a - b)

def multiplicar(a, b):
    print("Resultado:", a * b)

def dividir(a, b):
    try:
        print("Resultado:", a / b)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

# Diccionario de operaciones
operaciones = {
    '1': ("Sumar", sumar),
    '2': ("Restar", restar),
    '3': ("Multiplicar", multiplicar),
    '4': ("Dividir", dividir)
}

# Bucle principal
while True:
    try:
        # Entrada de datos
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))

        # Menú
        print(f"\n¿Qué cálculo quieres realizar entre {a} y {b}?")
        for clave, (nombre, _) in operaciones.items():
            print(f"{clave} - {nombre}")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion in operaciones:
            # Ejecutar la operación correspondiente
            funcion = operaciones[opcion]
            funcion(a, b)  # Llamamos a la función correspondiente
        else:
            print("Has ingresado una opción incorrecta.\n")
            continue  # Volver al menú
        # Preguntar si desea continuar después de cada operación
        repetir = input("\n¿Deseas realizar otro cálculo? (s/n): ").strip().lower()
        if repetir != 's':
            print("Programa finalizado.")
            break  # Salir del bucle

    except ValueError:
        print("Error: Ingresa solo números válidos.\n")  # Manejo de errores

