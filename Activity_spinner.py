#!/usr/bin/python3

from gi.repository import Gtk

# Spinners are also used to display indefinite activity, instead of actual progress

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Spinner")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_default_size(200,200)
		this.set_border_width(5)

		this.sp=Gtk.Spinner()
		this.bt=Gtk.ToggleButton(label="Start Spinning")
		this.bt.connect("toggled",this.spinning_toggled)
		this.bt.set_active(False)

		table = Gtk.Table(3, 2, True)
		table.attach(this.bt, 0, 2, 0, 1)
		table.attach(this.sp, 0, 2, 2, 3)

		this.connect("delete-event",Gtk.main_quit)
		this.add(table)
		this.show_all()  

	def spinning_toggled(this, widget):
		if widget.get_active():
			this.sp.start()  # start animation
			this.bt.set_label("Stop Spinning")
		else:
			this.sp.stop()  # stop animation
			this.bt.set_label("Start Spinning")
		

win=MyWindow()
Gtk.main()