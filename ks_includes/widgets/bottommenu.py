import logging
import os

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, GdkPixbuf


class BottomMenu(Gtk.Box):
  

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL)
        
        menuBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        
        dashboardIcon = Gtk.Image.new_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size("styles/z-bolt/images/dashboard.png", 50, 50))
        printFilesIcon = Gtk.Image.new_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size("styles/z-bolt/images/folder.png", 50, 50))
        printersIcon = Gtk.Image.new_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size("styles/z-bolt/images/printerchange.png", 50, 50))
        configureIcon = Gtk.Image.new_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size("styles/z-bolt/images/configure.png", 50, 50))
        
        dashboardButton = Gtk.Button(label="Dashboard" ,name ="menu-buttons")
        dashboardButton.set_image(dashboardIcon)
        dashboardButton.set_always_show_image (True)
        menuBox.pack_start(dashboardButton, True, True, 0)

        printFilesButton = Gtk.Button(label="Print Files", name ="menu-buttons")
        printFilesButton.set_image(printFilesIcon)
        printFilesButton.set_always_show_image (True)
        menuBox.pack_start(printFilesButton, True, True, 0)

        pintersButton = Gtk.Button(label="Printers" ,name ="menu-buttons")
        pintersButton.set_image(printersIcon)
        pintersButton.set_always_show_image (True)
        menuBox.pack_start(pintersButton, True, True, 0)
        
        configureButton = Gtk.Button(label="Configure" ,name ="menu-buttons")
        configureButton.set_image(configureIcon)
        configureButton.set_always_show_image (True)
        menuBox.pack_start(configureButton, True, True, 0)
        
        menuBox.set_hexpand(True)
       
        self.add(menuBox)

    

    