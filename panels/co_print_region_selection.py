import logging
import os

import i18n

import gi

from ks_includes.widgets.initheader import InitHeader
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk, GdkPixbuf

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintRegionSelection(*args)


class CoPrintRegionSelection(ScreenPanel):

    def __init__(self, screen, title):
        super().__init__(screen, title)

        
        initHeader = InitHeader (self, i18n.t('translate.selectRegionHeader'),i18n.t('translate.selectRegionContent'), "Bolgesecimi")
        
        
        
        # ComboBox'u oluştur
        self.regionCombobox = Gtk.ComboBoxText.new_with_entry()
        self.regionCombobox.set_name("region-combobox")
        self.regionCombobox.set_entry_text_column(0)
        self.regionCombobox.connect("changed", self.on_combobox_changed)
        self.regionCombobox.set_margin_left(500)
        self.regionCombobox.set_margin_right(500)
        
        # Entry'ı oluştur
        self.entry = Gtk.Entry()
        self.entry.get_style_context().add_class("custom-entry")

        

        # ComboBox'a öğeler ekle
        countries = [
                    "Austria",
                    "Brazil",
                    "Belgium",
                    "France",
                    "Germany",
                    "Switzerland",
                    "United Kingdom",
                    "United States of America",
                    "Uruguay",
                    "Austria",
                    "Brazil",
                    "Belgium",
                    "France",
                    "Germany",
                    "Switzerland",
                    "United Kingdom",
                    "United States of America",
                    "Uruguay",
                    "Uruguay",
                    "Austria",
                    "Brazil",
                    "Belgium",
                    "France",
                    "Germany",
                    "Switzerland",
                    "United Kingdom",
                    "United States of America",
                    "Uruguay",
                ]
       

        self.regionCombobox.set_active(0)
        

        # Açılır listenin boyutunu ayarla
        combo_box_text = self.regionCombobox.get_child()
        style_context = combo_box_text.get_style_context()
        style_context.add_class("custom-region")
       
         
        self.listbox = Gtk.ListBox(name ="region")
        self.listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        
        for country in countries:
            label = Gtk.Label(label=country, xalign=30, name="region-menu-label")
            self.listbox.add(label)

        
        self.listbox.set_activate_on_single_click(True)
        self.listbox.connect("row-activated", self.on_listbox_row_activated)
        
        scroll = self._gtk.ScrolledWindow()
        scroll.set_kinetic_scrolling(True)
        scroll.get_overlay_scrolling()

        scroll.set_margin_left(self._gtk.action_bar_width *3.65)
        scroll.set_margin_right(self._gtk.action_bar_width*3.6)
        
        scroll.add(self.listbox)
        
        self.continueButton = Gtk.Button(i18n.t('translate.continue'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4)
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)
        
        svg_file = "styles/z-bolt/images/expand-arrow-down.svg"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(svg_file)
        self.listOpenButton = Gtk.Button(image=Gtk.Image.new_from_pixbuf(pixbuf))
        self.listOpenButton.connect("clicked", self.on_button_clicked)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        vbox.pack_start(self.entry, True, True, 0)
        vbox.pack_end(self.listOpenButton, False, True, 0)
        vbox.set_margin_left(self._gtk.action_bar_width *3.6)
        vbox.set_margin_right(self._gtk.action_bar_width*3.6)

        # Event box oluştur
        event_box = Gtk.EventBox()
        
        # Image oluştur ve event box'a ekle
        image = Gtk.Image()
        image.set_from_file("styles/z-bolt/images/Wordmapdots.png")
        event_box.add(image)
        # self.content.add(event_box)
        event_box.show_all()
        
    
        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
       
        main.pack_start(initHeader, False, False, 0)
        main.pack_end(buttonBox, False, False, 20)
        main.pack_end(scroll, False, True, 0)
        main.pack_end(vbox, False, True, 0)
        

        
        self.content.add(main)

        
    def on_country_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            country = model[tree_iter][0]
            print("Selected: country=%s" % country)

    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_product_naming", "co_print_product_naming", None, 2)
        
    def on_combobox_changed(self, combobox):
        active_text = combobox.get_active_text()
        print("Seçilen seçenek:", active_text)
        
    def on_listbox_row_activated(self, listbox, row):
        # Seçilen öğenin değerini Entry kutusuna yazdırma
        selected_value = row.get_child().get_label()
        self.entry.set_text(selected_value)
        
    def on_arrow_clicked(self, widget, event):
        # Ok simgesi tıklandığında yapılacak işlemler
        if self.listbox.get_visible():
            self.listbox.hide()
        else:
            allocation = self.entry.get_allocation()
            x, y = self.entry.translate_coordinates(self, allocation.x, allocation.y + allocation.height)
            self.listbox.set_size_request(allocation.width, -1)
            self.move(x, y)
            self.listbox.show_all()
    def on_button_clicked(self, button):
        # Listbox öğesinin görünürlüğünü tersine çevirme
        if self.listbox.get_visible():
            self.listbox.hide()
        else:
            self.listbox.show()