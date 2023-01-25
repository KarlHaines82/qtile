from libqtile.config import Screen, Bar
from libqtile.lazy import lazy
from libqtile import bar, widget
from os.path import expanduser
from theme import theme_colors
from qtile_extras.widget import brightnesscontrol, upower
from qtile_extras.widget import statusnotifier, alsavolumecontrol
import mywidgets

ssep = {
    'background': "#292d3e",
    'foreground': '#ffffff',
    'padding': 8,
    'linewidth': 0,
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename=expanduser("~/.config/qtile/icons/arch01.png"),
                    mouse_callbacks={
                        'Button1': lazy.spawn(
                            "rofi -modi combi,window,drun -combi window,drun -show drun")
                    },
                    background=theme_colors[0],
                    width=18,
                    height=18,
                    padding=5,
                    margin=2,
                    scale=0.7,
                ),
                widget.GroupBox(
                    name="GroupBoxTop",
                    font='CaskaydiaCove Nerd Font SemiLight',
                    fontsize=16,
                    margin_y=2,
                    margin_x=0,
                    padding_y=2,
                    padding_x=2,
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
                widget.Sep(**ssep),
                widget.TextBox(
                    fontsize=22,
					text="\uE0C5",
                    foreground=theme_colors[11],
                    background=theme_colors[0],
                    margin_x=4,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    background=theme_colors[11],
                    foreground=theme_colors[9],
                    padding=0,
                ),
                widget.Image(
                    filename=expanduser(
                        "~/.config/qtile/icons/cpu.svg"),
                    width=18,
                    height=18,
                    margin_x=4,
                    background=theme_colors[11]
                ),
                widget.CPU(
                    foreground=theme_colors[0],
                    background=theme_colors[11],
                    padding=0,
                    margin_x=4,
                    format=" {load_percent}%",
                    width=45
                ),
                widget.TextBox(
                    fontsize=22,
					text=" \uE0C5",
                    background=theme_colors[11],
                    foreground=theme_colors[4],
                    margin_x=4,
                    padding=0,
                ),
                widget.Sep(
                    background=theme_colors[4],
                    padding = 5,
                ),
                widget.Image(
                    filename=expanduser(
                        "~/.config/qtile/icons/gnome-dev-memory.svg"),
                    width=18,
                    height=18,
                    margin_x=4,
                    background=theme_colors[4],
                ),
                widget.Memory(
                    foreground="#ffffff",
                    background=theme_colors[4],
                    mouse_callbacks={'Button1': lazy.spawn('kitty btop')},
                    padding=0,
                    margin_x=4,
                    measure_mem='G',
                ),
                widget.TextBox(
                    fontsize=22,
                    text=" \uE0C5",
                    background=theme_colors[4],
                    foreground=theme_colors[8],
                    padding=0,
                    margin_x=4,
                ),
                mywidgets.CapsNumWidget(
                    background=theme_colors[8],
                    margin_x=8,
                ),
                widget.TextBox(
                    fontsize=22,
					text="\uE0C5",
                    background=theme_colors[8],
                    foreground=theme_colors[0],
                    margin_x=4,
                    padding=0,
                ),
                widget.Sep(**ssep),
                #widget.Systray(
                #    icon_size=18,
                #), 
                statusnotifier.StatusNotifier(
                    icon_size=24,
                    icon_theme=expanduser('~/.local/share/icons/McMojave-circle-blue-dark/'),
                    padding=2,
                    margin_x=2,
                ),
                brightnesscontrol.BrightnessControl(),
                # alsavolumecontrol.ALSAWidget(
                #     icon_size=18,
                #     mode='both',
                #     theme_path=expanduser('~/.config/qtile/icons'),
                # ),
                upower.UPowerWidget(),
                widget.Clock(
                    font="OpenDyslexic Nerd Font",
                    fontsize=22,
                    format="%I:%M",
                    padding=4,
                    margin_y=4,
                ),
                widget.TextBox(
                    fontsize=22,
                    mouse_callbacks={'Button1': lazy.shutdown()},
                    text="",
                    padding_x=0,
                    margin_y=2,
                ),
            ],
            32,
            background=theme_colors[0],
        ),
        wallpaper_mode='stretch',
        wallpaper=expanduser('~/.config/qtile/icons/background.png'),
    ),
]
