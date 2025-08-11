#Ingresar 10 números y mostrar cuántos son múltiplos de 3.

for i in range(10):
    print("Ingrese un número para verificar si es múltiplo de 3.")
    try:
        numero = int(input("ingresa un numero: "))
        if numero % 3 == 0:
            print(f"{numero} es multiplo de 3")
        else:
            print(f"{numero} no es multiplo de 3")
    except ValueError:
        print("Por favor, ingrese un número válido.")
print("Fin del ejercicio")
# Fin del ejercicio
        