import logging
import os

import gi
import i18n

from ks_includes.widgets.initheader import InitHeader
from ks_includes.widgets.selectionbox import SelectionBox
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintSplashScreenPanel(*args)


class CoPrintSplashScreenPanel(ScreenPanel):

     
    def __init__(self, screen, title):
        super().__init__(screen, title)
     
        languages = [
            {'Lang':'en' ,'Name': i18n.t('translate.english'), 'Icon': 'English', 'Button': Gtk.RadioButton()},
            {'Lang':'fr' ,'Name': i18n.t('translate.french'), 'Icon': 'France', 'Button': Gtk.RadioButton()},
            {'Lang':'ge' ,'Name': i18n.t('translate.german'), 'Icon': 'Germany', 'Button': Gtk.RadioButton()},
            {'Lang':'tr' ,'Name': i18n.t('translate.turkish'), 'Icon': 'Turkey', 'Button': Gtk.RadioButton()},
            {'Lang':'it' ,'Name': i18n.t('translate.italian'), 'Icon': 'Italy', 'Button': Gtk.RadioButton()},
            {'Lang':'sp' ,'Name': i18n.t('translate.spanish'), 'Icon': 'Spain', 'Button': Gtk.RadioButton()},
            
            ]
        
        self.labels['actions'] = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.labels['actions'].set_hexpand(True)
        self.labels['actions'].set_vexpand(False)
        self.labels['actions'].set_halign(Gtk.Align.CENTER)
        self.labels['actions'].set_homogeneous(True)
        self.labels['actions'].set_size_request(self._gtk.content_width, -1)

       
        infoo = InitHeader (self, i18n.t('translate.selectLanguage'), i18n.t('translate.languageSettings'), "Geography")
        # selectionBox = SelectionBox (self, i18n.t('translate.mcuArchitecture'), "expand-arrow-right")
        # selectionBox.set_size_request(377, 97)

        # '''Burasi widget olacak'''
        # image = self._gtk.Image("Geography", self._gtk.content_width * .1 , self._gtk.content_height * .1)
        # subTitle = Gtk.Label( i18n.t('translate.languageSettings'))
        # subText = Gtk.Label()
        # '''Lütfen sistem dilini belirleyiniz'''
        # subText.set_markup("<span  font='18' color='#9A9A9A'>" + i18n.t('translate.selectLanguage') +"</span>")

        # info = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
       
        # info.pack_start(image, False, True, 10)
        # info.pack_end(subText, False, False, 10)
        # info.pack_end(subTitle, False, False, 10)
        # '''Wigget Bitis'''


        '''diller'''
        grid = Gtk.Grid(column_homogeneous=True,
                         column_spacing=10,
                         row_spacing=10)
        row = 0
        count = 0
        group =  [x for x in languages if x['Lang'] == i18n.get('locale')][0]['Button']
       
       
        for language in languages:
            
            languageImage = self._gtk.Image(language['Icon'], self._gtk.content_width * .05 , self._gtk.content_height * .05)
            languageName = Gtk.Label(language['Name'],name ="language-label")
            language['Button'] = Gtk.RadioButton.new_with_label_from_widget(group,"")
            if i18n.get('locale') == language['Lang']:
                 language['Button'] = Gtk.RadioButton.new_with_label_from_widget(None,"")
           
           
            
            language['Button'].connect("toggled",self.radioButtonSelected, language['Lang'])
            
             
            languageBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            f = Gtk.Frame()
            languageBox.pack_start(languageImage, False, True, 5)
            languageBox.pack_end(language['Button'], False, False, 5)
            languageBox.pack_end(languageName, True, True, 5)
            languageBox.set_size_request(50, 50)
            f.add(languageBox)
            grid.attach(f, count, row, 1, 1)
            count += 1
            if count % 2 is 0:
                count = 0
                row += 1


       
        
        gridBox = Gtk.FlowBox()
        gridBox.set_halign(Gtk.Align.CENTER)
        gridBox.add(grid)
        '''diller bitis'''
        
        
        
        self.continueButton = Gtk.Button(i18n.t('translate.continue'),name ="flat-button-blue")
        
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4 )
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)
       
        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main.pack_start(infoo, True, True, 0)
        main.pack_end(buttonBox, False, True, 50)
        main.pack_end(gridBox, True, False, 50)
        
        self.show_restart_buttons()
      
        self.content.add(main)
        self._screen.base_panel.visible_menu(False)
       
    def radioButtonSelected(self, button, lang):
        i18n.set('locale', lang)
        self._screen._remove_all_panels()
        #self._screen.reload_panels()
        self._screen.show_panel("co_print_splash_screen", "co_print_splash_screen", "Language", 2, True)


    def _resolve_radio(self, master_radio):
        active = next((
        radio for radio in
        master_radio.get_group()
        if radio.get_active()
        ))
        return active

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
