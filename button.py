#!/usr/bin/python3

from gi.repository import Gtk

# The Gtk widget can hold any valid Gtk.Widget

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this,title="Button test")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(10)

		vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)
		this.add(vbox)
		hbox=Gtk.Box(spacing=5)
		b=Gtk.Button("Click Me")
		b.connect("clicked",this.clicked_click_me)
		hbox.pack_start(b,True,True,0)

		b=Gtk.Button("Open")
		b.connect("clicked",this.clicked_open)
		hbox.pack_start(b,True,True,0)

		b=Gtk.Button("Close")
		b.connect("clicked",this.clicked_close)
		hbox.pack_start(b,True,True,0)

		vbox.pack_start(hbox,True,True,0)
		this.l=Gtk.Label("Hi there")
		vbox.pack_start(this.l,True,True,0)

	def clicked_click_me(this, button):
		this.l.set_label("Thanks for clicking it")
	
	def clicked_open(this, button):
		this.l.set_label("Haven't got anything to open")
	
	def clicked_close(this, button):
		this.l.set_label("That's not happening")

win=MyWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()

