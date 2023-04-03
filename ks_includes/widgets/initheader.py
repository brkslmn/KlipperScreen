import logging
import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class InitHeader(Gtk.Box):
  

    def __init__(self, this, _subTitle, _subText, _imageName):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)

        image = this._gtk.Image(_imageName, this._gtk.content_width * .1 , this._gtk.content_height * .1)
        subTitle = Gtk.Label(_subTitle)
        subText = Gtk.Label(_subText,name ="subtext-label")

        selectBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
       
        selectBox.pack_start(image, False, True, 10)
        selectBox.pack_end(subTitle, False, False, 10)
        selectBox.pack_end(subText, False, False, 10)

        self.add(selectBox)

    