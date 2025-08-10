#Pedir al usuario 5 letras y mostrarlas todas juntas como una palabra.
letras = []
print("Ingrese 5 letras para formar una palabra.")
for i in range(5):
    letra = input("Ingrese una letra: ")
    letras.append(letra)
palabra = ''.join(letras)
print("La palabra formada es: ", palabra)
# Fin del ejercicio
# Fin del ejercicio