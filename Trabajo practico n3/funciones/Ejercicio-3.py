"""
Ejercicio 3
Escribí un procedimiento que muestre la tabla del número recibido

"""
def mostrar_tabla(numero):
    """
    Muestra la tabla de multiplicar del número proporcionado.
    
    :param numero: int, el número del cual se desea mostrar la tabla de multiplicar
    """
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
# Solicitar al usuario un número
numero_usuario = int(input("Por favor, ingresa un número para mostrar su tabla de multiplicar: "))
# Llamada a la función para mostrar la tabla de multiplicar 
mostrar_tabla(numero_usuario)
