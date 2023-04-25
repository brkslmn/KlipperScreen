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
    return CoPrintMcuModelSelection(*args)


class CoPrintMcuModelSelection(ScreenPanel):

     
    def __init__(self, screen, title):
        super().__init__(screen, title)
     
        chips = [
            {'Name': "STM32F103",  'Button': Gtk.RadioButton()},
            {'Name': "STM32F207",  'Button': Gtk.RadioButton()},
            {'Name': "STM32F401",  'Button': Gtk.RadioButton()},
            {'Name': "STM32F405", 'Button': Gtk.RadioButton()},
            {'Name': "STM32F407", 'Button': Gtk.RadioButton()},
            {'Name': "STM32F429",  'Button': Gtk.RadioButton()},
            {'Name': "STM32F446", 'Button': Gtk.RadioButton()},
            {'Name': "STM32F031", 'Button': Gtk.RadioButton()},
            {'Name': "STM32F042", 'Button': Gtk.RadioButton()},
            {'Name': "STM32F070", 'Button': Gtk.RadioButton()},
            ]
        
        self.labels['actions'] = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.labels['actions'].set_hexpand(True)
        self.labels['actions'].set_vexpand(False)
        self.labels['actions'].set_halign(Gtk.Align.CENTER)
        self.labels['actions'].set_homogeneous(True)
        self.labels['actions'].set_size_request(self._gtk.content_width, -1)

       
        initHeader = InitHeader (self, i18n.t('translate.mcuModelHeader'), i18n.t('translate.mcuModelContent'), "mikrochip")

    
        '''diller bitis'''
        
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
        
        self.show_restart_buttons()
      
        self.content.add(main)
        self._screen.base_panel.visible_menu(False)
        
    def radioButtonSelected(self, button, baudRate):
        self.selected = baudRate
       
    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_mcu_bootloader_ofset", "co_print_mcu_bootloader_ofset", None, 2)
        
   

    def update_text(self, text):
        
        self.show_restart_buttons()

    def clear_action_bar(self):
        for child in self.labels['actions'].get_children():
            self.labels['actions'].remove(child)

    def show_restart_buttons(self):

        self.clear_action_bar()
        if self.ks_printer_cfg is not None and self._screen._ws.connected:
            power_devices = self.ks_printer_cfg.get("power_devices", "")
            if power_devices and self._printer.get_power_devices():
                logging.info(f"Associated power devices: {power_devices}")
                self.add_power_button(power_devices)

      

    def add_power_button(self, powerdevs):
        self.labels['power'] = self._gtk.Button("shutdown", _("Power On Printer"), "color3")
        self.labels['power'].connect("clicked", self._screen.power_devices, powerdevs, True)
        self.check_power_status()
        self.labels['actions'].add(self.labels['power'])

    def activate(self):
        self.check_power_status()
        self._screen.base_panel.show_macro_shortcut(False)
        self._screen.base_panel.show_heaters(False)
        self._screen.base_panel.show_estop(False)

    def check_power_status(self):
        if 'power' in self.labels:
            devices = self._printer.get_power_devices()
            if devices is not None:
                for device in devices:
                    if self._printer.get_power_device_status(device) == "off":
                        self.labels['power'].set_sensitive(True)
                        break
                    elif self._printer.get_power_device_status(device) == "on":
                        self.labels['power'].set_sensitive(False)

    def firmware_restart(self, widget):
        self._screen._ws.klippy.restart_firmware()

    def restart(self, widget):
        self._screen._ws.klippy.restart()

    def shutdown(self, widget):
        if self._screen._ws.connected:
            self._screen._confirm_send_action(widget,
                                              _("Are you sure you wish to shutdown the system?"),
                                              "machine.shutdown")
        else:
            logging.info("OS Shutdown")
            os.system("systemctl poweroff")

    def restart_system(self, widget):

        if self._screen._ws.connected:
            self._screen._confirm_send_action(widget,
                                              _("Are you sure you wish to reboot the system?"),
                                              "machine.reboot")
        else:
            logging.info("OS Reboot")
            os.system("systemctl reboot")

    def retry(self, widget):
        self.update_text((_("Connecting to %s") % self._screen.connecting_to_printer))
        if self._screen._ws and not self._screen._ws.connecting:
            self._screen._ws.retry()
        else:
            self._screen.reinit_count = 0
            self._screen.init_printer()
        self.show_restart_buttons()
