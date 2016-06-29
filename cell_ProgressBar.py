#!/usr/bin/python3

from gi.repository import Gtk, GObject

# CellRendererProgress renders a numeric value as a progress bar in the cell
# The percentage value of the progress bar can be modified by changing the “value” property. Similar to
# Gtk.ProgressBar, you can enable the activity mode by incrementing the “pulse” property instead of the “value”
# property.

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this, title="Cell Renderer Progress Bar")
		this.set_position(Gtk.WindowPosition.CENTER)

		this.model = Gtk.ListStore(str, int)  # the int will be used as the value for the progress bar

		this.itr = this.model.append(["TASK 1",0]) # captured the first row iterator [will be useful later on]  
		this.model.append(["TASK 2",0])
		this.model.append(["TASK 3",0]) # initially setting the progress to zero

		view = Gtk.TreeView(this.model)

		rnd_text = Gtk.CellRendererText()
		col0 = Gtk.TreeViewColumn("Task At hand", rnd_text, text=0)
		view.append_column(col0)

		rnd_pg = Gtk.CellRendererProgress()
		col1 = Gtk.TreeViewColumn("Progress", rnd_pg, value=1)  # here the "inverted" prop cud have been set 
													# some col of the model after following "value" by a comma
		view.append_column(col1)

		timeout_id = GObject.timeout_add(100, this.on_timeout, None) # after every 100us call the function on_timeout

		this.add(view)

	def on_timeout(this, usr_data):
		new_val = this.model[this.itr][1] + 1  # Increementing the old value by 1
		if new_val>100:									# Here we have stuck ourselves to integers
			this.itr = this.model.iter_next(this.itr)  # getting to the next job in line
		if this.itr == None:
			this.reset_model()
		new_val = this.model[this.itr][1] + 1

		this.model[this.itr][1] = new_val
		return True

	def reset_model(this):   # Brings the overall progress back to zero
		for row in this.model: 
			row[1]=0
		this.itr = this.model.get_iter_first()  # do not miss out on this one while resetting

def main():
	win = MyWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
