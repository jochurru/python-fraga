#Pedir al usuario que ingrese 8 números y mostrar la suma solo de los números negativos.
contador_negativos = 0
numeros_negativos = []
print("Ingrese 8 números para evaluar la suma de los negativos.")
for i in range(8):
    numero=int(input("Ingrese un numero: "))
    if numero < 0:
        contador_negativos +=1
        numeros_negativos.append(numero)
suma_negativos = sum(numeros_negativos)
print("La cantidad de números negativos es: ", contador_negativos)
print("La suma de los números negativos es: ", suma_negativos)
# Fin del programa