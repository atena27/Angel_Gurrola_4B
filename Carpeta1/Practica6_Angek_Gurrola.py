
from datetime import date, timedelta

# 1. CLASE LIBRO 
class Libro:
    """Representa un recurso bibliográfico."""
    def __init__(self, titulo, autor, anio, codigo):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.codigo = codigo # ID único del libro
        self.disponible = True # Estado inicial: disponible

    def mostrar_info(self):
        """Muestra los detalles del libro y su estado de disponibilidad."""
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"| Libro: {self.titulo} (Cód: {self.codigo})")
        print(f"| Autor: {self.autor}, Año: {self.anio}")
        print(f"| Estado: {estado}")

    def marcar_como_prestado(self):
        """Cambia el estado del libro a no disponible."""
        if self.disponible:
            self.disponible = False
            return True
        else:
            print(f"*** ERROR: El libro '{self.titulo}' ya está prestado. ***")
            return False

    def marcar_como_disponible(self):
        "Cambia el estado del libro a disponible."
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido marcado como DISPONIBLE.")


# 2. CLASES USUARIO (Padre), ESTUDIANTE y PROFESOR (Subclases) 

class Usuario:
    """Clase base para cualquier persona que usa la biblioteca."""
    def __init__(self, nombre, id_usuario, correo):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo
        self.prestamos_activos = []

    def mostrar_info(self):
        """Método base para mostrar la información del usuario."""
        print(f"\n--- USUARIO BÁSICO ---")
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id_usuario}")
        print(f"Correo: {self.correo}")

    def solicitar_prestamo(self, libro, dias=7):
        "Simula la solicitud de un préstamo, creando un objeto Préstamo."
        if libro.disponible:
            # Crea un nuevo objeto Préstamo
            nuevo_prestamo = Prestamo(libro, self)
            
            # Intenta marcar el libro como prestado
            if libro.marcar_como_prestado():
                self.prestamos_activos.append(nuevo_prestamo)
                
                # Calcula la fecha de devolución (hoy + días)
                fecha_devolucion = date.today() + timedelta(days=dias)
                
                nuevo_prestamo.registrar_prestamo(fecha_devolucion)
                print(f"Solicitud ACEPTADA para {self.nombre}.")
                return nuevo_prestamo
            else:
                return None
        else:
            print(f"Solicitud RECHAZADA: '{libro.titulo}' no está disponible.")
            return None

class Estudiante(Usuario):
    """Subclase de Usuario con atributos específicos de estudiante."""
    def __init__(self, nombre, id_usuario, correo, carrera, semestre):
        super().__init__(nombre, id_usuario, correo)
        self.carrera = carrera
        self.semestre = semestre

    # POLIMORFISMO: Sobrescribe el método del padre
    def mostrar_info(self):
        ""Muestra la información específica del estudiante."
        print(f"\n-ESTUDIANTE- ")
        print(f"Nombre: {self.nombre} (ID: {self.id_usuario})")
        print(f"Correo: {self.correo}")
        print(f"Detalles: {self.carrera} - Semestre {self.semestre}")
        print(f"Préstamos Activos: {len(self.prestamos_activos)}")

class Profesor(Usuario):
    "Subclase de Usuario con atributos específicos de profesor."
    def __init__(self, nombre, id_usuario, correo, departamento, tipo_contrato):
        super().__init__(nombre, id_usuario, correo)
        self.departamento = departamento
        self.tipo_contrato = tipo_contrato

    # POLIMORFISMO: Sobrescribe el método del padre
    def mostrar_info(self):
        """Muestra la información específica del profesor."""
        print(f"\n- PROFESOR -")
        print(f"Nombre: {self.nombre} (ID: {self.id_usuario})")
        print(f"Departamento: {self.departamento}")
        print(f"Tipo de Contrato: {self.tipo_contrato}")
        print(f"Préstamos Activos: {len(self.prestamos_activos)}")


# 3. CLASE PRÉSTAMO 

