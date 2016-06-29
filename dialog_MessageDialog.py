#!/usr/bin/python3


# Used to create simple, standard message dialogs, with a message, an icon, and buttons for user response
# A secondary text can be associated with the message dailog which causes the primary text to go bold (by defualt)
# It is simply used to supply extra information. Each of the text's markup can be changed using .set_markup() and
# .format_secondary_markup(). The icon can also be changed using .set_image() method.

# Since we are not creating a custom dialog we need not describe a separate class for creating the dialog

from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Message Dailog")
		this.set_position(Gtk.WindowPosition.CENTER)
		this.set_border_width(10)

		bt1 = Gtk.Button("Information")
		bt1.connect("clicked", this.on_information_clicked)
		
		this.add(bt1)

		# format: (parent, flags, type, buttons, messageformat, ...)
	def on_information_clicked(this, widget):
		dg = Gtk.MessageDialog(this, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "This is an info dialog")
		dg.format_secondary_text("Secondary text that explains it")
		dg.run()
		dg.destroy()
		# the button types do emmit the "response" signal with response id from Gtk.ResponseTypeself.
		# dg.get_message_area() can be used to get the content area for packing widgets of our own

	# The icons depict the message type for these dialogs
	# Message Type can be can be INFO, WARNING, QUESTION, ERROR, OTHER [The OTHER type doesn't have a deafult icon]
	# Button Type can be NONE, OK, CLOSE, CANCEL, YES_NO, OK_CANCEL (the last two create 2 different buttons for each field)


def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
