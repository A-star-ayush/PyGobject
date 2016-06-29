#!/usr/bin/python3

# This is the VIEW part. There is a single view widger: TreeView.
# This file also introduces the selection functionality.
# column and cell renderers are used to choose how to display the data provided by the model
# A Gtk.TreeViewColumn is the object that Gtk.TreeView uses to organize the vertical columns in the tree view.

from gi.repository import Gtk

def on_tree_selection_changed(selection):
	model, itr= selection.get_selected()
	if itr!=None:
		print("You selected"+str(model[itr][:]))


dataList = Gtk.ListStore(int, str)  

data = [(1, "ayush"),
        (2, "rajat"),
        (3, "avnish"),          
        (4, "jugat"),           
        (5, "shivam"),
        (6, "swastik")]

for row in data:
   dataList.append(list(row))  
    							
tree = Gtk.TreeView(dataList)  # specifying the data model in the cosntructor of the Gtk.TreeView

# tree2 = Gtk.TreeView()
# tree2.set_model(dataList) # another way of setting the model

rend = Gtk.CellRendererText() 
col = Gtk.TreeViewColumn("Number", rend, text=0)
col.set_alignment(0.5)  # a value btw 0.0 and 1.0
col.set_resizable(True)
col.set_min_width(100)  # there is nothing like min_height beacuse height depends on how much data is there
tree.append_column(col)  # (name of the label col to the user, cell renderer, data from model)

rend = Gtk.CellRendererText()
col = Gtk.TreeViewColumn("Name", rend, text=1)
col.set_alignment(0.5) 
col.set_resizable(True)  
tree.append_column(col)

# Many renderers (Gtk.CellRenderer...) available like: Accel, Combo, Pixbuf, Progress, Spin, Toggle and Spinner


# To render more than one model col in a single view col:

# col = Gtk.TreeViewColumn("Number & Name")
# col.set_alignment(0.5)
# number = Gtk.CellRendererText()
# name = Gtk.CellRendererText()
# col.pack_start(number, True)  # second argument is for expand
# col.pack_start(name, True)  # pack_end is also available
# col.add_attribute(number, "text", 0)
# col.add_attribute(name, "text", 1)  # The last argument specifies the model column to pick the data from 
# tree.append_column(col)




# For selection:

select=tree.get_selection()
select.connect("changed", on_tree_selection_changed)


win=Gtk.Window(title="Tree View Example")
win.connect("delete-event", Gtk.main_quit)
win.set_position(Gtk.WindowPosition.CENTER)
win.set_default_size(253,230)
win.add(tree)
win.show_all()
Gtk.main()