class Prestamo:
    """Representa la transacción de un libro prestado a un usuario."""
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = None
        self.fecha_devolucion = None

    def registrar_prestamo(self, fecha_limite):
        """Registra la fecha del préstamo y la fecha límite de devolución."""
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = fecha_limite
        print(f"  > Libro: '{self.libro.titulo}' prestado a {self.usuario.nombre}.")
        print(f"  > Fecha de Préstamo: {self.fecha_prestamo}")
        print(f"  > Fecha Límite de Devolución: {self.fecha_devolucion}")
    
    def devolver_libro(self):
        """Procesa la devolución y actualiza el estado del libro y del usuario."""
        if self.libro.disponible:
            # En un sistema real, esto no debería ocurrir, pero es una comprobación de seguridad.
            print(f"El préstamo de '{self.libro.titulo}' ya estaba marcado como devuelto/disponible.")
            return

        print(f"\n- PROCESANDO DEVOLUCIÓN -")
        print(f"Usuario: {self.usuario.nombre} | Libro: {self.libro.titulo}")
        
        self.libro.marcar_como_disponible()
        
        # Eliminar el préstamo de la lista de préstamos activos del usuario
        if self in self.usuario.prestamos_activos:
            self.usuario.prestamos_activos.remove(self)
        
        print("Devolución completada con éxito.")


# 4. SIMULACIÓN DEL SISTEMA 
print("="*60)
print("       SIMULACIÓN DEL SISTEMA DE PRÉSTAMOS DE BIBLIOTECA")
print("="*60)

## 4.1 Creación de Objetos

# Libros (al menos dos)
libro1 = Libro("Cien años de soledad", "Gabo", 1967, "L-001")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "L-002")
libro3 = Libro("Diseño de Algoritmos", "Cormen et al.", 2009, "L-003")

print("\n--- INFORMACIÓN INICIAL DE LIBROS ---")
libro1.mostrar_info()
libro2.mostrar_info()
print("-" * 30)

# Usuarios (al menos dos de cada subclase)
estudiante1 = Estudiante("Ana López", "U1001", "ana.l@uni.edu", "Ingeniería de Sistemas", "5to")
estudiante2 = Estudiante("Juan Pérez", "U1002", "juan.p@uni.edu", "Derecho", "3ro")

profesor1 = Profesor("Dr. Carlos Ruiz", "P2001", "c.ruiz@uni.edu", "Matemáticas", "Tiempo Completo")
profesor2 = Profesor("Mtra. Elena Gómez", "P2002", "e.gomez@uni.edu", "Literatura", "Medio Tiempo")


## 4.2 Demostración de Polimorfismo
print("\n" + "="*20 + " DEMOSTRACIÓN DE POLIMORFISMO " + "="*20)
# Llamando al mismo método 'mostrar_info' en diferentes tipos de objetos.
estudiante1.mostrar_info()
profesor1.mostrar_info()


## 4.3 Simulación de Préstamos

print("\n" + "="*20 + " SIMULACIÓN DE PRÉSTAMOS " + "="*20)

# 1. Préstamo exitoso (Profesor presta libro1)
prestamo_p1 = profesor1.solicitar_prestamo(libro1, dias=15)

# 2. Intento de préstamo fallido (libro1 ya está prestado)
profesor2.solicitar_prestamo(libro1)

# 3. Préstamo exitoso (Estudiante presta libro3)
prestamo_e1 = estudiante1.solicitar_prestamo(libro3)

# 4. Mostrar el estado de los objetos después de los préstamos
print("\n--- ESTADO DESPUÉS DE LOS PRÉSTAMOS ---")
libro1.mostrar_info()
libro3.mostrar_info()
estudiante1.mostrar_info()
profesor1.mostrar_info()

## 4.4 Simulación de Devolución
print("\n" + "="*20 + " SIMULACIÓN DE DEVOLUCIÓN " + "="*20)

# El profesor devuelve el libro1
if prestamo_p1:
    prestamo_p1.devolver_libro()

# Mostrar el estado final del libro y del usuario
print("\n--- ESTADO FINAL DESPUÉS DE DEVOLUCIÓN ---")
libro1.mostrar_info()
profesor1.mostrar_info()