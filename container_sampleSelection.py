#!/usr/bin/python3

from gi.repository import Gtk

# The diff btw sampleSelection.py and listBox.py is that each row of the listBox is selectable
class MySample(Gtk.Window):

    def __init__(this):
        Gtk.Window.__init__(this, title="Sample Selection",border_width=10)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        this.add(vbox)

        hbox = Gtk.Box(spacing=5)
        l = Gtk.Label(label="Require Internet Access",xalign=0)
        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER  # yet another way to set the properties
        hbox.pack_start(l, True, True, 0)
        hbox.pack_start(switch, False, True, 0)  # not allowed to expand

        vbox.pack_start(hbox, True, True, 0)

        hbox = Gtk.Box(spacing=5)
        # mark the use of same variable names again
        l = Gtk.Label(label="Enable Automatic Updates",xalign=0)
        check = Gtk.CheckButton()
        hbox.pack_start(l, True, True, 0)
        hbox.pack_start(check, False, True, 0)

        vbox.pack_start(hbox, True, True, 0)

        hbox = Gtk.Box(spacing=5)
        l = Gtk.Label(label="Date Format",xalign=0)
        combo = Gtk.ComboBoxText()
        combo.insert(0, "0", "24-hour")
        combo.insert(1, "1", "AM/PM")
        hbox.pack_start(l, True, True, 0)
        hbox.pack_start(combo, False, True, 0)

        vbox.pack_start(hbox, True, True, 0)


win = MySample()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
