"""
Ejercicio 5 
Hacé un procedimiento que indique si un número es par o impar.
"""
def es_par_o_impar(numero):
    """
    Indica si el número proporcionado es par o impar.
    
    :param numero: int, el número a evaluar
    """
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
# Solicitar al usuario un número
numero_usuario = int(input("Por favor, ingresa un número para verificar si es par o impar: "))
# Llamada a la función para verificar si el número es par o impar
es_par_o_impar(numero_usuario)
