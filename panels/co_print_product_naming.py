import logging
import os

import i18n

import gi

from ks_includes.widgets.initheader import InitHeader
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintProductNaming(*args)


class CoPrintProductNaming(ScreenPanel):

    def __init__(self, screen, title):
        super().__init__(screen, title)

       
        
        initHeader = InitHeader (self, i18n.t('translate.deviceNamingHeader'),i18n.t('translate.deviceNamingContent'), "naming")

        deviceImage = self._gtk.Image("device", self._gtk.content_width * .5 , self._gtk.content_height * .5)
       
        self.continueButton = Gtk.Button(i18n.t('translate.continue'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4 )
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)
        
        self.entry = Gtk.Entry(name="device-name")
        self.entry.set_text("Cihaz İsmi")
        self.entry.set_margin_left(self._gtk.action_bar_width *4)
        self.entry.set_margin_right(self._gtk.action_bar_width*4 )
       
      
        
        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main.pack_start(initHeader, False, False, 0)
        main.pack_start(self.entry, False, False, 20)
        main.pack_start(deviceImage, False, False, 20)
        main.pack_end(buttonBox, False, False, 20)
   

        self.content.add(main)
        

    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_wifi_selection", "co_print_wifi_selection", None, 2)
        
  
