#!/usr/bin/python3

from gi.repository import Gtk, GdkPixbuf # or u can directly import Pixbuf from gi.repository.GdkPixbuf

# for GdkPixbuf look at the development folder under linux because it is not provided in DevHelp

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Cell Renderer Pixbuf")
		this.set_position(Gtk.WindowPosition.CENTER)

		model = Gtk.ListStore(str, str, GdkPixbuf.Pixbuf)
		model.append(["New", "document-new", GdkPixbuf.Pixbuf.new_from_file("new.png")])
		model.append(["Open", "document-open", GdkPixbuf.Pixbuf.new_from_file("open.png")])
		model.append(["Save", "document-save", GdkPixbuf.Pixbuf.new_from_file("save.png")])

		view = Gtk.TreeView(model)
		rend_txt = Gtk.CellRendererText()
		col0 = Gtk.TreeViewColumn("Text", rend_txt, text=0)
		view.append_column(col0)

		rend_pix = Gtk.CellRendererPixbuf() # used to render an image given either a Gdk.Pixbuf or a named icon
		col1 = Gtk.TreeViewColumn("Named Icon", rend_pix, icon_name=1) # meaning to get icon names from col1 of model
		view.append_column(col1) # The icons found in the present theme falls under the named-icons category

		rend_pix2 = Gtk.CellRendererPixbuf()
		col2 = Gtk.TreeViewColumn("Pixbuf", rend_pix2, pixbuf=2) # using the pixbufs' here
		view.append_column(col2)

		this.add(view)

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
