#!/usr/bin/python3

# The list store and tree store classes implements Sortable so sorting functionality
# feels like an extension to them but the same is not the case with filters

from gi.repository import Gtk

def compare(model, row1, row2, user_data):
	col, _ = model.get_sort_column_id()  # returns the col/s set to be sorted using this function
	val1 = model.get_value(row1,col)  
	val2 = model.get_value(row2,col)	
	if val1[-1] < val2[-1]:  # sorting as per the last character in the string
		return -1
	elif val1[1] == val2[1]:   # The function takes in two rows and the return value is:
		return 0								# negative - if r1 should come before r2
	else:										# zero - if any they are equal
		return 1								# positive - if r1 should come after r2	

dataList = Gtk.ListStore(str, int)
dataList.append(["adsads",2])
dataList.append(["ghfdf",1])
dataList.append(["nskfd",6])
dataList.append(["dkal",0])
dataList.append(["jvnkla",4])
dataList.append(["djasl",9])

tree = Gtk.TreeView(dataList)

rend = Gtk.CellRendererText()
col = Gtk.TreeViewColumn("Random Text", rend, text=0)

col.set_sort_column_id(0)  # NOTE: here 0 refers to the first col of the model and not the view 
										# Col 1 of the view may not necessarily control the model's col0
		    # Now col 0 can be sorted by simply clicking on its header (ascending and descending on alternate clicks)

tree.append_column(col)

rend = Gtk.CellRendererText()
col = Gtk.TreeViewColumn("No.", rend, text=1)
col.set_sort_column_id(1)  # this uses the normal sort function and not the custome made one
tree.append_column(col)


dataList.set_sort_func(0, compare, None)  # last arg- user data
										  # first arg - current sort column id of sortable. If it is the same as 
										  # sort_column_id , then the model will sort using this function.
										  # thus different sort functions can be used for different cols


win = Gtk.Window(title = "sort example")
win.add(tree)
win.set_position(Gtk.WindowPosition.CENTER)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
