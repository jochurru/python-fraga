#ingreso de notas de estudiantes
print("Bienvenido al sistema de notas de estudiantes.")
# Inicialización de la lista de estudiantes
estudiantes = []

while True:
    nota=(input("Ingrese la nota del estudiante ('s' para salir): "))
    if nota == 's':
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    try:
        nota = int(nota)
        if nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10. Inténtalo de nuevo.")
            continue
        estudiantes.append(nota)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido o 's' para salir.")
        continue
# Procesar las notas ingresadas
aprobados = []
reprobados = []
notas_altas = []
for nota in estudiantes:
    if nota >= 6:
        aprobados.append(nota)
    else:
        reprobados.append(nota)
    if nota >= 9:
        notas_altas.append(nota)
# Mostrar los resultados
print("\nResultados del sistema de notas:")
print(f"Total de estudiantes: {len(estudiantes)}")
print(f"Estudiantes aprobados: {len(aprobados)}")
print(f"Estudiantes reprobados: {len(reprobados)}")
print(f"Estudiantes con notas altas (9 o más): {len(notas_altas)}")
print(f"Notas aprobadas: {aprobados}")
print(f"Notas reprobadas: {reprobados}")
print(f"Notas altas: {notas_altas}")
# Fin del programa
print("Gracias por usar el sistema de notas de estudiantes. ¡Hasta luego!")