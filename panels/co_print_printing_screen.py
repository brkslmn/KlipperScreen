import logging
import os
from ks_includes.widgets.bottommenu import BottomMenu
from ks_includes.widgets.checkbuttonbox import CheckButtonBox
import gi
import i18n

from ks_includes.widgets.initheader import InitHeader
from ks_includes.widgets.progressbar import ProgressBar
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk, GdkPixbuf

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintPrintingScreen(*args)


class CoPrintPrintingScreen(ScreenPanel):

     
    def __init__(self, screen, title):
        super().__init__(screen, title)
        
       
        self.labels['file'] = Gtk.Label("Printing File: benchy.gcode")
        self.labels['file'].get_style_context().add_class("printing-filename")
        self.labels['file'].set_hexpand(True)
        self.labels['status'] = Gtk.Label("Tahmini Süre: 0g. 02d. 30s.") 
        self.labels['status'].get_style_context().add_class("printing-status")
     
       
        ''' left '''
        self.labels['thumbnail'] = self._gtk.Image("file", self._screen.width / 3, self._screen.height / 3)
        self.labels['thumbnail'].get_style_context().add_class("thumbnail")
        
        
        heatedBed_box = ProgressBar(self, "30° / 60°", "tablaicon", 0.5, "progress-bar-extruder-yellow")
        extruder_box = ProgressBar(self, "100° / 200°", "extrudericon", 0.5, "progress-bar-extruder-blue")
        
        

        left_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        left_box.add(self.labels['thumbnail'])
        left_box.add(extruder_box)
        left_box.add(heatedBed_box)
        ''''''
        
        self.buttons = {}
        self.create_buttons()
        for button in self.buttons: 
            self.buttons[button].set_halign(Gtk.Align.START)
            self.buttons[button].set_valign(Gtk.Align.START)
          
          
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        
        button_box.add(self.buttons['pause'])
        button_box.add(self.buttons['cancel'])
        
        fi_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 10)
        
        fi_box.pack_start(self.labels['file'], True, True, 0)
        fi_box.pack_start(self.labels['status'], True, True, 0)
        self.labels['file'].set_halign(Gtk.Align.START)
        self.labels['status'].set_halign(Gtk.Align.START)
        
        rightInfo_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        rightInfo_box.add(fi_box)
        rightInfo_box.add(button_box)
        rightInfo_box.set_valign(Gtk.Align.CENTER)
        
        scale_printProgress = Gtk.ProgressBar(name ="progress-bar-print")
        scale_printProgress.set_fraction(0.7)
        scale_printProgress.set_show_text(False)
        scale_printProgress.set_hexpand(True) 
        


        

        extruders = [
            {'Name': '1', 'Icon': 'e_1_open'},
            {'Name': '2', 'Icon': 'e_1_open'},
            {'Name': '3', 'Icon': 'e_1_open'},
            {'Name': '4', 'Icon': 'e_1_open'},
            {'Name': '5', 'Icon': 'e_1_open'},
            {'Name': '6', 'Icon': 'e_1_open'},
            {'Name': '7', 'Icon': 'e_1_open'},
            {'Name': '8', 'Icon': 'e_1_open'},
            ]
        
        grid = Gtk.Grid(column_homogeneous=True,
                         column_spacing=10,
                         row_spacing=10)
        row = 0
        count = 0
        

        for language in extruders:
            
            languageImage = self._gtk.Image(language['Icon'], self._gtk.content_width * .15 , self._gtk.content_height * .15)
            
            languageBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            f = Gtk.Frame(name= "chip")
            languageBox.pack_start(languageImage, False, True, 5)
            languageBox.set_size_request(50, 50)
            f.add(languageBox)
            grid.attach(f, count, row, 1, 1)
            count += 1
            if count % 4 is 0:
                count = 0
                row += 1

        speedFactorLabel = Gtk.Label("200° / 200°",name ="progress-label")

        scale_speedFactor = Gtk.ProgressBar(name ="progress-bar-extruder")
        scale_speedFactor.set_fraction(0.7)
        scale_speedFactor.set_show_text(False)
        scale_speedFactor.set_hexpand(True)

        speedFactor_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        speedFactor_box.add(self._gtk.Image("extrudericon", 50, 50))
        speedFactor_box.add(speedFactorLabel)
        speedFactor_box.add(scale_speedFactor)
        speedFactor_box.set_valign(Gtk.Align.CENTER)

        
        
        extrusionFactorLabel = Gtk.Label("200° / 200°",name ="progress-label")

        scale_extrusionFactor = Gtk.ProgressBar(name ="progress-bar-extruder")
        scale_extrusionFactor.set_fraction(0.7)
        scale_extrusionFactor.set_show_text(False)
        scale_extrusionFactor.set_hexpand(True)

        extrusionFactor_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        extrusionFactor_box.add(self._gtk.Image("extrudericon", 50, 50))
        extrusionFactor_box.add(extrusionFactorLabel)
        extrusionFactor_box.add(scale_extrusionFactor)
        extrusionFactor_box.set_valign(Gtk.Align.CENTER)

        gridBox = Gtk.FlowBox()
        gridBox.set_halign(Gtk.Align.CENTER)
        gridBox.add(speedFactor_box)
        
        gridBox.add(grid)
        gridBox.add(extrusionFactor_box)

        scroll = self._gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.set_kinetic_scrolling(True)
        scroll.get_overlay_scrolling()
        scroll.set_hexpand(True)
        scroll.add(gridBox)
        scroll.set_min_content_height(self._screen.height / 2)
        right_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        right_box.pack_start(rightInfo_box, True, False, 0)
        right_box.pack_start(scale_printProgress, True, False, 0)
        right_box.pack_end(scroll, False, True, 0)
       
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        main_box.pack_start(left_box, True, True, 0)
        main_box.pack_start(right_box, True, True, 0)
        main_box.set_valign(Gtk.Align.CENTER)
        
       
        
        pagee = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        pagee.pack_start(main_box, True, True, 0)
      
        pagee.pack_end(BottomMenu(), False, True, 0)
        
        self.content.add(pagee)

    def show_file_thumbnail(self):
            if self._files.has_thumbnail(self.filename):
                if self._screen.vertical_mode:
                    width = self._screen.width * 0.9
                    height = self._screen.height / 4
                else:
                    width = self._screen.width / 3
                    height = self._gtk.content_height * 0.47
                pixbuf = self.get_file_image(self.filename, width, height)
                if pixbuf is not None:
                    self.labels['thumbnail'].set_from_pixbuf(pixbuf)     
        
    def update_filename(self):
        self.filename = self._printer.get_stat('print_stats', 'filename')
        self.labels["file"].set_label(os.path.splitext(self.filename)[0])
        self.filename_label = {
            "complete": self.labels['file'].get_label(),
            "current": self.labels['file'].get_label(),
            "position": 0,
            "limit": (self._screen.width * 37 / 480) // (self._gtk.font_size / 11),
            "length": len(self.labels['file'].get_label())
        }
        if self.animation_timeout is None and (self.filename_label['length'] - self.filename_label['limit']) > 0:
            self.animation_timeout = GLib.timeout_add_seconds(1, self.animate_label)
        self.update_percent_complete()
        self.update_file_metadata()

    def animate_label(self):
        pos = self.filename_label['position']
        if pos > (self.filename_label['length'] - self.filename_label['limit']):
            self.filename_label['position'] = 0
            self.labels['file'].set_label(self.filename_label['complete'])
        else:
            self.labels['file'].set_label(self.filename_label['current'][pos:self.filename_label['length']])
            self.filename_label['position'] += 1
        return True  
    
    def create_buttons(self):

        self.buttons = {
            'cancel': self._gtk.Button("close_print", None, "close", .5),
            'pause': self._gtk.Button("pause_print", None, "pause", .5),

        }
        self.buttons['cancel'].connect("clicked", self.cancel)
        
    def cancel(self, widget):
        buttons = [
            {"name": _("Cancel Print"), "response": Gtk.ResponseType.OK},
            {"name": _("Go Back"), "response": Gtk.ResponseType.CANCEL}
        ]
        if len(self._printer.get_stat("exclude_object", "objects")) > 1:
            buttons.insert(0, {"name": _("Exclude Object"), "response": Gtk.ResponseType.APPLY})
        label = Gtk.Label()
        label.set_markup(_("Are you sure you wish to cancel this print?"))
        label.set_hexpand(True)
        label.set_halign(Gtk.Align.CENTER)
        label.set_vexpand(True)
        label.set_valign(Gtk.Align.CENTER)
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)

