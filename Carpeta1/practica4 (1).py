#Practica 4


class Ticket:
    def __init__(self, id, tipo, prioridad):  
        self.id = id
        self.tipo = tipo 
        self.prioridad = prioridad
        self.estado = "pendiente"

class empleado:
    def __init__(self, nombre):  
        self.nombre = nombre

    def trabajar_ticket(self, ticket):    
        print(f"El empleado {self.nombre} revisará un ticket {ticket.id}")

class desarrollador(empleado):
    def trabajar_ticket(self, ticket):
        if ticket.tipo.lower() == "software":   
            ticket.estado = "resuelto"          
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else: 
            print("Este tipo de empleado no puede resolver")

class projecrManager(empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"{self.nombre} asignó el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_ticket(ticket)


# crear ticket y empleado  (instancias de objetos)
ticket1 = Ticket(1, "Software", "Media")
ticket2 = Ticket(2, "Prueba", "Baja")

developer1 = desarrollador("Jessica Sodi")
tester1 = empleado("Adela danger")
pm1 = projecrManager("Mia Khalifa")

pm1.asignar_ticket(ticket1, developer1)
pm1.asignar_ticket(ticket2, tester1)


#parte adicional 
#agregar un menu con while y con if que permita 
#1. crear un ticket
#2. ver tickets
#3. asignar tickets
#4.salir del programa



tickets = []
developer1 = desarrollador("Renatha")
tester1 = empleado("Ximena")
pm1 = projecrManager("Victoria")

#  creacion del menú
while True:
    print("\n-- MENÚ --")
    print("1. Crear un ticket")
    print("2. Ver tickets")
    print("3. Asignar ticket")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Crear ticket
        id = int(input("ID del ticket: "))
        tipo = input("Tipo (Software/Prueba/etc): ")
        prioridad = input("Prioridad (Alta/Media/Baja): ")
        nuevo_ticket = Ticket(id, tipo, prioridad)
        tickets.append(nuevo_ticket)
        print(f"Ticket {id} creado con éxito.")

    elif opcion == "2":
        # Ver tickets
        if not tickets:
            print("No hay tickets registrados.")
        else:
            for t in tickets:
                print(f"ID: {t.id}, Tipo: {t.tipo}, Prioridad: {t.prioridad}, Estado: {t.estado}")

    elif opcion == "3":
        # Asignar ticket
        if not tickets:
            print("No hay tickets para asignar.")
        else:
            for t in tickets:
                print(f"ID: {t.id}, Tipo: {t.tipo}, Estado: {t.estado}")
            
            id_ticket = int(input("Ingresa el ID del ticket a asignar: "))
            encontrado = None
            for t in tickets:
                if t.id == id_ticket:
                    encontrado = t
                    break
            
            if encontrado:
                print("¿A quién deseas asignarlo?")
                print("1. Desarrollador (Renatha)")
                print("2. Tester (Ximena)")
                opcion_emp = input("Elige: ")
                if opcion_emp == "1":
                    pm1.asignar_ticket(encontrado, developer1)
                elif opcion_emp == "2":
                    pm1.asignar_ticket(encontrado, tester1)
                else:
                    print("Opción inválida.")
            else:
                print("Ticket no encontrado.")

    elif opcion == "4":
        print("Saliendo")
        break

    else:
        print("Opción inválida, intenta de nuevo.")