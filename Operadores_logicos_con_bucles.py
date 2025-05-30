print("Operadores lógicos con bucles\n")
print("----------------------------------------------------------------------------------------------------------")
#Ejemplo con and; Imprimir solo los numeros de una lista que sean pares y mayores a 10:

print(f"'Ejemplo con and'\n Imprimir solo los numeros de una lista que sean pares y mayores a 10:")
numeros =[5,12,15,18,20,7,14]
for num in numeros:
    if num % 2 == 0 and num > 10:
        print(f"{num} es par y mayor a 10\n")

print("----------------------------------------------------------------------------------------------------------")
#Ejemplo con or; Contar elementos en una lista que sean menores a 0 o mayores a 100:
print(f"\n'Ejemplo con or'\n Contar elementos en una lista que sean menores a 0 o mayores a 100:")
valores = [-5, 50, 120, 75, -10,150, 30]
contador= 0
for val in valores:
    if val < 0 or val > 100:
        contador += 1
print(f"Cantidad de elementos menores a 0 o mayores a 100: {contador}\n")

print("----------------------------------------------------------------------------------------------------------\n")
#Ejemplo con not; Excluir un valor específico de una lista:
print(f"\n'Ejemplo con not'\n Excluir un valor específico de una lista:")
nombres = ["Ana", "Luis", "Maria","Pedro", "Sofia"]
for nombre in nombres:
    if not nombre == "Luis":
        print(f"Invitado a {nombre} \n")
print("----------------------------------------------------------------------------------------------------------\n")
#Operadores logicos en la estructura While:
print("Operadores lógicos en la estructura While\n")
print("----------------------------------------------------------------------------------------------------------")
#Ejemplo con and; Solicitar un numero que este dentro de un rango especifico:
numero = int(input("Ingrese un numero entre 1 y 100: "))
while numero < 1 or numero > 100:
    print("Numero fuera de rango. Intente nuevamente.")
    numero = int(input("Ingrese un numero entre 1 y 100: "))
print(f"Gracias, el numero {numero} es valido\n")
print("----------------------------------------------------------------------------------------------------------\n")
#Ejemplo con or; Continuar un programa hasta que el usuario decida salir de varias maneras:
respuesta =""
while respuesta.lower() != "salir" and respuesta.lower() != "exit":
    respuesta = input("Ingrese 'salir' o 'exit' para terminar el programa: ")
    if respuesta.lower() != "salir" and respuesta.lower() != "exit":
        print("Comando invalido, Ingrese 'salir' o 'exit' para finalizar\n")
    else:
        print("Programa finalizado.\n")
print("----------------------------------------------------------------------------------------------------------\n")
#Ejemplo con not; Contar hasta un numero mientras no se cumpla una condicion especifica:
contador = 1
limite = 10
while not contador > limite:
    print(f"Contador: {contador}")
    contador += 1
print("Contador ha alcanzado el limite, finalizando el bucle.\n")
print("----------------------------------------------------------------------------------------------------------\n")
#Ejemplo practico completo:
print("Ejemplo practico completo\n")
print("----------------------------------------------------------------------------------------------------------")

# Ejemplo práctico completo
"""
A continuación, presento un programa que combina los operadores lógicos en las tres
estructuras (if, while) para simular un sistema de gestión de notas estudiantiles:

"""
# Sistema de gestión de notas estudiantiles
notas = []
while True:
    entrada= input("Ingrese una nota entre 0 y 10 (o 'salir' para terminar): ").strip()
    if entrada.lower() == 'salir':
        break
    entrada_normalizada = entrada.replace(',', '.')

    if entrada_normalizada.replace('.', '', 1).isdigit():
        nota = float(entrada_normalizada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota fuera de rango. Debe estar entre 0 y 10.")
print(f"Notas ingresadas: {notas}\n")

#Procesar las notas ingresadas:
aprobados = 0
desaprobados = 0
notas_altas = 0
for nota in notas:
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1
    if nota > 8:
        notas_altas += 1
print(f"\nTotal de aprobados: {aprobados}")
print(f"Total de desaprobados: {desaprobados}")
print(f"Total de notas altas (mayores a 8): {notas_altas}\n")
print("----------------------------------------------------------------------------------------------------------\n")
# Fin del ejemplo práctico