#!/usr/bin/python3

# The major difference btw a simple window and a dialog is that a dialog comes with prepacked widgets
# which layout the dialog automatically - making it simple to add buttons, labels etc.
# Another big difference is the handling of responses to control how the application should behave after the
# dialog has been interacted with.

# Modal dialogs are those which freezes the rest of the application from user input

from gi.repository import Gtk

class CustomDialog(Gtk.Dialog):
	def __init__(this, parent):
		Gtk.Dialog.__init__(this, "Custom Dialog", parent, 0,   # format (this, name, parent, flags,
					("Cancel", Gtk.ResponseType.CANCEL, # (first_button_text, it's response type, ...))
					 "Ok", Gtk.ResponseType.OK))
		# canel and ok can be substituted with Gtk.STOCK_OPEN and _CANCEL ]
		this.set_default_size(150,100)    # clicking a button emits a signal called "response"

		l = Gtk.Label("Sample Label")

		# this.set_modal(True)  # to make it a modal dialog. No need here, because using .run makes it modal.						

		box = this.get_content_area()   # to add more widgets to the dialog we first "obtain" the box containter
		box.add(l)               # that is handling all the other widgets [this is not the case wid normal windows
		this.show_all()              # where we "create" the box to contain the widgets for that window]
		# .add_button can be used to add a buttons

# Response Type can be NONE, REJECT, ACCEPT, DELETE_EVENT, OK, CANCEL, CLOSE, YES, NO, APPLY, HELP
# flags can be Gtk.DialogFlags.MODAL , Gtk.DialogFlags.DESTROY_WITH_PARENT [u can even bitwise or them using '|']

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Sample Dialog")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_default_size(250,100)
		this.set_border_width(10)

		bt = Gtk.Button("Open Dialog")
		bt.connect("clicked", this.on_button_clicked)

		this.add(bt)

	def on_button_clicked(this, widget):
		diag = CustomDialog(this)
		response = diag.run() # run is used to wait for the dialog to return or get destroyed
			# before returning control flow to ur code. The method returns an int which may be a value
			# from Gtk.ResponseType or can be custom. If the dialog is destroyed, Gtk.ResponseType.NONE is returned
		if response == Gtk.ResponseType.OK:
			print("OK was selected")
		elif response == Gtk.ResponseType.CANCEL:
			print("CANCEL was selected")
		else:
			print("Something else occured")

		diag.destroy()         # .hide() is also available which simply removes the dialog from the view,
							   # however keeps it stored in the memory (useful when the same dialog is to be reused)

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()


