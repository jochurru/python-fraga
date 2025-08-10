#----------------------------------------------------------------------------------------------
#Limite de impresiones con bucle for
limite=int(input("Hasta que numero queres contar?: "))

for i in range (1, limite+1):
        print (i)
#-----------------------------------------------------------------------------------------------

#bucle aplicado con while
contador=0
acumulador=0
lista=[]
while contador<6:
        numero=int(input(f"Ingresa el numero {contador+1}: "))
        acumulador+=numero
        contador+=1
        promedio=acumulador/contador
        numeros=int (numero)
        lista.append(numeros)

print(f"La suma total de los 6 numeros es: {str(acumulador)}")
print(f"El promedio de los numeros ingresados es: {str(promedio)} ")
print(f"La lista es: {str(lista)}")

#----------------------------------------------------------------------------------------------

#Bucle aplicado con for
suma=0
contador2=0
x=0
lista2=[]

for x in range(1,7):
        x=int(input("Ingrese un numero: "))
        print(f"Ingresaste el numero: {x}")
        contador2=contador2+1        
        suma=suma+x
        promedio2= suma/contador2
        numero=int (x)
        lista2.append(numero)
        

print (f"El contador es: {str(contador2)}")
print(f"La suma de los numeros es: {str(suma)}")
print (f"El promedio de los numeros ingresados es: {str(promedio2)}")
print (f"La lista es: {str(lista2)}")

#----------------------------------------------------------------------------------------------
