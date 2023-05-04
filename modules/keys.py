from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
editor = "neovide"
aterminal = "wezterm"
terminal = "kitty"
dmenu = "rofi -modi run,window,combi -combi run,window -show combi"
browser = "chromium"
firefox = "firefox"
afileman = "thunar"
fileman = "dolphin"
telegram = "telegram-desktop"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # setup some app key bindings
    # TODO: add hotkeys for any user applications here
    #
    Key([mod], "Return", lazy.spawn(terminal),
        desc="Launch terminal"),
    Key([mod, "mod1"], "Return", lazy.spawn(aterminal),
        desc="Launch alternate terminal"),
    Key([mod], "d", lazy.spawn(dmenu), desc="Launch dmenu"),
    Key([mod, "mod1"], "e", lazy.spawn(afileman),
        desc="Launch alternate file manager"),
    Key([mod], "e", lazy.spawn(fileman),
        desc="Launch file manager"),
    Key([mod], "n", lazy.spawn(editor),
        desc="Launch my editor of choice"),
    Key([mod], "b", lazy.spawn(browser),
        desc="Launch chromium web browser"),
    Key([mod], "f", lazy.spawn(firefox),
        desc="Launch firefox web browser"),
    Key([mod], "s", lazy.spawn(
        "dex /usr/share/applications/spotify-adblock.desktop"),
        desc="Launch spotify"),
    Key([mod], "t", lazy.spawn(telegram),
        desc="Launch telegram"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down
    # in current stack. Moving out of range in Columns layout
    # will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up"),
    # Grow windows. If current window is on the edge of
    # screen and direction will be to screen edge -
    # window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),
    # Ratio grow and shink for use with monad-type layouts
    Key([mod], "i", lazy.layout.grow(),
        desc="Expand window size ratio by .05"),
    Key([mod], "m", lazy.layout.shrink(),
        desc="Shrink window size ratio by .05"),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(),
        desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]
