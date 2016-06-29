#!/usr/bin/python3

from gi.repository import Gtk, Gio

# HeaderBar is just like a box with a central label - can be used as the
# titlebar of an application


class headerBar(Gtk.Window):

    def __init__(this):
        Gtk.Window.__init__(this)
        this.set_border_width(10)
        this.set_default_size(500, 300)

        hb = Gtk.HeaderBar()
        hb.set_title("HeaderBar Example")
        hb.set_show_close_button(True)

        this.set_titlebar(hb)

        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        # image is scaled to the size of the Button
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)  # Mark the way an image is applied to the button
        hb.pack_end(button)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        # adds the linked style to the current style
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(button)

        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(button)

        hb.pack_start(box)

    # we need not put this on a layout because this is the only widget of our  window
        this.add(Gtk.TextView())
        # since hb has now become the titlebar

win = headerBar()
win.set_position(Gtk.WindowPosition.CENTER)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
