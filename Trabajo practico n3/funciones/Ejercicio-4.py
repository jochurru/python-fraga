"""
Ejercicio 4 
Creá un procedimiento que reciba una lista de palabras y las muestre una por una

"""
def mostrar_palabras(palabras):
    """
    Muestra cada palabra de la lista proporcionada una por una.
    
    :param palabras: list, lista de palabras a mostrar
    """
    print("Lista de palabras:")
    for palabra in palabras:
        print(palabra)
# Solicitar al usuario una lista de palabras
palabras_usuario = input("Por favor, ingresa una lista de palabras separadas por un espacio: ")
# Convertir la entrada del usuario en una lista
lista_palabras = palabras_usuario.split(" ")
# Llamada a la función para mostrar las palabras
mostrar_palabras(lista_palabras)
