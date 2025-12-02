from gi.repository import Gtk

class Navigation(Gtk.Box):
    def __init__(self, on_nav_change):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.on_nav_change = on_nav_change

        self.set_margin_start(8)
        self.set_margin_end(8)
        self.set_margin_top(8)
        self.set_margin_bottom(8)

        # ----- Dashboard -----
        title = Gtk.Label()
        title.set_markup("<b>Dashboard</b>")
        title.set_xalign(0)
        self.pack_start(title, False, False, 0)

        self.pack_start(self._make_button("overview", "Overview", "view-dashboard"), False, False, 0)
        self.pack_start(self._make_button("groups", "Groups", "folder"), False, False, 0)

        separator = Gtk.Separator()
        self.pack_start(separator, False, False, 10)

        # ----- Others -----
        self.pack_start(self._make_button("logs", "Logs", "text-x-generic"), False, False, 0)
        self.pack_start(self._make_button("profiles", "Profiles", "avatar-default"), False, False, 0)
        self.pack_start(self._make_button("settings", "Settings", "preferences-system"), False, False, 0)

    def _make_button(self, page_id, text, icon_name):
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        icon = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.MENU)
        label = Gtk.Label(text)
        label.set_xalign(0)

        box.pack_start(icon, False, False, 0)
        box.pack_start(label, True, True, 0)

        event = Gtk.EventBox()
        event.add(box)
        event.get_style_context().add_class("nav-item")

        event.connect("button-press-event", lambda *_: self.on_nav_change(page_id))
        return event
