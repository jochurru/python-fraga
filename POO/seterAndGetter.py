class Coche:
    def __init__(self, velocidad_inicial):
        self._velocidad = velocidad_inicial

    @property
    def velocidad(self):
        return (f"La velocidad actual es: {self._velocidad} km/h")
    
    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        #A Validacion del limite inferior
        if nueva_velocidad < 0:
            print("🚨 ERROR: La velocidad no puede ser negativa. ¡Frenando a 0!")
            self._velocidad_actual = 0  # Asignamos un valor seguro
        # B) VALIDACIÓN DE LÍMITE SUPERIOR
        elif nueva_velocidad > 250:
            print("🛑 AVISO: Velocidad peligrosa. ¡Limitando a 250 km/h!")
            self._velocidad_actual = 250 # Asignamos un valor seguro
        else:
            self._velocidad = nueva_velocidad
            print(f"✔️ Velocidad establecida a {nueva_velocidad} km/h.")

#Uso del codigo
mi_coche = Coche(100)
print(mi_coche.velocidad)  # Obtener la velocidad inicial
mi_coche.velocidad = 180  # Establecer una nueva velocidad válida
print(mi_coche.velocidad)  # Obtener la velocidad actualizada
mi_coche.velocidad = -50  # Intentar establecer una velocidad negativa
print(mi_coche.velocidad)  # Verificar la velocidad después del intento inválido
mi_coche.velocidad = 300  # Intentar establecer una velocidad excesiva
print(mi_coche.velocidad)  # Verificar la velocidad después del intento inválido
