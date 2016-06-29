#!/usr/bin/python3

# for theory refer to python-gtk-3-tutorial.pdf [page no ~ 95]
# also see the notes at the end of this file

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, GdkPixbuf

# for the ID's used, using global variables would have been a better choice. If we wanted to change the id
# afterwards it could have been acheived using a single change in the global vairable. Also it enhances readibility.
# Checkout the implementaition in the book which uses the global variables.

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Drag N Drop Example")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(10)

		vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=5)
		this.add(vbox)

		hbox = Gtk.Box(spacing = 3)
		vbox.pack_start(hbox, True, True, 0)

		this.dragArea = DragSource()
		this.dropArea = DropDestination() 
		hbox.pack_start(this.dragArea, True, True, 0)
		hbox.pack_start(this.dropArea, True, True, 0)

		box = Gtk.Box(spacing = 3)
		rbt_txt = Gtk.RadioButton.new_with_label_from_widget(None, "DND Text")  # DND - Drag N Drop
		rbt_img = Gtk.RadioButton.new_with_label_from_widget(rbt_txt, "DND Image")
		box.pack_start(rbt_txt, True, True, 0)
		box.pack_start(rbt_img, True, True, 0)
		vbox.pack_start(box, True, True, 0)

		rbt_txt.connect("toggled", this.add_targets, 11) # 11, 22 are self choosen - nothing special about them
		rbt_img.connect("toggled", this.add_targets, 22)


	def add_targets(this, radio_button, num):
		targets = Gtk.TargetList.new([])  # we start with an empty target list
		targets.add_text_targets(1) if num==11 else targets.add_image_targets(0, True) 
		# 1 is the id for text and 0 is the id for image
		this.dragArea.drag_source_set_target_list(targets)
		this.dropArea.drag_dest_set_target_list(targets)

class DragSource(Gtk.IconView):
	def __init__(this):
		Gtk.IconView.__init__(this)

		this.model = Gtk.ListStore(str, GdkPixbuf.Pixbuf)
		this.set_model(this.model)

		this.set_text_column(0)
		this.set_pixbuf_column(1)

		this.add_item("Item1","image-missing")
		this.add_item("Item2","help-about")
		this.add_item("Item3","edit-copy")

		this.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, [], Gdk.DragAction.COPY)
		this.connect("drag-data-get", this.on_data_request)

	def on_data_request(this, widget, drag_context, data, info, time):
		path = this.get_selected_items()[0]
		itr = this.model.get_iter(path)

		if info == 1: # 1 is the id we reserved for Target Type Text
			text = this.model.get_value(itr, 0) # since 0 is the text column in our model
			data.set_text(text, -1) # data is the Gtk.SelectionData object that needs to be filled with the data
								    # -1 to indicate that the string is null terminated; otherwise size of the string
		elif info == 0:
			pixbuf = this.model.get_value(itr, 1)
			data.set_pixbuf(pixbuf)


	def add_item(this, label, icon_name):
		pixbuf = Gtk.IconTheme.get_default().load_icon(icon_name, 16, 0)
		this.model.append([label, pixbuf])

class DropDestination(Gtk.Label):
	def __init__(this):
		Gtk.Label.__init__(this, "Drop Something on me!")
		this.drag_dest_set(Gtk.DestDefaults.ALL, [], Gdk.DragAction.COPY)

		this.connect("drag-data-received", this.on_data_received)

	def on_data_received(this, widget, drag_context, x, y, data, info, time):
		if info == 1:
			text = data.get_text()
			print("Received text: %s" % text)
		elif info == 0:
			pixbuf = data.get_pixbuf()
			width = pixbuf.get_width()
			height = pixbuf.get_height()

			print("Received Pixbuf with width %spx and height %spx" % (width, height))


def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()

############################# Notes ###########################################

# DND (Drag N Drop) is about source and target.
# To classify a widget as source: Gtk.Widget.drag_set_source(); as target: Gtk.Widget.drag_dest_set()
	# [eg. this.drag_dest_set in the DropDestination class above ]
    # However classes like Gtk.TreeView and Gtk.IconView require the use of special function
    # [eg. the Gtk.IconView.enable_model_drag_source above]
# For basic DND, source must connect to "drag-data-get" signal and target must to "drag-data-received"
	# the get signal (as used in the DragSource class above) has two important arguments: id and data
		# data (Gtk.SelectionData) must be filled with the data that the source chooses to send to the target
		# id helps identify the type of target object desired (which is previously set in Gtk.TargetList)
	# the received signal (as used in the DropDestination above) receives the "data" and "id"
		# knowledge of id can be used to choose what to do with the received data
# The nature of the transfer of data is dictated by the flags that u pass to the methods which are responsible
  # for classifying source and target. For eg. Gdk.DragAction.COPY is used both at the source and the target

# for more theory refer to the book alongside the url saved in the document named "Refrences" 