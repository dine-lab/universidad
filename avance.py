#Programa de agregar contactos-Interfaz
class ContacApp:
    def _init_(self):
        self.contactos = []

    def show_menu(self):
        while True:
            print("\n Menu de contactos:")
            print("1. Agregar contacto.")
            print("2. Eliminar contacto.")
            print("3. Buscar contacto.")
            print("4. Mostrar contactos.")
            print("5. Salir.")
            opcion=input("Seleccione una opción: ")
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
                print("Opción invalida, intente de nuevo")
