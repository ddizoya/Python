
from gi.repository import Gtk

class Ventana():
    def __init__(self):
        fichero = "/datos/local/ddizoya/Desktop/prueba.glade"
        builder = Gtk.Builder()
        builder.add_from_file(fichero)

        self.panel = builder.get_object("panel")
        self.boton = builder.get_object("boton")
        self.texto = builder.get_object("texto")
        self.ventana = builder.get_object("ventana")

        signals = {
            "on_boton_clicked": self.on_boton_clicked,
            "on_ventana_destroy": Gtk.main_quit
        }

        builder.connect_signals(signals)

    def on_boton_clicked(self,control):
        texto = self.texto.get_text()
        self.panel.set_text("Hola",texto)


if __name__ == '__main__':
    Ventana()
    Gtk.main()


