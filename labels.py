#!/usr/bin/python3

from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this,title="Label testing")
		this.set_default_size(300,300)
		this.set_border_width(5)
		this.set_position(Gtk.WindowPosition.CENTER)

		vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		this.add(vbox)

		l=Gtk.Label()
		l.set_text("Simple text")
		vbox.pack_start(l,True,True,0)

		l=Gtk.Label()
		l.set_markup("<b>Markup</b> <i>style</i>")  # follows pango text markup language
		vbox.pack_start(l,True,True,0)

		l=Gtk.Label()
		l.set_markup("Click <a href=\"http://www.google.com\">here</a> for more")
		vbox.pack_start(l,True,True,0)
		
		l=Gtk.Label(xalign=0)
		l.set_text("This text is aligned to the left.")
		vbox.pack_start(l,True,True,0)

		l=Gtk.Label()
		l.set_text("Line1 \nLine2")
		vbox.pack_start(l,True,True,0)

		l=Gtk.Label(selectable=True)
		l.set_markup("The contents can be copied to the clipboard")
		vbox.pack_start(l,True,True,0)

		b=Gtk.Button(label="Click Here")
		l=Gtk.Label()
		l.set_text_with_mnemonic("\"Alt+_q to activate the button\"")  # mnemonics work like accelerators in QT
		l.set_mnemonic_widget(b) # the mnemonic react to the widget specified here # they are set using _ instead of &
		vbox.pack_start(l,True,True,0)
		vbox.pack_start(b,True,True,0)
		

win=MyWindow()
win.show_all()
win.connect("delete-event",Gtk.main_quit)
Gtk.main()
		