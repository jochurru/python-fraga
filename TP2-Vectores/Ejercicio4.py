#Crear una lista con los cuadrados de los números pares del 1 al 10.
lista_cuadrados_pares = []
for num in range(1, 11):
    if num % 2 == 0:
        lista_cuadrados_pares.append(num ** 2)
    if num % 2 ==0:
        lista_cuadrados_pares.append(num ** 2)
# Imprimir la lista de cuadrados de números pares
print(f"Lista de cuadrados de numeros pares del 1 al 10: {lista_cuadrados_pares}")
