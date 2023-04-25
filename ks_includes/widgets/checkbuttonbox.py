import logging
import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Pango


class CheckButtonBox(Gtk.Box):
  

    def __init__(self, this, _content):
        super().__init__()
        
        self.button1 = Gtk.CheckButton(label=_content)
        self.label_widget = self.button1.get_child()
        self.label_widget.override_font(Pango.FontDescription("18"))
        
        self.button1.connect("toggled", self.on_button_toggled)
        
        info = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        info.set_halign(Gtk.Align.CENTER)
        
        info.pack_start(self.button1, False, False, 0)

        self.add(info)

    def on_button_toggled(self, button):
        
            if button.get_active():
                print("Radio butonu seçildi:", button.get_label())
            

    