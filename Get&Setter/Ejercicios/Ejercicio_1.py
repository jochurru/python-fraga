"""
Ejercicio 1: Clase Persona con Nombre
Crea una clase Persona con una propiedad _nombre privada. Usa get para obtener el nombre y set para asignarlo, 
asegurándote de que el nombre no esté vacío.
"""
class Persona:
    def __init__(self, nombre_inicial):
        self._nombre = nombre_inicial
        if not nombre_inicial.strip():
            print("🚨 ERROR: El nombre no puede estar vacío.")
        if any(char.isdigit() for char in nombre_inicial):
            print("🚨 ERROR: El nombre no puede contener números.")
            return
        else:
            self._nombre = nombre_inicial


    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            print("🚨 ERROR: El nombre no puede estar vacío.")
        
        elif any(char.isdigit() for char in nuevo_nombre):
            print("🚨 ERROR: El nombre no puede contener números.")
        else:
            self._nombre = nuevo_nombre
            print(f"✔️ Nombre establecido a: {nuevo_nombre}")

# Uso del código
persona = Persona("Juan")
print(persona.nombre)  # Obtener el nombre inicial

persona.nombre = "Ana"  # Establecer un nuevo nombre válido
print(persona.nombre)  # Obtener el nombre actualizado
persona.nombre = "   "  # Intentar establecer un nombre vacío
print(persona.nombre)  # Verificar el nombre después del intento inválido

persona= Persona("123")
print(persona.nombre)  # Obtener el nombre inicial

