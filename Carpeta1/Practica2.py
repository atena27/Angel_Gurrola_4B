

# Practica 2. Atributos públicos y privados

class Persona:
    def __init__(self, nombre, edad):           
        self.nombre = nombre
        self.edad = edad
        self._cuenta = None  # Atributo privado

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Esta persona cumplió: {self.edad} años")

    def asignar_cuenta(self, cuenta):
        self._cuenta = cuenta
        print(f"{self.nombre} ahora tiene una cuenta bancaria")
     
    def consultar_saldo(self):
        if self._cuenta:
            print(f"El saldo de {self.nombre} es ${self._cuenta.mostrar_saldo()}")
        else:
            print(f"{self.nombre} aún no tiene cuenta bancaria")


class CuentaBancaria:
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self._saldo = saldo  # Atributo privado

    def mostrar_saldo(self):
        return self._saldo
   
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Se deposita la cantidad de ${cantidad} a la cuenta. Nuevo saldo: ${self._saldo}")
        else:
            print("Ingrese una cantidad válida")

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Se retira la cantidad de ${cantidad} de la cuenta. Nuevo saldo: ${self._saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida")


# Crear objetos
persona1 = Persona("Miguel", 20)
cuenta1 = CuentaBancaria("001", 500)

# Asignar cuenta y consultar saldo
persona1.asignar_cuenta(cuenta1)
persona1.consultar_saldo()

# Depositar dinero
cuenta1.depositar(200)

# Consultar nuevamente saldo
persona1.consultar_saldo()

# Acceder a los atributos públicos
print(persona1.nombre)
print(persona1.edad)

