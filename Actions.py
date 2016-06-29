#!/usr/bin/python3

# Refer to chapter 21 of the guide "python-gtk-3-tutorial.pdf"
# Also refer to the GNOME wiki pages saved under Gtk : "Gtk/www.gtk.org/HowDoI"
# For function details refer to DevHelp or http://lazka.github.io/pgi-docs/#Gtk-3.0/

from gi.repository import Gtk, Gio

# Remember if u are refering to DevHelp, The GName classes are instantiated like: GSimpleAction becomes
# Gio.SimpleAction.new(..)

# We are using Gtk.ApplicationWindow since it implements GActionMap
# One can use GtkAccelMap for loadable keyboard accelerator speccification

class MyWindow(Gtk.ApplicationWindow):

    def __init__(this, app):  # and has the functionality of adding GMenuModel and setting menubar
        Gtk.ApplicationWindow.__init__(this, title="Actions", application=app)
        this.set_position(Gtk.WindowPosition.CENTER)
        this.set_default_size(400, 400)

        # name, parameter [Note that even new was written]
        action = Gio.SimpleAction.new("sampleAction", None)
        action.connect("activate", this.on_action_activated)
        this.add_action(action)   # method of GActionMap

        # format: accelerator string, win/app.actionName
        app.add_accelerator("<Control><Shift>T", "win.sampleAction")
        # win prefix is for window specific accelerators and app for those that
        # apply to the entire application

        quit = Gio.SimpleAction.new("quit", None)
        quit.connect("activate", this.on_quit_activated, app)
        this.add_action(quit)
        app.add_accelerator("<Control>q", "win.quit")
        # An application can also pickup accelerators from GMenuModel

        this.create_other_actions()
        menu_model = this.create_menu_model()
        # menu bar is for that window whereas app menu is for the entire
        # applications

        app.set_menubar(menu_model)   # app.set_app_menu(menu_model) is used to set the app menu

    def on_action_activated(this, action, param):
        print("Test succeeded")

    # remember u can always catch extra arguments as opposed to the
    def on_quit_activated(this, action, param, app):
        print("Quit called")							# definitions given in Devhelp
        app.quit()

    def on_other_action_activated(this, action, param):
        name = action.get_name()
        print("{0} action was called {1}".format(name, param))

    def create_other_actions(this):
        new = Gio.SimpleAction.new("new", None)
        new.connect("activate", this.on_other_action_activated)
        this.add_action(new)
        Open = Gio.SimpleAction.new("open", None)
        Open.connect("activate", this.on_other_action_activated)
        this.add_action(Open)

    def create_menu_model(this):
        menubar = Gio.Menu.new()  # The GMenu can be populated by adding GMenuItem instances or
        # using the convenience functions like insert_section, append and so on...
        # GMenu is a simple implementation of GMenuModel

        FileMenu = Gio.Menu.new()
        EditMenu = Gio.Menu.new()
        ViewMenu = Gio.Menu.new()

        menubar.append_submenu("File", FileMenu)  # Label, GMenuModel
        menubar.append_submenu("Edit", EditMenu)
        menubar.append_submenu("View", ViewMenu)

        FileSec1 = Gio.Menu.new()
        FileSec1.append("New", "win.new")  # Label, detailed-action
        FileSec1.append("Open", "win.open")
        # Items are like the leaf nodes [which further subdivide into nothing]
        # and actions are associated with them
        FileSec2 = Gio.Menu.new()
        FileSec2.append("Save", None)
        FileSec2.append("SaveAs", None)

        FileSec3 = Gio.Menu.new()
        FileSec3.append("Quit", "win.quit")

        FileMenu.append_section(None, FileSec1)  # Label, GMenuModel
        FileMenu.append_section(None, FileSec2)
        FileMenu.append_section(None, FileSec3)

        EditMenu.append("Copy", None)
        EditMenu.append("Cut", None)
        EditMenu.append("Paste", None)

        Windows = Gio.Menu.new()
        Windows.append("Toolbar", None)
        Windows.append("Statusbar", None)
        ViewMenu.append_submenu("Windows", Windows)

        TestAction = Gio.MenuItem.new("Test Action", None)
        menubar.append_item(TestAction)
        # the simple append used earlier combines GMenuItem.new and GMenu.append_item

        return menubar

        # Separators are not included in the menu model instead they are put between any 
        # two non-empty section if the sections do not have any label associated with them


class MyApplication(Gtk.Application):

    def __init__(this):
        Gtk.Application.__init__(this)

    def do_activate(this):  # we are overriding the method of the parent class
        win = MyWindow(this)
        win.show_all()

    def do_startup(this):
        Gtk.Application.do_startup(this)


app = MyApplication()
app.run([])


# Gio.Action is a way to 'expose' any "single task" your application or widget does by a name.

# Actions have the following properties:
# Name - identifier
# Enabled - whether the action is sensitive or not 
# State (optional) - among the possible, what state the action is in
# Parameter - the data the action needs to proceed 

# Remember the classical 4 examples for actions : 
# 1) stateless action - quit [they have no feeling of like undoing the task or toggling]
# 2) stateful action with no parameter - fullscreen [they implement the toggle like feature]
# 3) stateful action with parameter - justify [left, right, fill]
# 4) stateless action with parameter - openbookmark
# Deatiled actions are useful when we have a parameter

# Make actions (Gio.Action) -> add them to a group (Gio.ActionGroup) -> add them to a widget
# (Gtk.Widget.insert_action_group); here they will gain a prefix - "win/app" and henceforth their fullname 
# should be used; you can use Gtk.Application.add_action directly as well skipping the grouping stage
#  -> make keybindings for the actions (setting 'accel' property in the Gio.Menu file or by using 
# Gtk.Application.add_accelerator)

