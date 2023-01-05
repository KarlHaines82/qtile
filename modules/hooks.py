from libqtile import hook
from libqtile.log_utils import logger

from os.path import expanduser
import subprocess

@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog'
        or window.window.get_wm_transient_for()):
        logger.debug("{window} marked as floating" % window)
        window.floating = True

@hook.subscribe.startup_once
def autostart():
    run_autostart = expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([run_autostart])
