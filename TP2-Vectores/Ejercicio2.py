#Dadas dos listas, mostrar los elementos que están en ambas.
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
elementos_comunes = []
for elemento in lista1:
    if elemento in lista2:
        elementos_comunes.append(elemento)
# Imprimir los elementos comunes
print(f"Elementos comunes entre las dos listas: {elementos_comunes}")
