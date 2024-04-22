from modules.keys import keys, mod
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.screens import screens
from modules.mouse import mouse

from os import environ
from os.path import expanduser
import shlex
from subprocess import Popen

from libqtile.log_utils import logger
from logging import WARNING
from libqtile import hook, qtile
from libqtile.lazy import lazy


qtile_core = str(qtile.core.name)
def blab(s):
    logger.log(msg=s, exc_info=True, level=WARNING)


mod = mod
keys = keys
groups = groups
layouts = layouts
floating_layout = floating_layout
screens = screens
mouse = mouse


widget_defaults = dict(
    font="DroidSans Nerd Font",
    fontsize=16,
    custom_icon_paths=[
        expanduser("~/.config/qtile/icons"),
        expanduser("~/.local/share/icons"),
    ],
)
extension_defaults = widget_defaults.copy()

# environment variables
environ['QT_QPA_PLATFORMTHEME'] = 'qt6ct'
environ['NEOVIDE_MULTIGRID'] = 'true'

auto_fullscreen = True
auto_minimize = False
bring_front_click = True
cursor_warp = False
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
wmname = "qtile"

group_app_subscriptions = [
    ['null'],                                                                          # 0, any w/o a script
    ['1 ', 'alacritty', 'kitty', 'wezterm', 'konsole'],           # Group 1
    ['2 ', 'firefox', 'chromium', 'qutebrowser', 'librewolf',\
            'vivaldi', 'angelfish', 'midori' ],                           # Group 2
    ['3 ', 'vim', 'nvim', 'nvim-qt', 'neovide', 'kate'],        # Group 3
    ['4 ', 'codium', 'geany', 'kdevelop'],                         # Group 4
    ['5 ', 'dolphin', 'pcmanfm-qt', 'thunar'],                    # Group 5
    ['6 ', 'telegram-desktop', 'caprine', 'hexchat'],          # Group 6
    ['7 ', 'spotify', 'xmms'],                                  # Group 7
    ['8 ', 'gnu image manipulation program'],               # Group 8
    ['9 ', 'null'],                                                                # Group 9
]

autostarts = [
    "dbus-update-activation-environment --systemd --all",
    "dex -ae qtile",
    "dunst",
    "xsettingsd",
]

if qtile_core == 'x11':
    autostarts.extend(["picom"])
elif qtile_core == 'wayland':
    autostarts.extend([""])


autostarts_running = []


@hook.subscribe.client_new
def send_to_proper_workspace(client):
    for gsub in group_app_subscriptions:
        client_info = client.info()
        client_name = client_info['name'].lower()
        client_wm_class = str(client_info['wm_class'][1]).lower()
        if client_name in gsub:
            blab('Match name: %s' % client_name)
            client.togroup(gsub[0], switch_group=True)
        elif client_wm_class in gsub:
            blab("Match class: %s" % client_wm_class)
            client.togroup(gsub[0], switch_group=True)
        else:
            blab('No match for name: %s ' % client_name)


@hook.subscribe.client_new
def dialogs(window):
    if (window.window.get_wm_type == 'dialog'): 
        window.floating = True
        lazy.window.center(window)


@hook.subscribe.startup_complete
def autostart():
    blab("Beginning autostart() procedure")
    for p in autostarts:
        ppath = expanduser(p)
        proc = shlex.split(ppath)
        subproc = Popen(proc)
        autostarts_running.append(subproc)


@hook.subscribe.shutdown
def cleanup():
    for p in autostarts_running:
        blab('Killing process: '+str(p.args)+' (pid '+str(p.pid)+') ...')
        p.kill()

