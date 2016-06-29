#!/usr/bin/python3

from gi.repository import Gtk, GObject

# there are basically 2 modes of progress bar:
# 1) percentage mode - when you exactly know the fraction of the work done
# 2) activity mode - a block moves back and forth meaning there is no accurate way to knowing the amount of work

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Progress Bar")
		this.set_default_size(200,200)
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(10)

		vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		this.add(vbox)

		this.pg=Gtk.ProgressBar()  # making pg a class variable so that it can be used by all the member methods
		vbox.pack_start(this.pg, True, True,0) # by default the pg is horizontal and from left to right

		chk=Gtk.CheckButton("Show text")
		chk.connect("toggled",this.show_text_toggled)
		vbox.pack_start(chk, True, True, 0)

		chk=Gtk.CheckButton("Activity Mode")
		chk.connect("toggled",this.activity_mode_toggled)
		vbox.pack_start(chk, True, True, 0)
		
		chk=Gtk.CheckButton("Right to Left")
		chk.connect("toggled",this.r2l_toggled) # right 2 left
		vbox.pack_start(chk, True, True, 0)

		this.timeout_id=GObject.timeout_add(50, this.on_timeout, None)  # None - no user data is passed along
		this.acitivityMode=False  # varaible to know which mode we are operating in

	def show_text_toggled(this, widget):
		val=widget.get_active()

		if val:
			txt="Sample text"
		else:
			txt=None

		this.pg.set_text(txt)
		this.pg.set_show_text(val)

	def r2l_toggled(this, widget):
		val=widget.get_active()
		this.pg.set_inverted(val)

	def activity_mode_toggled(this, widget):
		this.acitivityMode=widget.get_active()

		if this.acitivityMode:
			this.pg.pulse()  # changing the mode to pulse rather than fraction
		else:
			this.pg.set_fraction(0.0)

	def on_timeout(this, user_data):
		# update the value of the progress data
		# Here the user data passed is None in the call above

		if this.acitivityMode:
			this.pg.pulse()
		else:
			val=this.pg.get_fraction() + 0.01
			if val>1:
				val=0
			this.pg.set_fraction(val)

		return True  # returning true so that the timeout function continues to get called

win=MyWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()




		
