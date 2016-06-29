#!/usr/bin/python3

from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Different types of button")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(5)
		vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		this.add(vbox)

		sz=this.get_size()

		hbox=Gtk.Box(spacing=5)
		b=Gtk.ToggleButton("Toggle Button")
		b.connect("toggled",this.toggled,"1")
		l=Gtk.Label("active until pressed again. Emits \"toggled\" signal.",xalign=sz[1])	
		hbox.pack_start(b,False,False,0)
		hbox.pack_start(l,True,True,0)
		vbox.pack_start(hbox,True,True,0)
		
		hbox=Gtk.Box(spacing=5)
		b=Gtk.CheckButton("Check Button")
		b.connect("toggled",this.toggled,"2")
		l=Gtk.Label("Inherits from Gtk.ToggleButton. Only difference in appearance. Associated with a label usually.",xalign=sz[1])
		hbox.pack_start(b,False,False,0)
		hbox.pack_start(l,True,True,0)
		vbox.pack_start(hbox,True,True,0)
		
		hbox=Gtk.Box(spacing=5)
		b1=Gtk.RadioButton.new_with_label_from_widget(None,"R1") # first button has the group argument as None
		b1.connect("toggled",this.toggled,"3")
		b2=Gtk.RadioButton.new_from_widget(b1) # more buttons can be added to a group by the first button name
		b2.set_label("R2")
		b2.connect("toggled",this.toggled,"4")
		l=Gtk.Label("Inherits from Gtk.ToggleButton but work in groups. Only one of them can be active at a time.",xalign=sz[1])
						# Whenever the status of one is changed, all of them emit the toggled signal.
		hbox.pack_start(b1,False,False,0)
		hbox.pack_start(b2,False,False,0)
		hbox.pack_start(l,True,True,0)
		vbox.pack_start(hbox,True,True,0)
		
		hbox=Gtk.Box(spacing=5)
		b=Gtk.LinkButton("http://www.google.com","Visit Google") # remember without http:// this will not work
		b.connect("activate-link",this.link_activated)
		l=Gtk.Label("Gtk.Button with a hyperlink. Emits \"activate-link\" signal.",xalign=sz[1])
		hbox.pack_start(b,False,False,0)
		hbox.pack_start(l,True,True,0)
		vbox.pack_start(hbox,True,True,0)
		
		hbox=Gtk.Box(spacing=5)
		ad=Gtk.Adjustment(0,0,100,1,10,0) # (value, lower, upper, step_increment, page_increment, page size)
		this.b=Gtk.SpinButton()
		this.b.set_adjustment(ad)
		this.b.set_value(0)  # to get we can use get_value or get_value_as_int
		this.b.set_digits(2)  # floating point digit precision
		# The spin button. Properties set using Gtk.Adjustment. Emits multiple signals
		# Signals: value-changed, change-value, wrapped, input, output
		c1=Gtk.CheckButton("Numeric")
		c2=Gtk.CheckButton("IfValid")
		c1.connect("toggled",this.numeric_toggled)
		c2.connect("toggled",this.valid_toggled)
		l=Gtk.Label("Spin Button.",xalign=sz[1])
		hbox.pack_start(this.b,False,False,0)
		hbox.pack_start(c1,False,False,0)
		hbox.pack_start(c2,False,False,0)
		hbox.pack_start(l,True,True,0)
		vbox.pack_start(hbox,False,False,0)

		hbox=Gtk.Box(spacing=10)
		b1=Gtk.Switch()
		b2=Gtk.Switch()
		b1.connect("notify::active",this.switch_activated,"1") # avoid using the "active" signal; rather use "notify::	active"
		b2.connect("notify::active",this.switch_activated,"2") # because emitting active signal causes the switch to animate
		l=Gtk.Label("Switches.",xalign=sz[1])
		hbox.pack_start(b1,False,False,0)
		hbox.pack_start(b2,False,False,0)
		hbox.pack_start(l,True,True,0)
		vbox.pack_start(hbox,True,True,0)


	def toggled(this, button, num):
		status=button.get_active()  # returns true if the button is pressed
		print("Status of the toogle button {0}: {1}".format(num,status))

	def link_activated(this, widget):
		print("The link was activated")

	def numeric_toggled(this, button):
		this.b.set_numeric(button.get_active())

	def valid_toggled(this, button):
		if button.get_active():
			policy=Gtk.SpinButtonUpdatePolicy.IF_VALID
		else:
			policy=Gtk.SpinButtonUpdatePolicy.ALWAYS
		this.b.set_update_policy(policy)

	def switch_activated(this, button, gparam, num):  # note the extra gparam parameter
		if button.get_active():
			state="on"
		else:
			state="off"
		print("Switch {} was turned ".format(num)	,state)


win=MyWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()