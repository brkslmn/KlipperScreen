import logging
import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, GdkPixbuf


class ProgressBar(Gtk.Box):
  

    def __init__(self, this, _temperature, _image, _fraction, _style):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL)
        
        this.labels['temperature'] = Gtk.Label(_temperature,name ="progress-label")
        scale_progress = Gtk.ProgressBar(name =_style)
        scale_progress.set_fraction(_fraction)
        scale_progress.set_show_text(False)
        scale_progress.set_hexpand(True)
        
        extruder_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        
        extruder_box.add(this._gtk.Image(_image, 80, 80))
        extruder_box.add(this.labels['temperature'])
        extruder_box.add(scale_progress)
        extruder_box.set_valign(Gtk.Align.CENTER)
       
        self.add(extruder_box)

    

    