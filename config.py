#
#   Karl's qtile config
#   telegram: @linuxkarl615
#
import os
from os.path import expanduser
from libqtile.lazy import lazy
from modules.keys import keys, mod
from modules.hooks import * 
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.screens import screens
from modules.mouse import mouse
#from modules.scratchpad import *

widget_defaults = dict(
    font="GE Inspira",
    fontsize=16,
    custom_icon_paths=[expanduser("~/.config/qtile/icons"),expanduser("~/.icons")],
)
extension_defaults = widget_defaults.copy()

auto_fullscreen = True
auto_minimize = False
bring_front_click = True
cursor_warp = False
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
wl_input_rules = None
wmname = "qtile"
