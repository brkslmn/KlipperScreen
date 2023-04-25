import logging
import os

import i18n

import gi

from ks_includes.widgets.initheader import InitHeader
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk, GdkPixbuf

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintWifiSelectionSelect(*args)


class CoPrintWifiSelectionSelect(ScreenPanel):

    def __init__(self, screen, title):
        super().__init__(screen, title)

        initHeader = InitHeader (self, i18n.t('translate.selectWifiHeader'),i18n.t('translate.selectWifiContent'), "wifi")
        
        # ComboBox'a öğeler ekle
        
        self.selectedWifiImage = self._gtk.Image("sinyal", self._gtk.content_width * .05 , self._gtk.content_height * .05)
        self.selectedWifiName = Gtk.Label("",name ="wifi-label")
        self.selectedWifiName.set_alignment(0,0.5)
        self.selectedWifiImage.set_alignment(1,0.5)

        self.entry = Gtk.Entry(name="device-name")
        self.entry.set_text("************")
        self.selectedWifiBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0, name= 'wifi')
    
        self.selectedWifiBox.pack_start(self.selectedWifiName, True, True, 5)
        self.selectedWifiBox.pack_end(self.selectedWifiImage, True, True, 15)
        self.selectedWifiBox.pack_end(self.entry, True, True, 15)
        self.selectedWifiBox.set_size_request(150, 70)
        self.selectedWifiBox.set_margin_left(self._gtk.action_bar_width *2.6)
        self.selectedWifiBox.set_margin_right(self._gtk.action_bar_width*2.6)
        
        self.continueButton = Gtk.Button(i18n.t('translate.connect'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4)
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)

        

        

    
        self.main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
       
        self.main.pack_start(initHeader, False, False, 0)
        self.main.pack_end(buttonBox, False, False, 20)
        self.main.pack_end(self.selectedWifiBox, False, True, 0)
        

        
        self.content.add(self.main)
       
    def initialize(self, items):
        self.selectedMenu = items
        self.selectedWifiName.set_label(self.selectedMenu['Name'])
    
    


    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_wifi_selection_connect", "co_print_wifi_selection_connect", None, 2, True, items=self.selectedMenu)
        
   
    
  