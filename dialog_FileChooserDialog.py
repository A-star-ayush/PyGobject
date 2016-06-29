#!/usr/bin/python3


# suitable for use with “File/Open” or “File/Save” menu items. You can use all of the 
# Gtk.FileChooser methods on the Gtk.FileChooserDialog as well as those for Gtk.Dialog.

# for theory refer to File_Info.png or page 95 of the python-gtk-3-tutorial.pdf

# In constrast to Gtk.Dialog, u cannot use custom response codes with Gtk.FileChooserDialog

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="FileChooser Example")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(10)
		this.set_default_size(280, 75)

		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		this.add(box)

		bt_file = Gtk.Button("Choose File")
		box.add(bt_file)
		bt_file.connect("clicked", this.on_file_clicked)
		
		bt_folder = Gtk.Button("Choose Folder")
		box.add(bt_folder)
		bt_folder.connect("clicked", this.on_folder_clicked)
		

		# format (title, parent, purpose(compulsory), (button_label, its repsonse type ..))
	def on_file_clicked(this, widget): 
		diag = Gtk.FileChooserDialog("Please select a file", this, Gtk.FileChooserAction.OPEN,
									("Cancel", Gtk.ResponseType.CANCEL,
									 "Open", Gtk.ResponseType.OK))

		this.add_filters(diag)
		# diag.set_default_size(800, 400)  # for some reason this is not working
		# a workaround cud be to change the ./config/gtk-3.0/settings.ini

		response = diag.run()
		if response == Gtk.ResponseType.OK:
			print("Open clicked")
			print("File Selected: " + diag.get_filename()) # for multiple selection: .set_select_multiple()
		elif response == Gtk.ResponseType.CANCEL:          # then the list can be retrived via .get_filenames()
			print("Cancel clicked")

		diag.destroy()

		#Gtk.FileChooserAction. can be OPEN, SAVE, SELECT_FOLDER, CREATE_FOLDER (it is a compulsory field)
		# the above fields can be bitwise ORed as well using '|'

	def on_folder_clicked(this, widget):
		diag = Gtk.FileChooserDialog("Please select a folder", this, Gtk.FileChooserAction.SELECT_FOLDER,
									("Cancel", Gtk.ResponseType.CANCEL,
									"Open", Gtk.ResponseType.OK))
		# no need to apply any filter here beacause we have set the chooser action to select folder
		
		response = diag.run()
		if response == Gtk.ResponseType.OK:
			print("Open clicked")
			print("Folder selected:" + diag.get_filename())
		elif response == Gtk.ResponseType.CANCEL:
			print("Cancel clicked")

		diag.destroy()

	def add_filters(this, diag):
		flt_txt = Gtk.FileFilter()   # Creating a text filter
		flt_txt.set_name("Text files")  # sets the human readable name of the filter
		flt_txt.add_mime_type("text/plain") # allowing a given mime type to filter 
		diag.add_filter(flt_txt)

		flt_py = Gtk.FileFilter()
		flt_py.set_name("Python")
		flt_py.add_mime_type("text/x-python")
		diag.add_filter(flt_py)
		
		flt_all = Gtk.FileFilter()
		flt_all.set_name("All")
		flt_all.add_pattern("*") # allowing shell type glob to filter
		diag.add_filter(flt_all)

		# a filter option for image types also exists

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
    