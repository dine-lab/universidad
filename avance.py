#Creamos el codigo genteee
#HOLA
import os
# Definimos la clase base AgendaContactos
class AgendaContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")

        contacto = {"nombre": nombre, "telefono": telefono}
        self.contactos.append(contacto)
        print(f"El Contacto {nombre} ha sido agregado correctamente.")

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre a buscar: ")
        encontrados = [contacto for contacto in self.contactos if nombre.lower() in contacto["nombre"].lower()]

        if encontrados:
            print("Contactos encontrados:")
            for contacto in encontrados:
                print(f"{contacto['nombre']} - {contacto['telefono']}")
        else:
            print("No se encontraron contactos con ese nombre.")

    def eliminar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        for contacto in self.contactos:
            if nombre.lower() == contacto["nombre"].lower():
                self.contactos.remove(contacto)
                print(f"El Contacto {nombre} ha sido eliminado correctamente.")
                return
        
        print("No se encontró el contacto para eliminar.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la lista.")
        else:
            print("\nLista de contactos:")
            for contacto in self.contactos:
                print(f"{contacto['nombre']} - {contacto['telefono']}")

    def show_menu(self):
        while True:
            print("\nMenú de contactos:")
            print("1. Agregar contacto.")
            print("2. Eliminar contacto.")
            print("3. Buscar contacto.")
            print("4. Mostrar contactos.")
            print("5. Salir.")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.eliminar_contacto()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.mostrar_contactos()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida, intente de nuevo.")

# Clase que extiende AgendaContactos para manejar archivos
class AgendaContactosArchivos(AgendaContactos):
    def __init__(self, archivo="contactos.txt"):
        super().__init__()  
        self.archivo = archivo
        self.cargar_contactos()

    def guardar_contactos(self):
        """Guarda los contactos en un archivo de texto."""
        with open(self.archivo, "w") as f:
            for contacto in self.contactos:
                f.write(f"{contacto['nombre']},{contacto['telefono']}\n")

    def cargar_contactos(self):
        """Carga los contactos desde un archivo de texto."""
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                for linea in f:
                    nombre, telefono = linea.strip().split(",")
                    self.contactos.append({"nombre": nombre, "telefono": telefono})

    def agregar_contacto(self):
        super().agregar_contacto()
        self.guardar_contactos()

    def eliminar_contacto(self):
        super().eliminar_contacto()
        self.guardar_contactos()

# Ejecución del programa
if __name__ == "__main__":
    agenda = AgendaContactosArchivos()
    agenda.show_menu()