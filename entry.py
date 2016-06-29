#!/usr/bin/python3

from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this,title="Entry tests")
		this.set_default_size(350,200)
		this.set_position(Gtk.WindowPosition.CENTER)

		vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		this.add(vbox)

		e=Gtk.Entry(margin=15)
		e.set_text("Name")  # can work this way as a placeholder
		e.connect("activate",this.name_entered)
		vbox.pack_start(e,True,True,0)
		
		e=Gtk.Entry(margin=15)
		e.set_text("Age")  # can work this way as a placeholder
		e.set_max_length(3)  # setting the max input length
		e.connect("activate",this.age_entered)
		vbox.pack_start(e,True,True,0)
		
		e=Gtk.Entry(margin=15)
		e.set_text("Sex")  # can work this way as a placeholder
		e.connect("activate",this.sex_entered)
		vbox.pack_start(e,True,True,0)

		e=Gtk.Entry(margin=15)
		e.set_visibility(False)
		e.connect("activate",this.pass_entered)
		vbox.pack_start(e,True,True,0)

		e=Gtk.Entry(margin=15)
		e.set_editable(False)  # This makes it read-only
		e.set_can_focus(False)  # This causes the entry field to ignore any mouse click or tab sequence
		e.set_text('This text cannot be edited')
		vbox.pack_start(e,True,True,0)



	def name_entered(this,entry_widget):
		name=entry_widget.get_text() # getting the current text from the entry field
		print(name)
	
	def age_entered(this,entry_widget):
		age=entry_widget.get_text()  # remember get_text returns a string
		print("Your age ten years from now will be: {}".format((int(age)+10)))
	
	def sex_entered(this,entry_widget):
		sex=entry_widget.get_text()  
		if sex=="male" or sex=="Male":
			print("Genuine")
		elif sex=="female" or sex=="Female":
			print("Genuine")
		else:
			print("WTF")
	
	def pass_entered(this,entry_widget):
		password=entry_widget.get_text()
		print("Password: {}".format(password)) # although the visibility for the password entry field
				# is set to False but the input is still captured as a string - how else cud it make sense!

win=MyWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
