#Pedir al usuario que ingrese 6 palabras y mostrar cuántas tienen más de 4 letras.
contador_palabras = 0
palabras_mayores = []
print("Ingrese 6 palabras para evaluar cuántas tienen más de 4 letras.")
for i in range(6):
    palabra = input("Ingrese una palabra: ")
    if len(palabra) > 4:
        contador_palabras += 1
        palabras_mayores.append(palabra)
print("La cantidad de palabras con más de 4 letras es:", contador_palabras)
print("Las palabras con más de 4 letras son:", palabras_mayores)    
print("Fin del programa")
# Fin del ejercicio