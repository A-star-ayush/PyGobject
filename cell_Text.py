#!/usr/bin/python3

from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Cell Renderer Text")
		this.set_position(Gtk.WindowPosition.CENTER)

		this.model = Gtk.ListStore(str, str)
		this.model.append(["    Uneditable Text     ", "       Editable Text     "])
		
		rend_txt0 = Gtk.CellRendererText()
		col0 = Gtk.TreeViewColumn("Col0", rend_txt0, text=0)

		view = Gtk.TreeView(this.model)
		view.append_column(col0)

		this.add(view)

		rend_txt1 = Gtk.CellRendererText()  # u need not create a new renderer for each col
		rend_txt1.set_property("editable",True)  # but here they have different properties (one is editable) 
		col1 = Gtk.TreeViewColumn("Col1", rend_txt1, text=1)
		view.append_column(col1)

		rend_txt1.connect("edited", this.on_text_edited)
		# Inspite of being editable, once you hit enter you will be back to the original text if no change is 
		# made to the model. To do so, you need no connect the appopriate signal to a model modifying function.

	def on_text_edited(this, widget, path, new_string):
		this.model[path][1] = new_string

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()