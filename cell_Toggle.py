#!/usr/bin/python3

from gi.repository import Gtk

# As a Gtk.CellRendererToggle can have two states, active and not active, you most likely want to bind the
# "active" property on the cell renderer to a "boolean" value in the model, thus causing the check button to 
# reflect the state of the model.

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Cell Renderer Toggle")
		this.set_position(Gtk.WindowPosition.CENTER)

		this.model = Gtk.ListStore(str, bool, bool)  # Note the use of the boolean values in the model
		this.model.append(["Action", True, False])
		this.model.append(["Romantic", False, False])
		this.model.append(["Mystery", True, True])

		view = Gtk.TreeView(this.model)
		this.add(view)

		rend_text = Gtk.CellRendererText()
		col0 = Gtk.TreeViewColumn("Genre", rend_text, text=0)

		rend_toggle = Gtk.CellRendererToggle()
		rend_toggle.connect("toggled", this.on_check_toggled)
		col1 = Gtk.TreeViewColumn("Check Button", rend_toggle, active=1) # here 1 refers to the model col no
														# that contains the controlling boolean values
		rend_toggle2 = Gtk.CellRendererToggle()
		rend_toggle2.set_radio(1)  # This property actually gives it its radio button [default is check button]
		rend_toggle2.connect("toggled", this.on_radio_toggled)
		col2 = Gtk.TreeViewColumn("Radio Button", rend_toggle2, active=2)

		view.append_column(col0)
		view.append_column(col1)
		view.append_column(col2)

	def on_check_toggled(this, widget, path):
		this.model[path][1] = not this.model[path][1]  # Note the way to negate in python

	def on_radio_toggled(this, widget, path):
		selected_path = Gtk.TreePath(path)
		for row in this.model:
			row[2] = (row.path == selected_path)
	# We do things differently for the radio buttons so that they retain their property that only one of them
	# is active at a time
	
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()