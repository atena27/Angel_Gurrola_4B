#Practica 5. Patrones de diseñon

class Logger:
    _instancia = None  # Atributo de clase para guardar la única instancia

    def __new__(cls, *args, **kwargs):
        # Validar si existe o no la instancia
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)  # Creamos la instancia de Logger
            # Agregamos un atributo llamado archivo que apunta a un archivo físico
            # "a" significa append = todo lo que se escriba se agrega al final del archivo
            cls._instancia.archivo = open("app.log", "a")
        return cls._instancia  # Devolver siempre la misma instancia

    def log(self, mensaje):
        self.archivo.write(mensaje + "\n")  # Agregamos salto de línea para legibilidad
        self.archivo.flush()  # Guardar en disco inmediatamente


# Uso del Singleton
Logger1 = Logger()  # Creamos la primera (y única) instancia
Logger2 = Logger()  # Devuelve la misma instancia, no crea otra

Logger1.log("Inicio de sesión en la aplicación")
Logger2.log("El usuario se autenticó")

# Comprobar que son el mismo objeto en memoria
print(Logger1 is Logger2)  # Devuelve True

#Actividad de la practica


class Presidente:
    _instancia = None

    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.nombre = nombre
            cls._instancia.historial = []
        return cls._instancia
    
    def accion(self, accion):
        evento = f"{self.nombre} {accion}"
        self.historial.append(evento)
        print(evento)

#Varios presidentes intentan tomar el poder
p1 = Presidente("AMLO")
p2 = Presidente("Peña Nieto")
p3 = Presidente("FOX")

p1.accion("firmo deccreto")
p2.accion("Visito España")
p3.accion("aprobo un presupuesto")

print("\nHistorial del presidente:")
print(p1.historial)

#Validacion singleton 
print(p1 is p2 is p3) #true o false


