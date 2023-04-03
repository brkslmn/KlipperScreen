import logging
import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class RadioButtonBox(Gtk.Box):
  

    def __init__(self, this, _content):
        super().__init__()

        button1 = Gtk.RadioButton.new_with_label_from_widget(None,_content)
        button1.connect("toggled", self.on_button_toggled, "1")

        info = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        
        info.set_name("selection-box")
        info.pack_end(button1, False, False, 0)

        self.add(info)

        def on_button_toggled(self, button, name):
        
        if button1.get_active():
            state = "on"
        else:
            state = "off"

    