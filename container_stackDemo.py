#!/usr/bin/python3  

from gi.repository import Gtk

# Stack unlike a notebook can only show one widget at a time
# StackSwitcher however can be used to dynamically handle the stack children

class StackWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this,title="Stack Demo",border_width=10)
		vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

		this.add(vbox)

		stack=Gtk.Stack()
		stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		stack.set_transition_duration(1000)

		chkButton=Gtk.CheckButton("Click Me")  # this is the text that appears next to the check button
		stack.add_titled(chkButton,"cb","Check Button")  # format (child_widget,"child_name","Dispaly name")
						# The display name serves as the label for the switch button handled by StackSwitcher
		l=Gtk.Label()
		l.set_markup("<big>A <b>F</b>ancy label</big>")  # to set a markup text
		stack.add_titled(l,"l1","A label")

		stackSwitcher=Gtk.StackSwitcher()
		stackSwitcher.set_stack(stack)
		vbox.pack_start(stackSwitcher,True,True,0)
		vbox.pack_start(stack,True,True,0)

win=StackWindow()
win.connect("delete-event",Gtk.main_quit)
win.set_position(Gtk.WindowPosition.CENTER)
win.show_all()
Gtk.main()