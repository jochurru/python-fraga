# main.py

# Importamos las clases necesarias
from clases_cesta import cesta, frutas 

def mostrar_menu():
    """Muestra las opciones disponibles al usuario."""
    print("\n" + "=" * 30)
    print("      🛒 MENÚ DE LA CESTA      ")
    print("=" * 30)
    print("1. Agregar frutas")
    print("2. Eliminar frutas")
    print("3. Mostrar cesta actual")
    print("4. Mostrar el total de frutas (Pendiente)") # Podríamos añadir esta función después
    print("5. Salir del programa")
    print("=" * 30)

def main():
    """Función principal que controla el flujo del programa con un menú."""
    
    mi_cesta_interactiva = cesta()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            # La clase cesta ya tiene su propio bucle interno de entrada
            mi_cesta_interactiva.pedir_frutas_al_usuario()
            
        elif opcion == '2':
            # La clase cesta ya tiene su propio bucle interno de eliminación
            mi_cesta_interactiva.eliminar_frutas_al_usuario()
            
        elif opcion == '3':
            mi_cesta_interactiva.mostrar_cesta()
            
        elif opcion == '4':
            print("Función de calcular total aún no implementada.")
            # Si hubieras añadido el método 'calcular_total()', lo llamarías aquí.
            
        elif opcion == '5':
            print("\n¡Gracias por usar el gestor de cestas! 👋")
            break # Rompe el bucle while True, terminando el programa
            
        else:
            print("❌ Opción no válida. Por favor, elige un número del 1 al 5.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()