import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GLib, Gdk

from navigation import Navigation
from pages.overview import OverviewPage
from pages.groups import GroupsPage
from pages.logs import LogsPage
from pages.profiles import ProfilesPage
from pages.settings import SettingsPage


class App:
    def __init__(self):
        self.window = Gtk.Window(title="SingBox GUI")
        self.window.set_default_size(1000, 650)
        self.window.connect("destroy", Gtk.main_quit)

        self.load_css()

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.window.add(hbox)

        # Sidebar Navigation
        self.nav = Navigation(self.on_nav_selected)
        hbox.pack_start(self.nav, False, False, 0)

        # Stack for pages
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(200)

        # Register pages
        self.stack.add_named(OverviewPage(), "overview")
        self.stack.add_named(GroupsPage(), "groups")
        self.stack.add_named(LogsPage(), "logs")
        self.stack.add_named(ProfilesPage(), "profiles")
        self.stack.add_named(SettingsPage(), "settings")

        hbox.pack_start(self.stack, True, True, 0)

    def on_nav_selected(self, name):
        self.stack.set_visible_child_name(name)

    def load_css(self):
        provider = Gtk.CssProvider()
        provider.load_from_path("gui/resources/style.css")

        screen = Gdk.Screen.get_default()

        Gtk.StyleContext.add_provider_for_screen(
            screen,
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_USER
        )

    def run(self):
        self.window.show_all()
        Gtk.main()
