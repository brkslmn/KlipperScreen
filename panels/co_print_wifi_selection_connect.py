import logging
import os

import i18n

import gi

from ks_includes.widgets.initheader import InitHeader
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk, GdkPixbuf

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintWifiSelectionConnect(*args)


class CoPrintWifiSelectionConnect(ScreenPanel):

    def __init__(self, screen, title):
        super().__init__(screen, title)

        image = self._gtk.Image("wifi-connected", self._gtk.content_width * .25 , self._gtk.content_height * .25)
        subTitle = Gtk.Label(i18n.t('translate.connected'), name="init-header-subtitle-label")
       
        selectBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
       
        selectBox.pack_start(image, False, True, 10)
        selectBox.pack_end(subTitle, False, False, 10)
        
        
        # ComboBox'a öğeler ekle
        
        self.selectedWifiImage = self._gtk.Image("sinyal", self._gtk.content_width * .05 , self._gtk.content_height * .05)
        self.selectedWifiName = Gtk.Label("",name ="wifi-label")
        self.selectedWifiName.set_alignment(0,0.5)
        self.selectedWifiImage.set_alignment(1,0.5)

        
        self.selectedWifiBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0, name= 'wifi')
    
        self.selectedWifiBox.pack_start(self.selectedWifiName, True, True, 5)
        self.selectedWifiBox.pack_end(self.selectedWifiImage, True, True, 15)
        self.selectedWifiBox.set_size_request(150, 70)
        self.selectedWifiBox.set_margin_left(self._gtk.action_bar_width *3)
        self.selectedWifiBox.set_margin_right(self._gtk.action_bar_width*3)
        
        self.continueButton = Gtk.Button(i18n.t('translate.continue'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4)
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)

        

        

    
        self.main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
       
        self.main.pack_start(selectBox, False, False, 0)
        self.main.pack_end(buttonBox, False, False, 20)
        self.main.pack_end(self.selectedWifiBox, False, True, 0)
        

        
        self.content.add(self.main)
       
    def initialize(self, items):
        self.selectedMenu = items
        self.selectedWifiName.set_label(self.selectedMenu['Name'])
    
    


    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_chip_selection", "co_print_chip_selection", None, 2)
        
   
    
  