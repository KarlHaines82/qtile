from os import environ
from os.path import expanduser
import shlex
from subprocess import Popen
# from qtile_extras.widget.decorations import \
# PowerLineDecoration as powerline_decor

from libqtile.log_utils import logger
from libqtile import hook

from modules.keys import keys, mod
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.screens import screens
from modules.mouse import mouse

mod = mod
keys = keys
groups = groups
layouts = layouts
floating_layout = floating_layout
screens = screens
mouse = mouse

widget_defaults = dict(
    font="CaskaydiaCove Nerd Font SemiLight",
    fontsize=14,
    icon_paths=[
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


@hook.subscribe.client_new
def dialogs(window):
    if (window.window.get_wm_type() == 'dialog' or
       window.window.get_wm_transient_for()):
        window.floating = True


@hook.subscribe.startup_complete
def autostart():
    logger.info("Beginning autostart() procedure...")
    autostarts = [
        "dex -ae qtile -s ~/.config/autostart",
        "sh -c ~/.config/conky/startconky.sh",
        "picom",
        "dunst",
        "blueman-applet",
        "copyq",
        "nm-tray",
    ]
    for p in autostarts:
        ppath = expanduser(p)
        proc = shlex.split(ppath)
        Popen(proc)


logger.debug('Config loaded')
