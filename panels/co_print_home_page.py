import logging
import os
from ks_includes.widgets.checkbuttonbox import CheckButtonBox
import gi
import i18n

from ks_includes.widgets.bottommenu import BottomMenu
from ks_includes.widgets.progressbar import ProgressBar
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk, GdkPixbuf

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintHomePage(*args)


class CoPrintHomePage(ScreenPanel):

     
    def __init__(self, screen, title):
        super().__init__(screen, title)
        
       
        menu = BottomMenu()
        
        extruderBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 10)
        extruderBox.set_name("extruder-box")
        
        extruderProgressBar = ProgressBar(self, "25° / 0°", "extrudericon", 0.5, "progress-bar-extruder-blue")
        extruderBox.pack_start(extruderProgressBar, True, True, 0)
        
        page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        page.pack_start(extruderBox, True, True, 0)
        page.pack_end(menu, True, True, 0)

        
        self.content.add(page)

    

