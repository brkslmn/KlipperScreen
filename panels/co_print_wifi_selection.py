import logging
import os

import i18n

import gi

from ks_includes.widgets.initheader import InitHeader
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk, GdkPixbuf

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintWifiSelection(*args)


class CoPrintWifiSelection(ScreenPanel):

    def __init__(self, screen, title):
        super().__init__(screen, title)

        
        initHeader = InitHeader (self, i18n.t('translate.selectWifiHeader'),i18n.t('translate.selectWifiContent'), "wifi")
        
        # ComboBox'a öğeler ekle
        self.wifies = [
            {'Name': "Wifi-Secenek 1", 'Icon': 'sinyal'},
            {'Name': "Wifi-Secenek 2", 'Icon': 'sinyal'},
            {'Name': "Wifi-Secenek 3", 'Icon': 'sinyal'},
            {'Name': "Wifi-Secenek 4", 'Icon': 'sinyal'},
            {'Name': "Wifi-Secenek 5", 'Icon': 'sinyal'},
            {'Name': "Wifi-Secenek 6", 'Icon': 'sinyal'},
            
            ]

       
         
        listbox = Gtk.ListBox(name ="wifi")
        listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        listbox.connect("selected_rows_changed",self.wifiChanged)
        
        for wifi in self.wifies:
            wifiImage = self._gtk.Image(wifi['Icon'], self._gtk.content_width * .05 , self._gtk.content_height * .05)
            wifiName = Gtk.Label(wifi['Name'],name ="wifi-label")
            wifiName.set_alignment(0,0.5)
            wifiImage.set_alignment(1,0.5)
            wifiBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20, name= 'wifi')
            
            wifiBox.pack_start(wifiName, True, True, 5)
            wifiBox.pack_end(wifiImage, True, True, 15)
            wifiBox.set_size_request(150, 70)
            listbox.add(wifiBox)

        
       
        
        self.scroll = self._gtk.ScrolledWindow()
        self.scroll.set_kinetic_scrolling(True)
        self.scroll.get_overlay_scrolling()
        self.scroll.set_margin_left(self._gtk.action_bar_width *2.6)
        self.scroll.set_margin_right(self._gtk.action_bar_width*2.6)
        
        self.scroll.add(listbox)
        
        self.continueButton = Gtk.Button(i18n.t('translate.continue'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4)
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)

        

        

    
        self.main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
       
        self.main.pack_start(initHeader, False, False, 0)
        self.main.pack_end(self.scroll, False, True, 0)
        

        
        self.content.add(self.main)
       
        
    
    def wifiChanged(self, listbox):
       selected = listbox.get_selected_row()
       self.selectedWifiIndex = selected.get_index()
       self._screen.show_panel("co_print_wifi_selection_select", "co_print_wifi_selection_select", None, 2, True, items=self.wifies[self.selectedWifiIndex])
       
       


    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_wifi_selection_select", "co_print_wifi_selection_select", None, 2, True, items=self.wifies[self.selectedWifiIndex])
        
   
    
  