#trabajo practico numero 2
suma=0
contador=0
nro=0
contador2=0

for i in range(1,6):
    nro=int(input("Ingrese un numero: "))
    print(f"Ingresaste el numero: {nro}")
    if nro > 5:
        contador=contador+1
        print(f"El contador es: {contador}")
    else:
        contador2=contador2+1
        print(f"El contador es: {contador2}")
print(f"El total de numeros mayores a 5 es: {contador}")
print(f"El total de numeros menores a 5 es: {contador2}")
