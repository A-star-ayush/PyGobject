#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

def hello(widget):
	print("Hello World!")

handlers = {
	"OnDeleteWindow" : Gtk.main_quit,
	"OnButtonPressed" : hello
}

def main():
	builder = Gtk.Builder()
	builder.add_from_file("example.glade")
	builder.connect_signals(handlers)

	window = builder.get_object("window1")
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
