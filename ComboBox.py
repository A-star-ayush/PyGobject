#!/usr/bin/python3

from gi.repository import Gtk

# ComboBox allows for the selection of an item from a dropdown menu.

# Similar to Gtk.TreeView - both use the modern view pattern. The display of the choices can be adapted to the data 
# in the model by using cell renderers. 

# If the combo box contains a large number of items, it may be better to display them in a grid rather than a list. 
# This can be done by calling Gtk.ComboBox.set_wrap_width().

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="ComboBox")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(10)

		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

		branches = ["CSE","EEE","EC","MEC","CVL"]
		years = ["1","2","3","4"]  # making them integers had the program crash on using both combo texts 

		model1 = Gtk.ListStore(str)
		for branch in branches:
			model1.append([branch])
		
		model2 = Gtk.ListStore(str)
		for year in years:
			model2.append([year])

		branch_combo = Gtk.ComboBox.new_with_model_and_entry(model1)
		branch_combo.set_entry_text_column(0) # only relevant if the combo box has been created with "entry"
		
		year_combo = Gtk.ComboBox.new_with_model_and_entry(model2)
		year_combo.set_entry_text_column(0)  # 0 refers to the col of the model to render options from

# The Gtk.ComboBox widget usually restricts the user to the available choices, but it can optionally have an 
# Gtk.Entry, allowing the user to enter arbitrary text if none of the available choices are suitable. To do this, 
# use one of the static methods Gtk.ComboBox.new_with_entry() or Gtk.ComboBox.new_with_model_and_entry().
# This entry can be accessed using the .get_child() method
		
		branch_combo.connect("changed", this.on_changed)
		year_combo.connect("changed", this.on_changed)

		vbox.pack_start(branch_combo, False, False, 0)
		vbox.pack_start(year_combo, False, False, 0)

		this.add(vbox)

	def on_changed(this, combo):
		itr = combo.get_active_iter()  # functionality available with Gtk.ComboText
		if itr!=None:
			model = combo.get_model()
			print("Selected: %s" % (model[itr][0]))
		else:
			entry = combo.get_child()
			print("Entered: %s" % (entry.get_text()))

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
