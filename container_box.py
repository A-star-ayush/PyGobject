#!/usr/bin/python3

from gi.repository import Gtk

### Using the Box Container ###

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this,title="Hello")
		this.box=Gtk.Box(spacing=5)  # creating a horizontal layout with spacing of 5 btw its children
		
		this.button1=Gtk.Button(label="Hello")
		this.button2=Gtk.Button(label="GoodBye")
		this.button3=Gtk.Button(label="Both")
		
		this.button1.connect("clicked",this.print_hello)  # the this pointer is absolutely neccessary in this case
		this.button2.connect("clicked",this.print_bye)
		this.button3.connect("clicked",this.print_hello)  # button 3 connects to both print functions
		this.button3.connect("clicked",this.print_bye)      # so both of them are called when button3 is clicked

		this.box.pack_start(this.button1,True,True,0)  # pack_end would insert from the other end
		this.box.pack_start(this.button2,True,True,0)
		this.box.pack_start(this.button3,True,True,0)

		this.add(this.box)
	def print_hello(this,widget):
		print("Hello")
	def print_bye(this,widget):
		print("GoodBye!")

win=MyWindow()
win.connect("delete-event",Gtk.main_quit)
win.set_default_size(500,200);   
win.set_position(Gtk.WindowPosition.CENTER)  # cause the application to appear at the centre of the screen
win.show_all()
Gtk.main()

