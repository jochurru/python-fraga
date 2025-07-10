"""
Ejercicio 1
Definí un procedimiento que reciba un nombre y muestre un saludo personalizado.
"""

def saludo_personalizado(nombre):
    """
    Muestra un saludo personalizado con el nombre proporcionado.
    
    :param nombre: str, el nombre de la persona a saludar
    """
    print(f"¡Hola, {nombre}! ¡Bienvenido!")

nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo_personalizado(nombre_usuario)
