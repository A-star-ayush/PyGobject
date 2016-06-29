#!/usr/bin/python3

from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

# Gtk.IconView displays a collection of icons in a grid view with features such as drag and drop, multiple selections
# and item reordering.

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(10)
		this.set_default_size(250,250) # this will restrict the icons so that they initially fall in a vertical line 

		icons = ["edit-copy", "edit-cut", "edit-paste"]
		labels = ["Copy", "Cut", "Paste"]

		model = Gtk.ListStore(Pixbuf, str) # Gtk.IconView requires one col of its model to contain Pixbuf objects

		iconView = Gtk.IconView.new_with_model(model)
		iconView.set_pixbuf_column(0)
		iconView.set_text_column(1)  # Which appears below the icon

		for i in range(0, 3):
			pix = Gtk.IconTheme.get_default().load_icon(icons[i], 64, 0)
			model.append([pix, labels[i]])

		# the selection mode can be set using .set_selection_model()

		this.add(iconView)

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
