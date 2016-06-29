#!/usr/bin/python3

from gi.repository import Gtk

# This is the MODEL part of the TreeView Widget
# Models (Gtk.TreeModel) hold data.
# Custom model can be created but the two provided are: Gtk.ListStore and Gtk.TreeStore
# Each Gtk.TreeModel can be used by more than one Gtk.TreeView.

# Here we shall see the ListStore Model

dataList = Gtk.ListStore(int, str)  # initiates a data table with 2 col of type int and str respectively
									# As the name suggests List store is a simple list meaning that an entry 
									# cannot have sub entries/ children
data = [(1, "ayush"),
        (2, "rajat"),
        (3, "avnish"),          # we cud have used the append function directly: dataList.append([3,"avnish"])
        (4, "jugat"),           # but writing the append function over and over again is quite tedious
        (5, "shivam"),
        (6, "swastik")]     # NOTE: append returns the iter to the current item which can be caught in a variable

for row in data:
   dataList.append((row))  # data has to be appended in the form of a tuple/list and nothing else 

# dataList.append([1,"ayush"])  # Duplicates can be added

# dataList.prepend([7,"anirudh"])  # puts it at the starting of the list

# row3=dataList.get_iter(3)  # returns a Gtk.TreeIter to the row number specified
# row0=dataList.get_iter_first()    # a path can also be specified (Gtk.TreePath("3"))

# there is also a get_value function [for example checkout sort.py]

# print(row0) # Simply issung the print command prints it address, to deference:
# print(dataList[row0][:])  # using slice to print everythin in row0
# print(dataList[row3][:])
# print(len(dataList))  # 6 - the number of rows. "len works just fine because dataList here is simply a list type"

# dataList[row0][1]="prasang"    # Setting Values

# for i in range(0,len(dataList)):
# 	row=dataList.get_iter(i)		# traversing the entire list
# 	print(dataList[row][:])

# for row in dataList:  # row is of type Gtk.TreeModelRow which can be deferenced directly
# 	print(row[:])    # The shortcut

# itr=dataList.append([7,"anirudh"]) # the append function returns the row number currently the data was appended to
# print(dataList[itr][:])     # it actually returns a Gtk.TreeIter object cannot directly be dereferenced (like above)


# dataList.clear()  # removes all the rows

# new_order=[2,3,5,1,4,0]     # Semantics: new_order[new_pos]=old_pos. Here the 0th row will now become the 5th row
# dataList.reorder(new_order)  # reoders the rows. Only works with unsorted stores.

# dataList.swap(dataList.get_iter(1),dataList.get_iter(3))  # Only works with unsorted stores 
													 # Swaps the 2 rows specified by the Gtk.TreeIter objects

# dataList.move_before(dataList.get_iter(0), dataList.get_iter(3))  # Moves row 0 before row 3
# dataList.move_after(dataList.get_iter(2), dataList.get_iter(4))  # Moves row 2 below row row 4
			# Appropriate shifts takes place when you use move_before or move_after
			# These 2 also work only on unsorted models

# dataList.remove(dataList.get_iter(0))  # removes row 0 from the model 
