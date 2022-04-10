import os
import subprocess
import sys
import gi
gi.require_version ("Gtk", "4.0")
gi.require_version ("Adw", "1")
from gi.repository import Gtk, Adw, GLib

class functions():
    def add_class(widget, style):
        widget.get_style_context().add_class(style)
    
    def clicked(widget, function):
        widget.connect("clicked", function)


class InstallerWindow (Adw.Window):
    def __init__ (self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
        # Pencere başlığı ve uygulama adı
        GLib.set_application_name ("Uygulama Kur")
        GLib.set_prgname ("Appiload")
        self.set_default_size (1, 1)

        # Başlık çubuğu olmayan bir pencereyi sürüklenebilir yapar
        self.win_hdl = Gtk.WindowHandle (
            halign = Gtk.Align.CENTER,
            valign = Gtk.Align.CENTER
        )
        self.set_content (self.win_hdl)

        # Uygulama içinde sayfalar
        self.stk_main = Gtk.Stack ()
        self.stk_main.set_transition_type(Gtk.StackTransitionType.NONE)
        self.win_hdl.set_child (self.stk_main)

        # Pencere kenarlarına yapışık kalmamasını sağlar
        self.stk_main.set_margin_top(20)
        self.stk_main.set_margin_bottom(20)
        self.stk_main.set_margin_start(20)
        self.stk_main.set_margin_end(20)

        # Soru kısmı
        self.box_0 = Gtk.Box(
            spacing = 10,
            halign = Gtk.Align.FILL,
            orientation = Gtk.Orientation.HORIZONTAL
        )
        self.stk_main.add_titled (
            self.box_0,
            "page0",
            "Soru"
        )
        
        # Simge
        self.img_question = Gtk.Image.new_from_icon_name ("dialog-question-symbolic")
        self.img_question.set_icon_size (Gtk.IconSize.LARGE)
        self.box_0.append (
            self.img_question
        )

        # Soru
        self.lbl_question = Gtk.Label(
            label = "Bu uygulamayı kurmak istiyor musunuz?"
        )
        self.box_0.append (self.lbl_question)

        # Düğme kutusu
        self.box_0_btn = Gtk.Box(
            spacing = 6,
            orientation = Gtk.Orientation.HORIZONTAL,
            halign = Gtk.Align.END
        )
        self.box_0.append(self.box_0_btn)

        # Düğmeler
        self.btn_install = Gtk.Button(
            label = "Kur"
        )
        functions.add_class(self.btn_install, "suggested-action")
        functions.clicked(self.btn_install, self.on_install_clicked)
        self.box_0_btn.append(self.btn_install)

        self.btn_cancel = Gtk.Button(
            label = "İptal"
        )
        functions.clicked(self.btn_cancel, self.on_cancel_clicked)
        self.box_0_btn.append(self.btn_cancel)

        # Kurulum ilerlemesi
        self.box_1 = Gtk.Box(
            spacing = 10,
            halign = Gtk.Align.FILL,
            orientation = Gtk.Orientation.HORIZONTAL
        )
        self.stk_main.add_titled (
            self.box_1,
            "page1",
            "Soru"
        )

        # Kuruluyor
        self.img_installing = Gtk.Image.new_from_icon_name ("insert-object-symbolic")
        self.img_installing.set_icon_size (Gtk.IconSize.LARGE)
        self.box_1.append (
            self.img_installing
        )

        # İlerleme
        self.box_1_progress = Gtk.Box (
            spacing = 6,
            hexpand = True,
            halign = Gtk.Align.FILL,
            orientation = Gtk.Orientation.VERTICAL
        )
        self.box_1.append (self.box_1_progress)

        self.lbl_installing = Gtk.Label (
            halign = Gtk.Align.START
        )
        self.lbl_installing.set_markup (
            "<b>Kuruluyor</b>"
        )
        self.box_1_progress.append (self.lbl_installing)

        self.prc_progress = Gtk.ProgressBar (
            halign = Gtk.Align.FILL,
            vexpand = True,
        )
        self.box_1_progress.append (self.prc_progress)

        # Düğme kutusu
        self.box_1_btn = Gtk.Box (
            spacing = 6
        )
        self.box_1.append (self.box_1_btn)

        self.btn_1_cancel = Gtk.Button(
            label = "İptal"
        )
        functions.clicked(self.btn_1_cancel, self.on_cancel_clicked)
        self.box_1_btn.append (self.btn_1_cancel)

    def on_cancel_clicked(self, widget):
        self.close()
    def on_install_clicked(self, widget):
        self.stk_main.set_visible_child(self.box_1)

class InstallerApp (Adw.Application):
    def __init__ (self, **kwargs):
        super().__init__ (**kwargs)
        self.connect (
            'activate', 
            self.on_activate
        )

    def on_activate (self, app):
        self.win = InstallerWindow (application = app)
        self.win.present ()

app = InstallerApp(application_id = "io.github.afacanc38.appiload")
app.run(sys.argv)