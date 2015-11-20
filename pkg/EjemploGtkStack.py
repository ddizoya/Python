from inspect import stack

__author__ = 'ddizoya'
from gi.repository import Gtk

class EjemploGtkStack(Gtk.Window):
    def __init__(self):

        Gtk.Window.__init__(self, title = "Ejemplo Stack")
        self.set_border_width(10)

        cajaV = Gtk.Box(Gtk.Orientation.VERTICAL, spacing = 6)
        self. add(cajaV)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.OVER_UP_DOWN)
        stack.set_transition_duration(1000)

        btnChequeo = Gtk.CheckButton("?Pulsame!")
        stack.add_titled(btnChequeo, "Pulsa", "Boton de chequeo")

        label = Gtk.Label()
        label.set_markup("<big>Una etiqueta</big>")
        stack.add_titled(label, "Etiqueta", "Una etiqueta")

        conmutadorStack = Gtk.StackSwitcher()
        conmutadorStack.set_stack(stack)

        cajaV.pack_start(conmutadorStack, True, True, 0)
        cajaV.pack_start(stack, True, True, 0)


obj = EjemploGtkStack()
obj.show_all()
Gtk.main()