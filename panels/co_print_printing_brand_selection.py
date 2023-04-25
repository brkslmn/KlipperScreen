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
    return CoPrintPrintingBrandSelection(*args)


class CoPrintPrintingBrandSelection(ScreenPanel):

     
    def __init__(self, screen, title):
        super().__init__(screen, title)
     
        initHeader = InitHeader (self, i18n.t('translate.printingSettings'), i18n.t('translate.printingSettingsSubText'), "yazicibaglama")
        
        self.image = self._gtk.Image("Creality-Ender-3-Pro", self._gtk.content_width * .5 , self._gtk.content_height * .5)
        
        #finish button  
        self.continueButton = Gtk.Button(i18n.t('translate.finish'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4)
        self.continueButton.set_always_show_image (True)
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)
        
        #treePrinterList--start--
        tree = Gtk.TreeView(name="tree-list")
        
        store = Gtk.TreeStore(bool, str)
        tree.set_model(store)
        
        
        iter1 = store.append(None,[None, "Creality"])
        iter2 = store.append(None, [None, "Anet"])
        iter3 = store.append(None, [None, "Anet"])
        
        
        store.append(iter1, [True, "Creality Ender 3 Pro"])
        store.append(iter1, [False, "Creality Ender 3 V2"])
        store.append(iter1, [False, "Creality CR 10 2017"])
        store.append(iter1, [False, "Creality CR 10 Smart Pro 2022"])
        store.append(iter1, [False, "Creality CR 10 v3"])
        store.append(iter1, [False, "Creality Ender 3 V2"])
        store.append(iter1, [False, "Creality CR 10 2017"])
        store.append(iter1, [False, "Creality CR 10 Smart Pro 2022"])
        store.append(iter1, [False, "Creality CR 10 v3"])
        
        
        store.append(iter2, [None, "Anet a4 2018"])
        store.append(iter2, [None, "Anet a8 2017"])
        store.append(iter2, [None, "Anet a8 2019"])
        store.append(iter2, [None, "Anet E10"])
        store.append(iter2, [None, "Anet E16"])
        store.append(iter2, [None, "Anet a8 2019"])
        store.append(iter2, [None, "Anet E10"])
        store.append(iter2, [None, "Anet E16"])
        
        store.append(iter3, [None, "Anet a4 2018"])
        store.append(iter3, [None, "Anet a8 2017"])
        store.append(iter3, [None, "Anet a8 2019"])
        store.append(iter3, [None, "Anet E10"])
        store.append(iter3, [None, "Anet E16"])
        store.append(iter3, [None, "Anet a8 2019"])
        store.append(iter3, [None, "Anet E10"])
        store.append(iter3, [None, "Anet E16"])
        
        # create a column
        column = Gtk.TreeViewColumn()
        tree.append_column(column)
        # add a toggle render
        toggle = Gtk.CellRendererToggle()
        column.pack_start(toggle, True)
        column.add_attribute(toggle, "active", 0)
        toggle.set_radio(True)
        # and add a text renderer to the same column
        text_ren = Gtk.CellRendererText()
        column.pack_start(text_ren, True)
        column.add_attribute(text_ren, "text", 1)
        
        tree.expand_all()
        select = tree.get_selection()
        select.connect("changed", self.on_tree_selection_changed)
        tree.get_selection().set_mode(Gtk.SelectionMode.SINGLE)
        #treePrinterList--end--

        scroll = self._gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.set_kinetic_scrolling(True)
        scroll.get_overlay_scrolling()
        scroll.set_hexpand(True)
        scroll.add(tree)
        
        selectedPrinterName= Gtk.Label("Creality Ender 3 Pro", name="selected-printer-name")
        selectedPrinterDimension = Gtk.Label(i18n.t('translate.dimension') + ": " + "235mm × 235mm x 300mm", name="selected-printer-dimension")
        selectedPrinterBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        selectedPrinterBox.pack_start(self.image, False, True, 0)
        selectedPrinterBox.pack_start(selectedPrinterName, False, True, 10)
        selectedPrinterBox.pack_start(selectedPrinterDimension, False, True, 0)
        selectedPrinterBox.set_hexpand(True)

        pageBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        pageBox.set_hexpand(True)
        pageBox.set_margin_left(self._gtk.action_bar_width *2.5)
        pageBox.set_margin_right(self._gtk.action_bar_width*2.5)
        pageBox.pack_start(scroll, False, True, 50)
        pageBox.pack_start(selectedPrinterBox, False, True, 0)
        
        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main.pack_start(initHeader, False, False, 0)
        main.pack_start(pageBox, False, True, 0)
        main.pack_end(buttonBox, False, True, 50)
        #main.pack_end(menuBox, False, True, 50)
       
      
        self.content.add(main)
        self._screen.base_panel.visible_menu(False)
       
    def radioButtonSelected(self, button, baudRate):
        self.selected = baudRate
    
    
    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_printing_screen", "co_print_printing_screen", None, 2)
        
    def on_tree_selection_changed(selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            print("You selected", model[treeiter][0])
            
            
        
   
