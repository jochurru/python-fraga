class frutas:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
    def mostrar_info(self):
        return f"Fruta: {self.nombre}, Tipo: {self.tipo}, Precio: ${self.precio}"
    
class cesta:
    def __init__(self):
        self.frutas = []
        
    def agregar_fruta(self, nueva_fruta):
        """
        Agrega una fruta, pero solo si no existe ya una fruta con el mismo nombre.
        """
        nombre_nuevo = nueva_fruta.nombre.lower()

        # 1. Recorrer la lista para verificar si la fruta ya existe
        for fruta_existente in self.frutas:
            if fruta_existente.nombre.lower() == nombre_nuevo:
                print(f"⚠️ ERROR: La fruta '{nueva_fruta.nombre}' ya está en la cesta. No se agregó.")
                return 

        # 2. Si el bucle termina sin encontrar duplicados, se agrega la fruta
        self.frutas.append(nueva_fruta)
        print(f"✔️ {nueva_fruta.nombre} ha sido añadida a la cesta.") # Esta línea maneja la impresión de éxito
        
    def mostrar_cesta(self):
        for fruta in self.frutas:
            print(fruta.mostrar_info())
            
    def pedir_frutas_al_usuario(self):
        print("\n--- Introducción de Frutas ---")
        while True:
            nombre = input("Ingrese el nombre de la fruta (o 'salir' para terminar): ")
            if nombre.lower() == 'salir':
                print("Finalizando la entrada de frutas.")
                break
                
            tipo = input(f"Ingrese el tipo de {nombre}: ")
            
            try:
                precio = float(input(f"Ingrese el precio de {nombre}: "))
            except ValueError:
                print("❌ Precio inválido. Debe ser un número. Intente con esta fruta de nuevo.")
                continue # Vuelve al inicio del bucle while
                
            nueva_fruta = frutas(nombre, tipo, precio)
            
            # La llamada a 'agregar_fruta' ya maneja la impresión de éxito O error
            self.agregar_fruta(nueva_fruta)

# ----------------------------------------------------
# USO INTERACTIVO
# ----------------------------------------------------
mi_cesta_interactiva = cesta()
mi_cesta_interactiva.pedir_frutas_al_usuario()

print("\n" + "=" * 30)
print("RESUMEN DE LA CESTA:")
mi_cesta_interactiva.mostrar_cesta()


