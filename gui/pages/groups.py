import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GroupsPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label(label="Groups Page", xalign=0)
        self.pack_start(label, False, False, 20)
