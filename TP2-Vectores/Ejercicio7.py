#Filtrar los elementos de una lista que sean múltiplos de 3 y mayores que 10.
lista_numeros = [5, 12, 15, 8, 9, 18, 20, 21]
lista_filtrada =[]
for num in lista_numeros:
    if num > 10 and num % 3 == 0:
        lista_filtrada.append(num)
# Imprimir la lista filtrada
print(f"Lista filtrada (múltiplos de 3 y mayores que 10): {lista_filtrada}")
