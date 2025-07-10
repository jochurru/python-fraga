#Dada una lista con elementos repetidos, elimina los duplicados sin usar set().
lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = []
for elemento in lista:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)
# Imprimir la lista sin duplicados
print("Lista sin duplicados:", lista_sin_duplicados)
