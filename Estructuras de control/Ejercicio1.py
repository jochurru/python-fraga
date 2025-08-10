#Ingresar 7 números y mostrar cuántos son mayores que 10.

contador=0
numeros_mayores = []
print("Ingrese 7 números para evaluar cuántos son mayores que 10.")
for i in range(7):
    numero=int(input("ingrese un mumero: "))
    if numero > 10:
        contador += 1
        numeros_mayores.append(numero)
print("La cantidad de numeros mayores que 10 es: ", contador)
print("Los números mayores que 10 son: ", numeros_mayores)
# Fin del programa