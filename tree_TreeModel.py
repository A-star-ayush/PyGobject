#!/usr/bin/python3

# This file is about the Gtk.TreeStore Model

from gi.repository import Gtk

def print_tree_store(store):
	root=store.get_iter_first()
	print_rows(store, root, "")

def print_rows(store, treeIter, indent):
	while treeIter!=None:   # None is the equivalent of NULL in C
		print (indent+str(store[treeIter][:]))  # printing the elements at that level
		if store.iter_has_child(treeIter):
			childItr=store.iter_children(treeIter)
			print_rows(store, childItr, indent+"\t")  # to create the proper alignment
		treeIter=store.iter_next(treeIter)



dataTree=Gtk.TreeStore(int, str) # this structure of int, str has to maintainted throughout

data = [(1, "Ayush"),
        (2, "Rajat"),
        (3, "Avnish"),          
        (4, "Jugat") ]
    
data2 = [(1, "Agrawal"),
		 (2, "Goel"),
		 (3, "Garg"),
		 (4, "Singh") ]


for row in data:
	dataTree.append(None, row)   # The first argument specifies the Gtk.Iter after whose last child the
					# new row should be inserted. If None (NULL) is specified the row gets added at the top level

for i in range(0,4):
	dataTree.append(dataTree.get_iter(i), data2[i])  # the surnames get added as child nodes to the respective names


# for row in dataTree:  # row is of type Gtk.TreeModelRow
# 	print(row[:])      # printing this way only prints data (since it is at the top level of hirearchy) and not data2 


# To print the entire tree:
# print_tree_store(dataTree)  # function defined above

# for i in range(0, len(dataTree)):   # The iterative approach for printing all the elements
# 	itr=dataTree.get_iter(i)
# 	print(dataTree[itr][:])
# 	indent="\t"
# 	while(dataTree.iter_has_child(itr)):	
# 		itr=dataTree.iter_children(itr)
# 		print(indent+str(dataTree[itr][:]))
# 		indent+='\t'

# row0_0=dataTree.get_iter(0)
# dataTree[row0_0][1]="Anirudh"  # Changes Ayush to Anirudh

# row0_0=dataTree.get_iter(0)
# dataTree[row0_0][1]="Swastik"  # changes the parent node (name) to Swastik
# row0_1=dataTree.iter_children(row0_0)
# dataTree[row0_1][1]="Mittal"  # Modified the child node (surname) to Mittal

# Shortcut for the above by getting iterators from path:
# path=Gtk.TreePath("0:0")# Meaning the first child of the first node(more depths can be reached using subsequent :'s)
# dataTree[dataTree.get_iter(0)][1]="Swastik"
# dataTree[dataTree.get_iter(path)][1]="Mittal"


# Many other functions like inser_after/before, prepend, swap, reorder, move_after/before, is_ansector 
# are also available [check them out on DevHelp] 