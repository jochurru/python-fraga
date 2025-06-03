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
    print("\nBienvenido al programa de operaciones matemáticas.")
    print("Puedes realizar operaciones de suma, resta, multiplicación y división.")
    print("Escribe '0' para salir del programa.\n")
    try:
        a = int(input("Ingresa el primer número: "))
        if a == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        b = int(input("Ingresa el segundo número: "))
        if b == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        print(f"\n¿Qué cálculo quieres realizar entre {a} y {b}?")
        print("1 - Sumar")
        print("2 - Restar")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("Escribe '0' para salir del programa.\n")

        opcion = input("Selecciona una opción (1-4) para realizar una operacion o '0' para salir: ")

        if opcion == '1':
            print(f"\nHas seleccionado sumar {a} y {b}.")
            sumar(a, b)        
        
        elif opcion == '2':
            print(f"\nHas seleccionado restar {a} y {b}.")
            restar(a, b)
        
        elif opcion == '3':
            print(f"\nHas seleccionado multiplicar {a} y {b}.")
            multiplicar(a, b)
        
        elif opcion == '4':
            print(f"\nHas seleccionado dividir {a} y {b}.")
            if b == 0:
                print("Error: No se puede dividir entre cero.")
            dividir(a, b)
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
            
        else:
            print("Has ingresado una opción incorrecta.\n")
    except ValueError:
        print("Error: Ingresa solo números válidos.\n")


