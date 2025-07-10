#Verificar si una lista está en orden ascendente.
lista = []
# Solicitar al usuario que ingrese números para la lista
while True:
    entrada = input("Ingrese un número (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = float(entrada)
        lista.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")
# Verificar si la lista está en orden ascendente
esta_ordenada = True
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        esta_ordenada = False
        break
# Imprimir si la lista está ordenada o no
if esta_ordenada:
    print("La lista está en orden ascendente.")
else:
    print("La lista no está en orden ascendente.")
