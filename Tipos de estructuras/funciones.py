def suma (a,b):
    """
    Suma dos números y devuelve el resultado.
    
    Parámetros:
    a (int, float): El primer número.
    b (int, float): El segundo número.
    
    Retorna:
    int, float: La suma de a y b.
    """
    return a + b

def resta (a,b):
    """
    Resta el segundo número del primero y devuelve el resultado.
    
    Parámetros:
    a (int, float): El primer número.
    b (int, float): El segundo número.
    
    Retorna:
    int, float: La resta de a y b.
    """
    return a - b

def multiplicacion (a,b):
    """
    Multiplica dos números y devuelve el resultado.
    
    Parámetros:
    a (int, float): El primer número.
    b (int, float): El segundo número.
    
    Retorna:
    int, float: El producto de a y b.
    """
    return a * b

def division (a,b):
    """
    Divide el primer número por el segundo y devuelve el resultado.
    
    Parámetros:
    a (int, float): El numerador.
    b (int, float): El denominador.
    
    Retorna:
    int, float: El cociente de a y b.
    
    Lanza:
    ValueError: Si b es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

while True:
    a= input("Ingrese el primer número (o 'salir' para terminar): ")
    if a.lower() == 'salir':
        break
    b = input("Ingrese el segundo número (o 'salir' para terminar): ")
    if b.lower() == 'salir':
        break
    try:
        a = float(a)
        b = float(b)
        print("Que operación desea realizar?")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        operacion = input("Ingrese el número de la operación: ")
        if operacion == '1':
            resultado = suma(a, b)
            print(f"La suma de {a} y {b} es: {resultado}\n")
        elif operacion == '2':
            resultado = resta(a, b)
            print(f"La resta de {a} y {b} es: {resultado}\n")
        elif operacion == '3':
            resultado = multiplicacion(a, b)
            print(f"La multiplicación de {a} y {b} es: {resultado}\n")
        elif operacion == '4':
            try:
                resultado = division(a, b)
                print(f"La división de {a} entre {b} es: {resultado}\n")
            except ValueError as e:
                print(f"Error: {e}. No se puede dividir por cero.\n")
        else:
            print("Operación no válida. Por favor, ingrese un número entre 1 y 4.\n")
            continue
    except ValueError as e:
        print(f"Error: {e}. Asegúrese de ingresar números válidos.\n")
