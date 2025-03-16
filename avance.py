#Creamos el codigo genteee
#HOLA
class AgendaContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input(" Ingrese el nombre del contacto: ")
        telefono = input(" Ingrese el número de teléfono: ")

        contacto = {"nombre": nombre, "telefono": telefono}
        self.contactos.append(contacto)
        print(f"El Contacto {nombre} ha sido agregado correctamente.")

    def buscar_contacto(self):
        nombre = input(" Ingrese el nombre a buscar: ")
        encontrados = []

        for contacto in self.contactos:
            if nombre.lower() in contacto["nombre"].lower():
                encontrados.append(contacto)

        if len(encontrados) > 0:
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

agenda = AgendaContactos()