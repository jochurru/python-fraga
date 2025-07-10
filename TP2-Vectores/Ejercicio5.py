#Dada una lista, encontrar el segundo número más grande.
lista_numeros = [5, 3, 8, 1, 4, 9, 2]
if len(lista_numeros) < 2:
    print("La lista debe tener al menos dos elementos.")
else:
    lista_numeros.sort(reverse=True)
    segundo_mayor = lista_numeros[1]
    print("El segundo número más grande es:", segundo_mayor)

