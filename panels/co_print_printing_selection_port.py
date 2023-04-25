import logging
import os
from ks_includes.widgets.checkbuttonbox import CheckButtonBox
import gi
import i18n

from ks_includes.widgets.initheader import InitHeader
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk, GdkPixbuf

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintPrintingSelectionPort(*args)


class CoPrintPrintingSelectionPort(ScreenPanel):

     
    def __init__(self, screen, title):
        super().__init__(screen, title)
     
       
        initHeader = InitHeader (self, i18n.t('translate.printingSettings'), i18n.t('translate.printingSettingsSubText'), "yazicibaglama")

         
        self.continueButton = Gtk.Button(i18n.t('translate.continue'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4)
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)


        self.portOne = Gtk.Button("usb-0:1:1.0-port0",name ="flat-button-black")
       
        self.portOne.set_hexpand(True)
        self.portOne.set_margin_left(self._gtk.action_bar_width *4)
        self.portOne.set_margin_right(self._gtk.action_bar_width*4)
        portOneBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        portOneBox.pack_start(self.portOne, False, True, 0)
        portOneBox.set_center_widget(self.portOne)


        self.portTwo = Gtk.Button("usb-0:1:1.0-port1",name ="flat-button-black")
        
        self.portTwo.set_hexpand(True)
        self.portTwo.set_margin_left(self._gtk.action_bar_width *4)
        self.portTwo.set_margin_right(self._gtk.action_bar_width*4)
        portTwoBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        portTwoBox.pack_start(self.portTwo, False, True, 0)
        portTwoBox.set_center_widget(self.portTwo)

        
        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main.pack_start(initHeader, True, True, 0)
        main.pack_end(buttonBox, False, True, 50)
        main.pack_end(portOneBox, False, False, 0)
        main.pack_end(portTwoBox, True, True, 50)
        
       
      
        self.content.add(main)
        self._screen.base_panel.visible_menu(False)
       
    def radioButtonSelected(self, button, baudRate):
        self.selected = baudRate
    
    
    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_printing_brand_selection", "co_print_printing_brand_selection", None, 2)
        
   
