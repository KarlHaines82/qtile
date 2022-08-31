from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import subprocess, os
from os.path import expanduser
from theme import theme_colors
#from libqtile.utils import guess_terminal

mod = "mod4"
#terminal = guess_terminal()
terminal = "alacritty"
dmenu = "rofi -show drun"
browser = "firefox"
fileman = "dolphin"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Ratio grow and shink for use with monad-type layouts
    Key([mod], "i", lazy.layout.grow(), desc="Expand window size ratio by .05"),
    Key([mod], "m", lazy.layout.shrink(), desc="Shrink window size ratio by .05"),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
        ),
    # setup some key bindings
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn(dmenu), desc="Launch dmenu"),
    Key([mod], "e", lazy.spawn(fileman), desc="Launch file manager"),
    Key([mod], "f", lazy.spawn(browser), desc="Launch web browser"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    ]

# Set up our groups and bind their respective keys, got a few workarounds
# in effect since we're using these fancy icons
group_names = ["1  ", "2  ", "3  ", "4  ", "5  ", "6  ", "7  ", "8  ", "9  "]
# Set some default layouts
groups = []
for n in group_names:
    name=n[:1]
    match(name):
        case '1'|'2':
            groups.append(Group(n, layout='max'))
        case '3'|'9':
            groups.append(Group(n, layout='treetab'))
        case '4'|'5':
            groups.append(Group(n, layout='floating'))
        case _:
            groups.append(Group(n, layout='monadtall'))
# now bind the keys using the first char in each group name
for g in groups:
    keys.extend([
        Key([mod], g.name[:1], lazy.group[g.name].toscreen(), 
            desc="Switch to group {}".format(g.name)),
        Key([mod, "shift"], g.name[:1], lazy.window.togroup(g.name,switch_group=True), 
            desc="Move current container to group {}".format(g.name)),
        ])

# Configure the layouts variable
layouts = [
    layout.Max(),
    layout.MonadTall(
        ratio=0.75,
        max_ratio=0.8,
        min_ratio=0.5,
        change_ratio=0.05,
        ),
    layout.TreeTab(
        fontsize=11,
        sections=["TreeTab"],
        section_fontsize=10,
        active_bg=theme_colors[0],
        padding_left=0,
        padding_x=0,
        padding_y=3,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200
        ),
    layout.Tile(),
    layout.Floating(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    ]

widget_defaults = dict(
    font="NotoSerif Nerd Font",
    fontsize=16,
    )
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename=expanduser("~/.config/qtile/icons/arch01.png"),
                    mouse_callbacks={'Button1': lazy.spawn("/usr/bin/kitty")},
                    background=theme_colors[0],
                    width=18,
                    height=18,
                    padding=2,
                    margin_x=2,
                    margin_y=2,
                    ),
                widget.GroupBox(
                    name="GroupBoxTop",
                    margin_y=4,
                    margin_x=0,
                    padding_y=0,
                    padding_x=0,
                    borderwidth=3,
                    active=theme_colors[-2],
                    inactive=theme_colors[-1],
                    rounded=True,
                    highlight_method='line',
                    urgent_alert_method='block',
                    urgent_border=theme_colors[8],
                    this_current_screen_border=theme_colors[9],
                    this_screen_border=theme_colors[4],
                    other_current_screen_border=theme_colors[0],
                    other_screen_border=theme_colors[0],
                    foreground=theme_colors[11],
                    background=theme_colors[0],
                    disable_drag=True,
                    markup=True,
                    ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[expanduser("~/.config/qtile/icons")],
                    foreground=theme_colors[9],
                    background=theme_colors[0],
                    padding=5,
                    margin_x=4,
                    margin_y=4,
                    scale=0.7,
                    ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                        },
                        name_transform=lambda name: name.upper(),
                    ),
                #widget.TextBox("&lt;MOD-r&gt; to spawn cmd", foreground="#d75f5f"),
                widget.Systray(
                    icon_size=23,
                    padding=2,
                    padding_x=4,
                    ),
                widget.Clock(
                    font='OpenDyslexic',
                    fontsize=22,
                    format="%I:%M",
                    padding=4,
                    padding_left=5,
                    ),
                widget.TextBox(
                    fontsize=26,
                    mouse_callbacks={'Button1': lazy.shutdown()},
                    text="ﮊ",
                    padding=2,
                    margin_x=2,
                    ),
                ],
            26,
            background=theme_colors[0],
            ),
        ),
    ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    ]

#dgroups_key_binder = None
#dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="dunst"),
        Match(wm_class="gimp"),
        Match(wm_class="keepassxc"),
        Match(wm_class="telegram-desktop"),
        Match(wm_class="kvantummanager"),
        Match(wm_class="qt5ct"),
        Match(wm_class="lxappearance"),
        ]
    )

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog'
        or window.window.get_wm_transient_for()):
        window.floating = True

@hook.subscribe.startup_once
def autostart():
    home = expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
    os.environ['QT_QPA_PLATFORMTHEME']='qt5ct'
    os.environ['EDITOR']='nvim-qt'

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
