import logging
import os

import i18n

import gi

from ks_includes.widgets.initheader import InitHeader
from ks_includes.widgets.checkbuttonbox import CheckButtonBox
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GLib, Gdk

from ks_includes.screen_panel import ScreenPanel


def create_panel(*args):
    return CoPrintContractApproval(*args)


class CoPrintContractApproval(ScreenPanel):

    def __init__(self, screen, title):
        super().__init__(screen, title)

        confidentialityAgreement = Gtk.Label("We have a 14-day return policy, which means you have 14 days after receiving your item to request a return.\nTo be eligible for a return, your item must be in the same condition that you received it, unworn or unused, with tags, and in its original packaging. You’ll also need the receipt or proof of purchase. To start a return, you can contact us at coprint3d@gmail.com. Please note that returns will need to be sent to the address which will send.\nIf your return is accepted, we’ll send you a return shipping label, as well as instructions on how and where to send your package. Items sent back to us without first requesting a return will not be accepted. You can always contact us for any return question at coprint3d@gmail.com.\nDamages and issuesPlease inspect your order upon reception and contact us immediately if the item is defective, damaged or if you receive the wrong item, so that we can evaluate the issue and make it right.\nUnfortunately, we cannot accept returns on sale items or gift cards.\nExchangesThe fastest way to ensure you get what you want is to return the item you have, and once the return is accepted, make a separate purchase for the new item.\nEuropean Union 14 day cooling off periodNotwithstanding the above, if the merchandise is being shipped into the European Union, you have the right to cancel or return your order within 14 days, for any reason and without a justification. As above, your item must be in the same condition that you received it, unworn or unused, with tags, and in its original packaging with unopening. You’ll also need the receipt or proof of purchase. \nWe have a 14-day return policy, which means you have 14 days after receiving your item to request a return.\nTo be eligible for a return, your item must be in the same condition that you received it, unworn or unused, with tags, and in its original packaging. You’ll also need the receipt or proof of purchase. To start a return, you can contact us at coprint3d@gmail.com. Please note that returns will need to be sent to the address which will send.\nIf your return is accepted, we’ll send you a return shipping label, as well as instructions on how and where to send your package. Items sent back to us without first requesting a return will not be accepted. You can always contact us for any return question at coprint3d@gmail.com.\nDamages and issuesPlease inspect your order upon reception and contact us immediately if the item is defective, damaged or if you receive the wrong item, so that we can evaluate the issue and make it right.\nUnfortunately, we cannot accept returns on sale items or gift cards.\nExchangesThe fastest way to ensure you get what you want is to return the item you have, and once the return is accepted, make a separate purchase for the new item.\nEuropean Union 14 day cooling off periodNotwithstanding the above, if the merchandise is being shipped into the European Union, you have the right to cancel or return your order within 14 days, for any reason and without a justification. As above, your item must be in the same condition that you received it, unworn or unused, with tags, and in its original packaging with unopening. You’ll also need the receipt or proof of purchase.", name ="contract-approval-label") 
        confidentialityAgreement.set_line_wrap(True)
        
        initHeader = InitHeader (self, i18n.t('translate.confidentialityAgreementHeader'),i18n.t('translate.confidentialityAgreementContent'), "Privacy")

        scroll = self._gtk.ScrolledWindow()
        scroll.set_kinetic_scrolling(True)
        scroll.get_overlay_scrolling()
        scroll.add(confidentialityAgreement)
      
        self.continueButton = Gtk.Button(i18n.t('translate.continue'),name ="flat-button-blue")
        self.continueButton.connect("clicked", self.on_click_continue_button)
        self.continueButton.set_hexpand(True)
        self.continueButton.set_margin_left(self._gtk.action_bar_width *4)
        self.continueButton.set_margin_right(self._gtk.action_bar_width*4 )
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.pack_start(self.continueButton, False, True, 0)
        buttonBox.set_center_widget(self.continueButton)
        
        acceptButtonBox = CheckButtonBox(self, i18n.t('translate.accept'))
        
        accept = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        accept.set_margin_left(450)
        accept.set_margin_right(450)
        accept.pack_start(scroll, False, True, 0)
        accept.pack_end(acceptButtonBox, False, False, 20)
        
      
        
        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main.pack_start(initHeader, False, False, 0)
        main.pack_end(buttonBox, False, False, 20)
        main.pack_end(accept, False, True, 20)

        self.content.add(main)
        

    def on_click_continue_button(self, continueButton):
        self._screen.show_panel("co_print_region_selection", "co_print_region_selection", None, 2)
        
  
