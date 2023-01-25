# pyright: reportMissingImports=false
from os import environ
from os.path import expanduser
from libqtile.log_utils import logger
from modules.hooks import *
from modules.keys import keys, mod
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.screens import screens
from modules.mouse import mouse

widget_defaults = dict(
    font="CaskaydiaCove Nerd Font SemiLight",
    fontsize=16,
    custom_icon_paths=[
        expanduser("~/.config/qtile/icons"),
        expanduser("~/.local/share/icons"),
    ],
)
extension_defaults = widget_defaults.copy()
# environment variables
environ['QT_QPA_PLATFORMTHEME'] = 'qt5ct'
environ['NEOVIDE_MULTIGRID'] = 'true'

auto_fullscreen = True
auto_minimize = False
bring_front_click = True
cursor_warp = False
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
wl_input_rules = None
wmname = "qtile"

logger.debug('Config loaded')
