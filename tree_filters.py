#!/usr/bin/python3

# filters (unlike sorting) are either created independently and a model is set for them or they are spawned
# from a model. They are also a type of TreeModel class, creating a layer of indirections - allowing only
# a subset of the model data to be seen

from gi.repository import Gtk

def fltr_func(model, itr, data):
	name=model[itr][0]
	if name[-1]=='h':  # skips out on Anant
		return True
	else:
		return False

dataList = Gtk.ListStore(str, str)
dataList.append(["Ayush","Agrawal"])
dataList.append(["Anirudh","Agrawal"])
dataList.append(["Ashutosh","Agrawal"])
dataList.append(["Anant","Agrawal"])

rend = Gtk.CellRendererText()
name_col = Gtk.TreeViewColumn("Name", rend, text=0)
surname_col = Gtk.TreeViewColumn("Surname", rend, text=1)

fltr = dataList.filter_new()   # spawing the filter instance from the model itself (yields a Gtk.TreeModelFilter)
fltr.set_visible_func(fltr_func, data=None )

tree = Gtk.TreeView(fltr)   # since the filter already contains the information about the model  
tree.append_column(name_col)
tree.append_column(surname_col)

win = Gtk.Window(title="filter example")
win.add(tree)
win.connect("delete-event", Gtk.main_quit)
win.set_position(Gtk.WindowPosition.CENTER)
win.show_all()
Gtk.main()
