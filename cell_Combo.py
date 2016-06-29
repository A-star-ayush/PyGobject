#!/usr/bin/python3

from gi.repository import Gtk

# Gtk.CellRendererCombo renders text in a cell like Gtk.CellRendererText from which it is derived. But
# while the latter offers a simple entry to edit the text, Gtk.CellRendererCombo offers a Gtk.ComboBox widget
# to edit the text. The values to display in the combo box are taken from the Gtk.TreeModel specified in the “model”
# property separately for the renderer.

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Cell Renderer Combo")
		this.set_position(Gtk.WindowPosition.CENTER)

		this.model = Gtk.ListStore(str, str, str)
		this.model.append(["HUM","Ethics",""])
		this.model.append(["CSE","Computers",""])
		this.model.append(["EEE","Electronics",""])
		this.model.append(["MAT","Mathematics",""])

		view = Gtk.TreeView(this.model)

		rnd_txt = Gtk.CellRendererText()
		col0 = Gtk.TreeViewColumn("CODE", rnd_txt, text=0)
		view.append_column(col0)

		rnd_combo = Gtk.CellRendererCombo()
		rnd_combo.set_property("editable", True)
		rnd_combo.set_property("model", this.model)  # The model has to be separately stated for this renderer
		rnd_combo.set_property("text-column",1)  # col 1 of the model becomes the list of choices
		rnd_combo.set_property("has-entry", True) # Gtk.Entry type style 
		rnd_combo.connect("edited", this.on_combo_edited) # connecting the signal so that the entries get saved
		col1 = Gtk.TreeViewColumn("COURSE", rnd_combo, text=2)  # Initially the col 2 of the model has nothing
		view.append_column(col1)

		for col in (col0, col1):
			col.set_resizable(True)
			col.set_alignment(0.5)
			col.set_min_width(100)

		this.add(view)

	def on_combo_edited(this, widget, path, text):
		this.model[path][2] = text

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
