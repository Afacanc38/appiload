selamun = "aleyküm"

import gi, os
gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "1")
from gi.repository import Gtk, Handy

Handy.init()

class MyWindow(Handy.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.set_default_size(500, 300)

        # WindowHandle
        self.handle = Handy.WindowHandle()
        self.add(self.handle)

        # WinBox
        self.winBox = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        self.handle.add(self.winBox)

        # Revealer
        self.revealer = Gtk.Revealer()
        self.revealer.set_reveal_child(True)
        self.winBox.pack_start(self.revealer, False, True, 0)

        # Headerbar
        self.hb = Handy.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.props.title = "Revealer Example"
        self.revealer.add(self.hb)

        # MainBox
        self.mainBox = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL, halign=Gtk.Align.CENTER, valign=Gtk.Align.CENTER)
        self.winBox.pack_start(self.mainBox, True, False, 0)

        # Revealer button
        self.rvBtn = Gtk.Button(label="Hide headerbar")
        self.mainBox.pack_start(self.rvBtn, True, False, 0)
        self.rvBtn.connect("clicked", self.on_rvBtn_clicked)

    def on_rvBtn_clicked(self, widget):
        reveal = self.revealer.get_reveal_child()
        if reveal == True:
            self.revealer.set_reveal_child(False)
            self.rvBtn.set_label("Show headerbar")
        else:
            self.revealer.set_reveal_child(True)
            self.rvBtn.set_label("Hide headerbar")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()