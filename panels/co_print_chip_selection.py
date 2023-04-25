import logging
import os
from ks_includes.widgets.checkbuttonbox import CheckButtonBox
import gi
import i18n

from ks_includes.widgets.initheader import InitHeader
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintChipSelection(*args)


class CoPrintChipSelection(ScreenPanel):

     
    def __init__(self, screen, title):
        super().__init__(screen, title)
     
        chips = [
            {'Name': "MCU Architecture"},
            {'Name': "Botloader Offset"},
            {'Name': "Processor Model"},
            {'Name': "Com Interface"},
            {'Name': "Clock Referance"},
            ]
        
      
       
        initHeader = InitHeader (self, i18n.t('translate.chipSettings'), i18n.t('translate.chipSettingsSubText'), "mikrochip")

        '''diller'''
        grid = Gtk.Grid(column_homogeneous=True,
                         column_spacing=10,
                         row_spacing=10)
        row = 0
        count = 0
        
       
        for chip in chips:
            chipImage = self._gtk.Image("expand-arrow-right", self._gtk.content_width * .05 , self._gtk.content_height * .05)
            chipName = Gtk.Label(chip['Name'],name ="wifi-label")
            chipName.set_alignment(0,0.5)
            chipImage.set_alignment(1,0.5)
            
           
            chipBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50, name="chip")
            f = Gtk.Frame(name="chip")
            chipBox.pack_start(chipName, False, True, 10)
           
            chipBox.pack_end(chipImage, True, True, 10)
            
            f.add(chipBox)
            grid.attach(f, count, row, 1, 1)
            count += 1
            if count % 2 is 0:
                count = 0
                row += 1


       
        
        gridBox = Gtk.FlowBox()
        gridBox.set_halign(Gtk.Align.CENTER)
        gridBox.add(grid)
        '''diller bitis'''
        
        self.scroll = self._gtk.ScrolledWindow()
        self.scroll.set_kinetic_scrolling(True)
        self.scroll.get_overlay_scrolling()
        self.scroll.set_margin_left(self._gtk.action_bar_width *2.6)
        self.scroll.set_margin_right(self._gtk.action_bar_width*2.6)
        
        self.scroll.add(gridBox)
        
        self.checkButton = CheckButtonBox(self, i18n.t('translate.enableLowLevelOptions'))
        
        self.checkButton.set_hexpand(True)
        self.checkButton.set_margin_left(self._gtk.action_bar_width *3)
        self.checkButton.set_margin_right(self._gtk.action_bar_width*3)
        checkButtonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        checkButtonBox.pack_start(self.checkButton, False, True, 0)
        checkButtonBox.set_center_widget(self.checkButton)
        

        self.continueButton = Gtk.Button(i18n.t('translate.continue'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4)
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)


        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main.pack_start(initHeader, True, True, 0)
        main.pack_end(buttonBox, False, True, 50)
        main.pack_end(checkButtonBox, False, True, 50)
        main.pack_end(self.scroll, True, True, 50)
        
     
      
        self.content.add(main)
        self._screen.base_panel.visible_menu(False)
       
    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_mcu_selection", "co_print_mcu_selection", None, 2)
        
   

