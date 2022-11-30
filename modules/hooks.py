from libqtile import hook
from os.path import expanduser
from os import environ
import subprocess

@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog'
        or window.window.get_wm_transient_for()):
        window.floating = True

@hook.subscribe.startup_once
def autostart():
    run_autostart = expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([run_autostart])
    environ['QT_QPA_PLATFORMTHEME']='qt5ct'
    environ['EDITOR']='nvim-qt'
