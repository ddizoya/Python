#!/usr/bin/python
from gi.repository import Gtk

class ExemploBoxGTK(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title = "Ejemplo de box.")
        self.caixa = Gtk.Box (spacing = 10)
        self.caixa.set_visible(True)
        self.caixa.set_orientation(Gtk.Orientation.VERTICAL) #Poner la caja con orientacin vertical
        self.add(self.caixa)
        self.set_visible(True)
        self.set_resizable(False)


        self.boton1 = Gtk.Button(label = "Hola")
        self.boton1.connect ("clicked", self.on_boton1_clicked)
        self.boton1.set_visible(True)
        self.caixa.pack_end(self.boton1, True, True, 3)


        self.boton2 = Gtk.Button (label = "Adeus")
        self.boton2.connect("clicked",self.on_boton2_clicked)
        self.boton2.set_visible(True)
        self.caixa.pack_end (self.boton2, True, True, 3)

        self.etiqueta = Gtk.Label("")
        self.caixa.pack_end (self.etiqueta, True, True, 3)
        self.etiqueta.set_visible(True)



    def on_boton1_clicked(self, control):
        self.etiqueta.set_text("Hola")

    def on_boton2_clicked(self, control):
        self.etiqueta.set_text("Adeus")


ventana = ExemploBoxGTK()
ventana.connect("delete-event", Gtk.main_quit)
ventana.show_all
Gtk.main()


