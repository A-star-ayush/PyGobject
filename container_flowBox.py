#!/usr/bin/python3

from gi.repository import Gtk, Gdk

# The minimum requirement for running FlowBox is Gtk 3.12

class flowBox(Gtk.Window):

    def __init__(this):
        Gtk.Window.__init__(this)
        this.set_default_size(400, 400)
        this.set_border_width(10)

        header = Gtk.HeaderBar(title="Flow Box")
        header.set_subtitle("Sample color app")
        header.set_show_close_button(True)

        this.set_titlebar(header)

        scroller = Gtk.ScrolledWindow()
        this.add(scroller)

        fb = Gtk.FlowBox()
        fb.set_valign(Gtk.Align.START)
        fb.set_maximum_chilren_per_line(10)
        fb.set_selection_mode(Gtk.SelectionMode.NONE)

        this.create_flowbox(fb)

        scroller.add(fb)

    def color_swatch(this, str_color):
        color = Gdk.color_parse(str_color)
        rgba = Gdk.RGBA.from_color(color)
        button = Gtk.Button()
        area = Gtk.DrawingArea()
        area.set_size_request(24, 24)
        area.override_background_color(0, rgba)
        button.add(area)
        return button

    def create_flowbox(this, flowbox):
        colors = [
        'AliceBlue',
        'AntiqueWhite',
        'AntiqueWhite1',
        'AntiqueWhite2',
        'AntiqueWhite3',
        'AntiqueWhite4',
        'aqua',
        'aquamarine',
        'aquamarine1',
        'aquamarine2',
        'aquamarine3',
        'aquamarine4',
        'azure',
        'azure1',
        'azure2',
        'azure3',
        'azure4',
        'beige',
        'bisque',
        'bisque1',
        'bisque2',
        'bisque3',
        'bisque4',
        'black',
        'BlanchedAlmond',
        'blue',
        'blue1',
        'blue2',
        'blue3',
        'blue4',
        'BlueViolet',
        'brown',
        'brown1',
        'brown2',
        'brown3',
        'brown4',
        'burlywood',
        'burlywood1',
        'burlywood2',
        'burlywood3',
        'burlywood4',
        'CadetBlue',
        'CadetBlue1',
        'CadetBlue2',
        'CadetBlue3',
        'CadetBlue4',
        'chartreuse',
        'chartreuse1',
        'chartreuse2',
        'chartreuse3',
        'chartreuse4',
        'chocolate',
        'chocolate1',
        'chocolate2',
        'chocolate3',
        'chocolate4',
        'coral',
        'coral1',
        'coral2',
        'coral3',
        'coral4'
        ]

        for color in colors:
            button = this.color_swatch_new(color)
            flowbox.add(button)


win = flowBox()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
