#Programa de agregar contactos-Interfaz
#Manejo de archivos, parte KIM
class AgendaContactosArchivos(AgendaContactos):
    def _init_(self, archivo="contactos.txt"):
        super()._init_()  
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

    #guardarlos en el txt
    def agregar_contacto(self):
        super().agregar_contacto()
        self.guardar_contactos()

    def eliminar_contacto(self):
        super().eliminar_contacto()
        self.guardar_contactos()
