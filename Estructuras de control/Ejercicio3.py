#Solicitar al usuario 6 números y mostrar el promedio solo de los números mayores que 100.
contador_mayores =0
numeros_mayores =[]
print("Ingrese 6 números para evaluar el promedio de los mayores que 100.")
for i in range(6):
    numero=int(input("Ingrese un numero: "))
    if numero > 100:
        contador_mayores +=1
        numeros_mayores.append(numero)
        if contador_mayores > 0:
            promedio_mayores = sum(numeros_mayores) / contador_mayores
        else:
            promedio_mayores = 0
print("La cantidad de números mayores que 100 es: ", contador_mayores)
print("El promedio de los números mayores que 100 es: ", promedio_mayores)
# Fin del programa