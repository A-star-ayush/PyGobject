#!/usr/bin/python3

from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="TEST")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(10)
		this.set_default_size(200,200)
		green=Gdk.Color(0x0000, 0xffff, 0x0000)
		red=Gdk.Color(0xffff, 0x0000, 0x0000)
		this.modify_bg(0, green) # First argument is the state
		this.modify_fg(0, red)
		l = Gtk.Label("Hello")
		this.add(l)

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
