__author__ = 'ddizoya'

from gi.repository import Gtk

class GridL (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Ejemplo Grid")
        grid = Gtk.Grid()
        self.add(grid)

        boton1 = Gtk.Button (label = "Buton1")
        boton2 = Gtk.Button (label = "Buton2")
        boton3 = Gtk.Button (label = "Buton3")
        boton4 = Gtk.Button (label = "Buton4")
        boton5 = Gtk.Button (label = "Buton5")
        boton6 = Gtk.Button (label = "Buton6")


        #attach(hijo, columna, fila, ancho, alto)
        grid.attach(boton1, 0, 0, 1, 1)
        grid.attach(boton2, 1, 0, 2, 1)
        grid.attach(boton3, 0, 1, 1, 2)
        grid.attach(boton4, 1, 1, 2, 1)
        grid.attach(boton5, 2, 1, 1, 1)
        grid.attach(boton6, 2, 2, 1, 1)




obj = GridL()
obj.connect("delete-event", Gtk.main_quit)
obj.show_all()
Gtk.main()