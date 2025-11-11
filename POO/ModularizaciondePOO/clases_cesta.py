class frutas:
    def __init__(self, nombre, tipo, precio):
        # Estandarización: Guardar nombre y tipo con la primera letra en mayúscula
        self.nombre = nombre.strip().capitalize() 
        self.tipo = tipo.strip().capitalize()
        self.precio = precio
    
    def mostrar_info(self):
        return f"Fruta: {self.nombre}, Tipo: {self.tipo}, Precio: ${self.precio:.2f}"
    

class cesta:
    def __init__(self):
        self.frutas = []
        
    def agregar_fruta(self, nueva_fruta):
        """
        Agrega una fruta, solo si no existe el par (Nombre + Tipo) en la lista.
        """
        nombre_nuevo = nueva_fruta.nombre.lower() 
        tipo_nuevo = nueva_fruta.tipo.lower()
        
        # Recorre la lista para verificar la unicidad compuesta (Nombre Y Tipo)
        for fruta_existente in self.frutas:
            n_existente = fruta_existente.nombre.lower()
            t_existente = fruta_existente.tipo.lower()
            
            if n_existente == nombre_nuevo and t_existente == tipo_nuevo:
                print(f"⚠️ ERROR: La fruta '{nueva_fruta.nombre}' tipo '{nueva_fruta.tipo}' ya está en la cesta. No se agregó.")
                return 

        # Si no hay duplicados, se agrega la fruta
        self.frutas.append(nueva_fruta)
        print(f"✔️ {nueva_fruta.nombre} ({nueva_fruta.tipo}) ha sido añadida a la cesta.")
    
    def eliminar_fruta(self, nombre_fruta):
        nombre_fruta = nombre_fruta.lower()
        
        # Buscar y eliminar la fruta por nombre
        for fruta in self.frutas:
            if fruta.nombre.lower() == nombre_fruta:
                self.frutas.remove(fruta)
                print(f"🗑️ {fruta.nombre} ha sido eliminada de la cesta.")
                return
                
        print(f"⚠️ La fruta '{nombre_fruta.capitalize()}' no se encontró en la cesta.")
        
    def mostrar_cesta(self):
        print("\n--- DETALLE DE LA CESTA ---")
        if not self.frutas:
            print("La cesta está vacía.")
            return
            
        for fruta in self.frutas:
            print(fruta.mostrar_info())
            
    def pedir_frutas_al_usuario(self):
        print("\n--- Introducción de Frutas ---")
        while True:
            # 1. VALIDACIÓN DE NOMBRE
            nombre_input = input("Ingrese el nombre de la fruta (o 'salir' para terminar): ").strip()
            
            if nombre_input.lower() == 'salir':
                print("Finalizando la entrada de frutas.")
                break
                
            if not nombre_input:
                print("❌ El nombre de la fruta no puede estar vacío. Intente de nuevo.")
                continue

            # 2. VALIDACIÓN DE TIPO (Bucle anidado para reintento)
            while True:
                tipo_input = input(f"Ingrese el tipo de {nombre_input}: ").strip()
                if not tipo_input:
                    print("❌ El tipo de fruta no puede estar vacío. Intente de nuevo.")
                else:
                    break 

            # 3. VALIDACIÓN DE PRECIO
            try:
                precio = float(input(f"Ingrese el precio de {nombre_input}: "))
            except ValueError:
                print("❌ Precio inválido. Debe ser un número. Intente con esta fruta de nuevo.")
                continue
                
            # Creación y adición (la clase frutas estandariza el texto)
            nueva_fruta = frutas(nombre_input, tipo_input, precio)
            self.agregar_fruta(nueva_fruta)
            
    def eliminar_fruta(self, nombre_fruta, indice_a_eliminar=None):
        nombre_fruta_lower = nombre_fruta.lower()
        
        # 1. Encontrar todas las frutas que coinciden con el nombre
        coincidencias = []
        for i, fruta in enumerate(self.frutas):
            if fruta.nombre.lower() == nombre_fruta_lower:
                coincidencias.append((i, fruta))

        if not coincidencias:
            print(f"⚠️ La fruta '{nombre_fruta.capitalize()}' no se encontró en la cesta.")
            return

        # 2. Si hay múltiples coincidencias, y no se especificó un índice, 
        #    devolvemos la lista para que el método interactivo elija.
        if len(coincidencias) > 1 and indice_a_eliminar is None:
            return coincidencias  # Devolvemos las opciones al método interactivo

        # 3. Eliminar la fruta: Si solo hay una coincidencia O el índice fue proporcionado
        
        # Obtener el índice real de la fruta a eliminar
        if indice_a_eliminar is not None:
            # Si el índice viene del menú, lo usamos
            indice_real = indice_a_eliminar
        else:
            # Si solo hay una coincidencia, usamos ese índice
            indice_real = coincidencias[0][0]
        
        fruta_eliminada = self.frutas.pop(indice_real)
        print(f"🗑️ {fruta_eliminada.nombre} ({fruta_eliminada.tipo}) ha sido eliminada de la cesta.")
        return True # Indicador de éxito

    
    def eliminar_frutas_al_usuario(self):
        print("\n--- Eliminación de Frutas ---")
        while True:
            nombre = input("Ingrese el nombre de la fruta a eliminar (o 'salir' para terminar): ").strip()
            
            if nombre.lower() == 'salir':
                print("Finalizando la eliminación de frutas.")
                break
            
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                continue

            # Llamamos a eliminar_fruta. Puede devolver True (eliminado), None (no encontrado) 
            # o la lista de opciones [(indice, fruta), ...] si hay ambigüedad.
            resultado = self.eliminar_fruta(nombre)
            
            # --- Manejo de ambigüedad (El problema que reportaste) ---
            if isinstance(resultado, list):
                print(f"\nSe encontraron múltiples tipos de '{nombre.capitalize()}':")
                for i, (indice_cesta, fruta) in enumerate(resultado):
                    print(f"  {i+1}. Tipo: {fruta.tipo}, Precio: ${fruta.precio:.2f}")

                while True:
                    try:
                        opcion = input("Elige el número del tipo a eliminar (o 0 para cancelar): ")
                        opcion_int = int(opcion)
                        
                        if opcion_int == 0:
                            print("Eliminación cancelada.")
                            break
                        
                        # El índice real de la fruta a eliminar en self.frutas
                        indice_a_eliminar = resultado[opcion_int - 1][0] 
                        
                        # Llamamos de nuevo a eliminar_fruta con el índice específico
                        self.eliminar_fruta(nombre, indice_a_eliminar)
                        break
                        
                    except (ValueError, IndexError):
                        print("❌ Opción inválida. Intente de nuevo.")
            
    def calcular_total(self):
        total = sum(fruta.precio for fruta in self.frutas)
        return total