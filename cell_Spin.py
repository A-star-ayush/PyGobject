#!/usr/bin/python3

# Gtk.CellRendererSpin renders text in a cell like Gtk.CellRendererText from which it is derived. But
# while the latter offers a simple entry to edit the text, Gtk.CellRendererSpin offers a Gtk.SpinButton
# widget (and not a Gkt.Spinner() !). Of course, that means that the text has to be parseable 
# as a floating point number.

# The range of the spinbutton is taken from the adjustment property of the cell renderer, which can be set explicitly
# or mapped to a column in the tree model, like all properties of cell renders. Gtk.CellRendererSpin also has
# properties for the climb rate and the number of digits to display.

from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Cell Renderer Spin")
		this.set_position(Gtk.WindowPosition.CENTER)

		this.model = Gtk.ListStore(str, int)
		this.model.append(["Apples",10])
		this.model.append(["Mangoes",2])
		this.model.append(["Strawberry",5])

		view = Gtk.TreeView(this.model)

		rnd_text = Gtk.CellRendererText()
		col0 = Gtk.TreeViewColumn("Fruit", rnd_text, text=0)
		view.append_column(col0)	

		rnd_spin = Gtk.CellRendererSpin()
		rnd_spin.set_property("editable", True) # Otherwise what use would be the spin
		rnd_spin.connect("edited", this.on_quantity_edited)

		adj = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
		rnd_spin.set_property("adjustment", adj)
		col1 = Gtk.TreeViewColumn("Quantity", rnd_spin, text=1)
		view.append_column(col1)

		this.add(view)

	def on_quantity_edited(this, widget, path, value):
		this.model[path][1] = int(value)  # remember this conversion otherwise issues may rise

# One thing to observe here is in the function on_quantity_edited, all the arguments to it are just the same
# as those required in catching a Gtk.Spin() edited signal except the extra path argument. This goes general 
# with all the signal connections that are made using the renderer. 

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
