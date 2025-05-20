#trabajo practico numero 2
#Ejercicio 1
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

#Ejercicio 2
contador_max=0
contador_min=0
nro1=0
maximo=5
for i in range (5):
    nro1=int(input("Ingrese un numero: "))
    if nro1 > maximo:
        maximo=nro1
        contador_max=contador_max+1
        print(f"El contador es: {contador_max}")
    else:
        if nro1 < maximo:
            contador_min=contador_min+1
            print(f"El contador es: {contador_min}")

print(f"El total de numeros mayores a 5 es: {contador_max}")
print(f"El total de numeros menores a 5 es: {contador_min}")

#Ejercicio 3
maximo=0
minimo=999

for i in range(5):
    num2=int(input("Ingrese un numero: "))
    if num2 > maximo:
        maximo=num2
    if num2 < minimo:
        minimo=num2
print(f"El numero maximo es: {maximo}")
print(f"El numero minimo es: {minimo}")
