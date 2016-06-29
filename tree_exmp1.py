#!/usr/bin/python3

# An anime list created using the TreeModel and TreeView
# In order to implement both (filtering and sorting) behaviours, the model becomes the child of the filtered 
# model and the filtered model the child of the sorted model
# We are using the implicit sort functions (explicit one was creating some problems [try later])

from gi.repository import Gtk

def fltr_func(model, itr, data):
	genre = model[itr][2]
	rating = str(model[itr][0])  # converting into str is necessary for operation due to the model and the view
	[genreList, ratingList] = data
	if genre in genreList:  # mark the way the if statement is used to compute the "contains" condition
		if rating in ratingList:
			return True
	return False

class MyWindow(Gtk.Window):
	def __init__(this):
		Gtk.Window.__init__(this)
		this.set_position(Gtk.WindowPosition.CENTER)  # the this pointer is mandatory
		this.set_border_width(5)

		hb = Gtk.HeaderBar()
		hb.set_title("Anime List")
		hb.set_show_close_button(True)
		this.set_titlebar(hb)

		model = Gtk.ListStore(int, str, str)

		dataList=[(5,"Naruto", "Action"),
		          (4,"Bleach", "Action"),
		          (3,"Fairy Tail", "Action"),
		          (5,"Death Note", "Mystery"),
		          (2,"Shiki", "Mystery"),
		          (3,"Another", "Mystery"),
		          (5,"Fullmetal Alchemist", "Action"),
		          (3,"Code Geas", "Action"),
		          (4,"Attack on Titans", "Action"),
		          (3,"Sword Art Online", "Action"),
		          (3,"Dragon Ball Super", "Action"),
		          (3,"Detective Conan", "Mystery"),
		          (4,"Kuroko no Basuke", "Sports"),
		          (3,"High School DxD", "Action"),
		          (4,"Tokyo Ghoul", "Action"),
		          (3,"Fate Zero", "Action"),
		          (3,"Noragami", "Action"),
		          (3,"Btoom", "Action"),
		          (4,"Elfen Lied", "Romantic"),
		          (2,"Hellsing Ultimate", "Action"),
		          (4,"Arslan Senki", "Historical"),
		          (4,"Seven Deadly Sins", "Action"),
		          (3,"Prince of Stride", "Sports"),
		          (4,"Erased","Mystery"),
		          (4,"Monster","Mystery")]

		for row in dataList:
			model.append(row)

		this.genreList=[]
		this.ratingList=[]

		this.filtered_model = Gtk.TreeModelFilter(child_model = model)
		this.filtered_model.set_visible_func(fltr_func, data = ([this.genreList, this.ratingList]))
		
		sorted_filtered_model = Gtk.TreeModelSort(model = this.filtered_model) 

		view = Gtk.TreeView(sorted_filtered_model) # mark the initialization was done with just model

		rend = Gtk.CellRendererText()
		col0 = Gtk.TreeViewColumn("Name", rend, text=1)
		col1 = Gtk.TreeViewColumn("Genre", rend, text=2)
		col2 = Gtk.TreeViewColumn("Rating", rend, text=0)

		min_width = (190, 140, 80)
		col_id = (1, 2, 0) 
		i = 0
		for col in (col0, col1, col2):  # better than doing it separately for each
			col.set_resizable(True)
			col.set_alignment(0.5)
			col.set_min_width(min_width[i])
			col.set_sort_column_id(col_id[i]) # remember here col0 is not handling the 0th col of model
			i+=1                     	# Here we are using the inbuilt sort function
			view.append_column(col)

		vbox = Gtk.Box(orientation= Gtk.Orientation.VERTICAL, spacing=5)
		this.add(vbox)

		hbox = Gtk.Box(spacing=5)

		button_labels = ("Action", "Mystery", "Sports", "Romantic", "Historical")
		for i in button_labels:
			bt = Gtk.ToggleButton(i)
			bt.connect("toggled", this.on_button_toggle_genre, i)
			hbox.pack_start(bt, True, True, 0)

		vbox.pack_start(hbox, False, False, 0)  # Try making these true and try to go all the way upto 
													# displaying everything and then return
		
		hbox = Gtk.Box(spacing=5)  # necessary to reinatialize it 
		button_labels_2 = ("5", "4", "3", "2","1")
		for i in button_labels_2:
			bt = Gtk.ToggleButton(i)
			bt.connect("toggled", this.on_button_toggle_rating, i)
			hbox.pack_start(bt, True, True, 0)

		vbox.pack_start(hbox, False, False, 0)
		vbox.pack_start(view, True, True, 0)

	def on_button_toggle_genre(this, button, genre):
		status = button.get_active()
		if status:
			this.genreList.append(genre)
		else:
			this.genreList.remove(genre)
		this.filtered_model.refilter()

	def on_button_toggle_rating(this, button, rating):
		status = button.get_active()
		if status:
			this.ratingList.append(rating)
		else:
			this.ratingList.remove(rating)
		this.filtered_model.refilter()

		
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

		