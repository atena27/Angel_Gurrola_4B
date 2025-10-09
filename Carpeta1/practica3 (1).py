# Práctica 3: Introducción de Polimorfismo

class PagoTarjeta:
    def procesar_pago(self, cantidad):
        return f"Procesado pago de ${cantidad} con tarjeta"

class Transferencia: 
    def procesar_pago(self, cantidad):
        return f"Procesado pago de ${cantidad} por medio de transferencia"

class Paypal:
    def procesar_pago(self, cantidad):
        return f"Procesado pago de ${cantidad} por medio de PayPal"

class Deposito:
    def procesar_pago(self, cantidad):
        return f"Procesado pago de ${cantidad} por medio de depósito en ventanilla"

# Instancias con diferentes métodos de pago
metodos_pago = [
    PagoTarjeta(),
    Transferencia(),
    Paypal(),
    Deposito()
]

# Ejemplo de cantidades diferentes
cantidades = [100, 500, 20000, 400]

# Polimorfismo en acción
for metodo, cantidad in zip(metodos_pago, cantidades):
    print(metodo.procesar_pago(cantidad))

#Notificaciones
def notificacion(app, mensaje):
    print(f"[{app}] {mensaje}")


print("\n Notificaciones ")
notificacion("Facebook", "Juan te envió un mensaje.")
notificacion("Instagram", "Ana comentó tu foto")
notificacion("Tinder", "¡Tienes un match con María!")
notificacion("WhatsApp", "Nuevo mensaje en el grupoS")
notificacion("YouTube", "Tu canal favorito subió un nuevo video.")
