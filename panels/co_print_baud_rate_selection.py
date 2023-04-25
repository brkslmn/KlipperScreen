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
            {'Name': "9600",  'Button': Gtk.RadioButton()},
            {'Name': "14400",  'Button': Gtk.RadioButton()},
            {'Name': "19200",  'Button': Gtk.RadioButton()},
            {'Name': "38400", 'Button': Gtk.RadioButton()},
            {'Name': "57600", 'Button': Gtk.RadioButton()},
            {'Name': "115200",  'Button': Gtk.RadioButton()},
            {'Name': "128000", 'Button': Gtk.RadioButton()},
            {'Name': "256000", 'Button': Gtk.RadioButton()},
            ]
        
        self.labels['actions'] = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.labels['actions'].set_hexpand(True)
        self.labels['actions'].set_vexpand(False)
        self.labels['actions'].set_halign(Gtk.Align.CENTER)
        self.labels['actions'].set_homogeneous(True)
        self.labels['actions'].set_size_request(self._gtk.content_width, -1)

       
        initHeader = InitHeader (self, i18n.t('translate.baudRateSettings'), i18n.t('translate.baudRateSettingsSubText'), "mikrochip")

        '''diller'''
        grid = Gtk.Grid(column_homogeneous=True,
                         column_spacing=10,
                         row_spacing=10)
        row = 0
        count = 0
        
        group =chips[0]['Button']
        for chip in chips:
            chipName = Gtk.Label(chip['Name'],name ="wifi-label")
            chipName.set_alignment(0,0.5)
            
            chip['Button'] = Gtk.RadioButton.new_with_label_from_widget(group,"")
            if chips[0]['Name'] == chip['Name']:
                 chip['Button'] = Gtk.RadioButton.new_with_label_from_widget(None,"")
           
           
            
            chip['Button'].connect("toggled",self.radioButtonSelected, chip['Name'])
            chip['Button'].set_alignment(1,0.5)
            chipBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50, name="chip")
           
            f = Gtk.Frame(name="chip")
            chipBox.pack_start(chipName, False, True, 10)
           
            chipBox.pack_end(chip['Button'], False, False, 10)
            
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
        main.pack_end(self.scroll, True, True, 50)
        
       
      
        self.content.add(main)
        self._screen.base_panel.visible_menu(False)
       
    def radioButtonSelected(self, button, baudRate):
        self.selected = baudRate
    
    
    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_sd_card_selection", "co_print_sd_card_selection", None, 2)
        
   
