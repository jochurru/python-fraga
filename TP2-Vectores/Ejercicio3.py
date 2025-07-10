#Dadas dos listas del mismo tamaño, sumar elemento a elemento.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
suma_listas = []
for i in range(len(lista1)):
    suma_listas.append(lista1[i] + lista2[i])
# Imprimir la lista resultante de la suma
print(f"Suma de las dos listas: {suma_listas}")
