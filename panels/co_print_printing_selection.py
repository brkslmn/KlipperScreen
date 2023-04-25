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
    return CoPrintPrintingSelection(*args)


class CoPrintPrintingSelection(ScreenPanel):

     
    def __init__(self, screen, title):
        super().__init__(screen, title)
     
       
        initHeader = InitHeader (self, i18n.t('translate.printingSettings'), i18n.t('translate.printingSettingsSubText'), "yazicibaglama")

        self.image = self._gtk.Image("printer-connect", self._gtk.content_width * .25 , self._gtk.content_height * .25)
       
        
        self.continueButton = Gtk.Button(i18n.t('translate.searchingPrinting'),name ="flat-button-yellow")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *3)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*3)
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)

        spinner = Gtk.Spinner()
        spinner.start()

        scroll = self._gtk.ScrolledWindow()
        scroll.set_hexpand(True)
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.add(spinner)

        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main.pack_start(initHeader, True, True, 0)
        main.pack_end(buttonBox, False, True, 50)
        main.pack_end(scroll, False, False, 0)
        main.pack_end(self.image, True, True, 50)
        
       
      
        self.content.add(main)
        self._screen.base_panel.visible_menu(False)
       
    def radioButtonSelected(self, button, baudRate):
        self.selected = baudRate
    
    
    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_printing_selection_port", "co_print_printing_selection_port", None, 2)
        
   
