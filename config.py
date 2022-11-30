#
#   Karl's qtile config
#   telegram: @linuxkarl615
#
from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy
from os.path import expanduser
import os
from modules.keys import keys, mod
from modules.hooks import * 
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.screens import screens
from modules.mouse import mouse

widget_defaults = dict(
    font="Ubuntu Nerd Font",
    fontsize=16,
    icon_theme='Shiny-Color-Dark-Icons',
)
extension_defaults = widget_defaults.copy()

auto_fullscreen = True
auto_minimize = True
bring_front_click = True
cursor_warp = False
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
wl_input_rules = None
wmname = "qtile"
