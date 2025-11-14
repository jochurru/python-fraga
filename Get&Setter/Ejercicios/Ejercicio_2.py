"""
Crear una clase CuentaBancaria con los atributos:
titular
saldo

"""
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        # 1. Llamamos al setter del titular para aplicar la validación inicial.
        # Si la validación falla, lanzará ValueError (usando la lógica de 'hasattr').
        self.titular = titular 
        
        # 2. Llamamos al setter del saldo para aplicar la validación inicial.
        self.saldo = saldo_inicial
        
        # 3. Solo imprimimos el mensaje de éxito de creación después de ambas validaciones.
        print(f"✔️ Cuenta creada para {self._titular} con saldo inicial de ${self._saldo:.2f}")

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, nuevo_titular):
        # Limpiamos los espacios en blanco
        nuevo_titular_limpio = nuevo_titular.strip()
        
        # Almacenamos el valor anterior antes de la reasignación
        previous = getattr(self, '_titular', None)
        
        if not nuevo_titular_limpio:
            if not hasattr(self, '_titular'):
                raise ValueError("🚨 ERROR (INIT): El nombre del titular no puede estar vacío.")
            print("🚨 ERROR: El nombre del titular no puede estar vacío. No se ha modificado.")
            
        elif any(char.isdigit() for char in nuevo_titular_limpio):
            if not hasattr(self, '_titular'):
                raise ValueError("🚨 ERROR (INIT): El nombre del titular no puede contener números.")
            print("🚨 ERROR: El nombre del titular no puede contener números. No se ha modificado.")
            
        else:
            self._titular = nuevo_titular_limpio
            # Imprimimos el mensaje de cambio solo si el titular es diferente al anterior (y no es la inicialización fallida)
            if previous != nuevo_titular_limpio and previous is not None:
                print(f"✔️ Titular establecido a: {nuevo_titular_limpio}")
            # NOTA: En la inicialización, 'previous' es None, por lo que este mensaje no se imprime, evitando duplicidad con el __init__.

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        # Almacenamos el valor anterior antes de la reasignación
        previous_saldo = getattr(self, '_saldo', None)
        
        if nuevo_saldo < 0:
            if not hasattr(self, '_saldo'): 
                raise ValueError("🚨 ERROR (INIT): El saldo no puede ser negativo.")
            print("🚨 ERROR: El saldo no puede ser negativo. No se ha modificado.")
        else:
            self._saldo = nuevo_saldo
            # Imprimimos el mensaje de cambio solo si el saldo es diferente al anterior y no es la primera asignación
            if previous_saldo != nuevo_saldo and previous_saldo is not None:
                print(f"✔️ Saldo actualizado a: ${nuevo_saldo:.2f}")
            # NOTA: En la inicialización, 'previous_saldo' es None, por lo que este mensaje no se imprime.

# Uso del codigo

print("--- Prueba de Codigo CuentaBancaria ---")
cuenta = CuentaBancaria("Carlos Gomez", 1000)
print(f"Cuenta titular actual: {cuenta.titular}")
print(f"Cuenta saldo actual: ${cuenta.saldo:.2f}")

# Reasignación de titular
cuenta.titular = "Ana Martinez"
print(f"Cuenta titular actualizado a: {cuenta.titular}")

# Reasignación inválida (se aplica la validación)
print("\n--- PRUEBA DE REASIGNACIÓN INVÁLIDA ---")
cuenta.titular = " " 
print(f"Titular después de intento fallido: {cuenta.titular}") # Debe seguir siendo "Ana Martinez"

cuenta.saldo = -500 
print(f"Saldo después de intento fallido: {cuenta.saldo}") # Debe seguir siendo $1000.00

# Inicialización inválida (lanza excepción y detiene la creación)
print("\n--- PRUEBA DE INICIALIZACIÓN INVÁLIDA ---")
try:
    CuentaBancaria("456", 2000)
except ValueError as e:
    print(e)