from os import environ
from os.path import expanduser
import shlex
from subprocess import Popen

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


group_app_subscriptions = [
    ['null'],   # 0, any w/o a script                                 #
    ['1 ', 'alacritty', 'kitty', 'konsole'],                    # Group 1
    ['2 ', 'firefox', 'chromium', 'qutebrowser'],  # Group 2
    ['3 ', 'vim', 'nvim', 'nvim-qt', 'neovide', 'kate', 'xed'],  # Grup 3
    ['4 ', 'null'],                                             # Group 4
    ['5 ', 'dolphin', 'pcmanfm-qt', 'thunar'],                  # Group 5
    ['6 ', 'telegram-desktop', 'caprine', 'hexchat'],           # Group 6
    ['7 ', 'spotify', 'cava', 'xmms'],                          # Group 7
    ['8 ', 'gnu image manipulation program'],                   # Group 8
    ['9 ', 'null'],                                             # Group 9
]


@hook.subscribe.client_new
def send_to_proper_workspace(client):
    for gsub in group_app_subscriptions:
        client_info = client.info()
        client_name = client_info['name'].lower()
        client_wm_class = str(client_info['wm_class'][1]).lower()
        if client_name in gsub:
            logger.warn('Match name: %s' % client_name)
            client.togroup(gsub[0], switch_group=True)
        else:
            if client_wm_class in gsub:
                logger.warn('Match class: %s' % client_wm_class)
                client.togroup(gsub[0], switch_group=True)
            # else:
            #     logger.warn('No match for name: %s ' % client_name)


@hook.subscribe.client_new
def dialogs(window):
    if (window.window.get_wm_type() == 'dialog' or
       window.window.get_wm_transient_for()):
        window.floating = True


@hook.subscribe.startup_complete
def autostart():
    logger.warn("Beginning autostart() procedure...")
    autostarts = [
        "dex -ae qtile -s ~/.config/autostart",
        "sh -c ~/.config/conky/startconky.sh",
        "picom",
        "dunst",
        "blueman-applet",
        "copyq",
        "nm-applet --indicator",
    ]
    for p in autostarts:
        ppath = expanduser(p)
        proc = shlex.split(ppath)
        Popen(proc)


logger.warn('Config loaded')
