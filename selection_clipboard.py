#!/usr/bin/python3


# There are multiple types of clipboard selections. The most common one is CLIPBOARD. There exists a selection called
# PRIMARY which stores text selected by the user via mouse.

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Clipboard Example")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(10)

		grid = Gtk.Grid(row_spacing=5, column_spacing=5)

		this.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD) # Gdk.SELECTION_PRIMARY also exists
		this.entry = Gtk.Entry()
		
		this.image = Gtk.Image.new_from_icon_name("process-stop", Gtk.IconSize.MENU)

		bt_copy = Gtk.Button("Copy Text")
		bt_paste = Gtk.Button("Paste Text")
		bt_copyi = Gtk.Button("Copy Image")
		bt_pastei = Gtk.Button("Paste Image")

		for widget in (this.entry, bt_copy, bt_paste):
			grid.add(widget)  # the first 3 widgets gets placed in a horizontal layout
		grid.attach_next_to(this.image, this.entry, Gtk.PositionType.BOTTOM, 1, 1)
		grid.attach_next_to(bt_copyi, this.image, Gtk.PositionType.RIGHT, 1, 1)
		grid.attach_next_to(bt_pastei, bt_copyi, Gtk.PositionType.RIGHT, 1, 1)

		bt_copy.connect("clicked", this.on_copy_clicked)
		bt_copyi.connect("clicked", this.on_copyi_clicked)
		bt_paste.connect("clicked", this.on_paste_clicked)
		bt_pastei.connect("clicked", this.on_pastei_clicked)

		this.add(grid)

	def on_copy_clicked(this, widget):
		this.clipboard.set_text(this.entry.get_text(), -1) # -1 means that the length will be determined
														# otherwise a fixed length argument can be specified
	def on_copyi_clicked(this, widget):
		if this.image.get_storage_type() == Gtk.ImageType.PIXBUF:
			this.clipboard.set_image(this.image.get_pixbuf())
		else:
			print("No image has been pasted yet.")

	def on_paste_clicked(this, widget):
		txt = this.clipboard.wait_for_text()  # requests the contents of the clipboard as text and converts to utf-8,
		#  if neccessary.This function waits for the data to be received using the main loop, so events, timeouts, 
		#  etc, may be dispatched during the wait.
		if txt!=None:
			this.entry.set_text(txt)
		else:
			print("No text on the clipboard")

	def on_pastei_clicked(this, widget):
		img = this.clipboard.wait_for_image()
		if img!=None:
			this.image.set_from_pixbuf(image)

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
